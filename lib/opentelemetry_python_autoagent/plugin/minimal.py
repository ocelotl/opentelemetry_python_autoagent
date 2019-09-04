from opentelemetry_python_autoagent.plugin.base import BasePlugin


class MinimalPlugin(BasePlugin):

    def monkeypatch(self, tracer):

        pass


__all__ = ['MinimalPlugin']
