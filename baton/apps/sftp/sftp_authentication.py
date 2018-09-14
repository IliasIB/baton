from baton.apps.base.authentication import Authentication
import pysftp


class SFTPAuthentication(Authentication):
    """Authenticator for SFTP

    This class provides a basic interface to authenticate an account for
    the SFTP protocol. It implements the abstract base methods of the
    Authentication class.

    """
    @staticmethod
    def authenticate(
            host,
            username,
            password,
            port=22,
            save_login=False,
            host_keys=None,
            private_key=None,
            private_key_pass=None,
            default_path=None):
        """Connects the client to the host with given username and password

        :param host The host with which a connection must be established
        :param username The username of the user that want to login
        :param password The password of the user that want to login
        :param port The port that the SFTP server listens on
        :param save_login If set, the credentials of the user are saved to the
        keyring service of the OS
        :param private_key The private key that the SFTP server may be using to
        ensure security
        :param private_key_pass A password to use on encrypted private keys
        :param default_path The path that should be used upon connection

        :return sftp_connection An active connection to the host

        :exception ConnectionException Thrown when a connection couldn't be
        established
        :exception CredentialException Thrown when credentials were incorrect
        :exception SSHException Thrown when there are issues with the SSH
        connection
        :exception AuthenticationException Thrown when there are issues while
        performing authentication
        :exception HostKeysException Thrown when an incorrect host key was
        given

        """
        # Check if user wants to use host keys
        cnopts = pysftp.CnOpts()
        if host_keys is None:
            cnopts.hostkeys = None
        else:
            cnopts.hostkeys.load(host_keys)

        # Make connection to the SFTP server
        sftp_connection = pysftp.Connection(
            host=host,
            port=port,
            username=username,
            password=password,
            cnopts=cnopts,
            private_key=private_key,
            private_key_pass=private_key_pass,
            default_path=default_path
        )
        return sftp_connection
