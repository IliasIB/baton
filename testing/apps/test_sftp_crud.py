from baton.apps.sftp.sftp_remote_crud import SFTPRemoteCRUD
import pytest


def test_sftp_remote_crud(sftpserver, tmpdir):
    """Test creation, reading, updating and deleting of files via SFTP"""
    with sftpserver.serve_content({'a_dir': {'somefile.txt': "File content"}}):
        # Get interface object
        sftp_interface = SFTPRemoteCRUD(
            sftpserver.host,
            username="user",
            password="pw",
            port=sftpserver.port
        )

        # Make file for creation testing
        write_path = tmpdir.join("test_file")
        write_path.write("test")

        # Upload file, dowload and check if it hasn't changed
        sftp_interface.create(
            local_path=write_path
        )
        read_path = tmpdir.join("test_read")
        sftp_interface.read(
            local_path=read_path,
            remote_path="test_file"
        )
        """An extra b is added because the mock SFTP library adds this to
        uploaded files
        """
        assert "b'test'" == read_path.read()

        # Check updating of files
        sftp_interface.update(
            remote_path="test_file",
            name="test_rename"
        )
        read_path = tmpdir.join("test_rename")
        sftp_interface.read(
            local_path=read_path,
            remote_path="test_rename"
        )

        # Check deletion of files
        sftp_interface.delete(
            remote_path="test_rename"
        )
        with pytest.raises(IOError):
            read_path = tmpdir.join("test_delete")
            sftp_interface.read(
                local_path=read_path,
                remote_path="test_rename"
            )
