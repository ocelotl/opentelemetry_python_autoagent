from abc import ABCMeta, abstractmethod


class BasePlugin(metaclass=ABCMeta):

    @abstractmethod
    def run(self, path):
        """
        Runs the file defined in path
        """


__all__ = ['BasePlugin']
