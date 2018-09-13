from abc import ABC, abstractmethod


class Authentication(ABC):
    """Abstract base class for the authentication of plugins

    To be able to authenticate with a plugin, the plugin must have an
    authentication class that implements the functions of this abstract class.
    The functions themselves are used for basic authentication to the
    plugin. Note that functions of the plugin may extend beyond those in the
    base class if needed as long as the base functions are properly
    implemented.

    """

    @abstractmethod
    def authorize(self):
        """The implementation of this function should authenticate the user"""
        pass
