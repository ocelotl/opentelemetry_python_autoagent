from abc import ABCMeta, abstractmethod


class BasePlugin(metaclass=ABCMeta):

    @abstractmethod
    def monkeypatch(self, tracer):
        """
        Monkeypatches the specific package
        """


__all__ = ['BasePlugin']
