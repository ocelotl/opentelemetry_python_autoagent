from abc import ABCMeta, abstractmethod


class BasePlugin(metaclass=ABCMeta):

    @abstractmethod
    def get_options(self):
        """
        Returns a dictionary of command line options
        """


__all__ = ['BasePlugin']
