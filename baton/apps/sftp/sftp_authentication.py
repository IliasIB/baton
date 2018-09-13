from baton.apps.base import Authentication


class SFTPAuthentication(Authentication):
    """Authenticator for SFTP

    This class provides a basic interface to authenticate an account for
    the SFTP protocol. It implements the abstract base methods of the
    Authentication class.

    """
    def __init__(self, arg):
        super(SFTPAuthentication, self).__init__()
        self.arg = arg
