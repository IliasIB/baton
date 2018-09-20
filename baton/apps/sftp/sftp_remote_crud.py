from baton.apps.base.remote_crud import RemoteCRUD
from baton.apps.sftp.sftp_authentication import SFTPAuthentication


class SFTPRemoteCRUD(RemoteCRUD):
    """Remote CRUD for SFTP

    This class provides a basic interface to use basic CRUD operations for
    the SFTP protocol. It implements the abstract base methods of the
    RemoteCRUD class.

    """

    def __init__(self, hostname, username, password, port=22):
        self.sftp_connection = SFTPAuthentication.authenticate(
            hostname,
            username=username,
            password=password,
            port=port
        )

    def create(self, local_path, remote_path=None):
        """Creates a file on the SFTP server

        :param local_path The path of the file that should be uploaded
        :param remote_path The path where the file should be uploaded to; if
        not used, the basename of local_path will be used

        :exception IOError If remotepath doesn’t exist
        :exception OSError If localpath doesn’t exist
        """
        self.sftp_connection.put(
            localpath=local_path,
            remotepath=remote_path
        )

    def read(self, remote_path, local_path=None):
        """Reads a file from the SFTP server

        :param remote_path The path of the file that should be downloaded
        :param local_path The path where the file should be downloaded to; if
        not used, the basename of remote_path will be used

        :exception IOError If remotepath doesn’t exist
        :exception OSError If localpath doesn’t exist
        """
        self.sftp_connection.get(
            remotepath=remote_path,
            localpath=local_path
        )

    def update(self, local_path=None, remote_path=None, name=None):
        """Updates a file on the SFTP server

        :param local_path The path of the file that should be used to
        overwrite the remote file
        :param remote_path The path to the file that should be overwritten; if
        not used, the basename of local_path will be used
        :param name The new name of the remote file

        :exception IOError If remotepath doesn’t exist
        :exception OSError If localpath doesn’t exist
        """
        if local_path is not None:
            self.sftp_connection.put(
                localpath=local_path,
                remotepath=remote_path
            )
        if name is not None and remote_path is not None:
            self.sftp_connection.rename(
                remote_src=remote_path,
                remote_dest=name
            )

    def delete(self, remote_path):
        """Deletes a file or folder from the SFTP server

        :param remote_path The path to the folder or file that should be
        deleted

        :exception IOError If folder or file doesn't exist
        """
        if self.sftp_connection.isfile(remotepath=remote_path):
            self.sftp_connection.remove(remotefile=remote_path)
        else:
            self.sftp_connection.rmdir(remotepath=remote_path)
