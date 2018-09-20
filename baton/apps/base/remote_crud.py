from abc import ABC, abstractmethod


class RemoteCRUD(ABC):
    """Abstract base class for CRUD operations of plugins

    To be able to use CRUD operations with a plugin, the plugin must have a
    RemoteCRUD class that implements the functions of this abstract class.
    The functions themselves are used for basic CRUD operations of a service.
    Note that functions of the plugin may extend beyond those in the
    base class if needed as long as the base functions are properly
    implemented.

    """

    @abstractmethod
    def create(self):
        """The implementation of this function should create a file"""
        pass

    @abstractmethod
    def read(self):
        """The implementation of this function should read a file's data"""
        pass

    @abstractmethod
    def update(self):
        """The implementation of this function should update a file"""
        pass

    @abstractmethod
    def delete(self):
        """The implementation of this function should delete a file"""
        pass
