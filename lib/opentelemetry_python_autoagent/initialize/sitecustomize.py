from pkg_resources import iter_entry_points

# FIXME avoid a hard dependency on a client like this one, create a
# plugin-based interface to handle this
from jaeger_client import Config

tracer = Config(
    config={
        'sampler': {
            'type': 'const',
            'param': 1,
        },
        'logging': True,
        'reporter_batch_size': 1,
    },
    service_name='opentelemetry_python_autoagent',
).initialize_tracer()


for entry_point in iter_entry_points(
    group='opentelemetry_python_autoagent_10'
):

    entry_point.load()().monkeypatch(tracer)
