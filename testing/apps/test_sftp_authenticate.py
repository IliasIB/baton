from baton.apps.sftp.sftp_authentication import SFTPAuthentication


def test_sftp_authenticate(sftpserver):
    with sftpserver.serve_content({'a_dir': {'somefile.txt': "File content"}}):
        with SFTPAuthentication.authenticate(
            host=sftpserver.host,
            username="user",
            password="pw",
            port=sftpserver.port
        ) as sftp_connection:
            sftp_connection.isfile("/a_dir/somefile.txt")
