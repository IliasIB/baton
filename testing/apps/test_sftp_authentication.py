from baton.apps.sftp.sftp_authentication import SFTPAuthentication


def test_sftp_authenticate(sftpserver):
    with sftpserver.serve_content({'a_dir': {'somefile.txt': "File content"}}):
        with SFTPAuthentication.authenticate(
            host=sftpserver.host,
            port=sftpserver.port,
            username="user",
            password="pw"
        ) as sftp_connection:
            assert sftp_connection.isfile("/a_dir/somefile.txt")
