from baton.apps.base import Authentication


class GoogleDriveAuthentication(Authentication):
    """Authenticator for Google Drive

    This class provides a basic interface to authenticate an account for
    Google Drive. It implements the bastract base methods of the Authentication
    class.

    """
    def __init__(self, arg):
        super(GoogleDriveAuthentication, self).__init__()
        self.arg = arg
