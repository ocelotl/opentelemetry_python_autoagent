from pkg_resources import iter_entry_points
from logging import getLogger, basicConfig, DEBUG

# FIXME avoid a hard dependency on a client like this one, create a
# plugin-based interface to handle this
from jaeger_client import Config

from click import command, option


getLogger('').handlers = []
basicConfig(format='%(message)s', level=DEBUG)

plugins = {}

for entry_point in iter_entry_points(
    group='opentelemetry_python_autoagent_10'
):

    plugins[entry_point.name] = entry_point


@command()
@option(
    '--plugin',
    default='minimal',
    help=(
        'Name of the plugin to use when running the'
        ' autoagent, options are:\n\n{}'.format('\n'.join(plugins.keys()))
    )
)
@option(
    '--path',
    help=(
        'Path of the file that is to be executed by the autoagent plugin'
    )
)
def run(plugin, path):

    print('Using plugin: {}'.format(plugin))

    try:

        plugin_class = plugins[plugin].load()

    except KeyError:

        raise RuntimeError('Invalid plugin: {}'.format(plugin))

    config = Config(
        config={
            'sampler': {
                'type': 'const',
                'param': 1,
            },
            'logging': True,
            'reporter_batch_size': 1,
        },
        service_name=plugin,
    )

    plugin_class().run(path, config.initialize_tracer())


__all__ = ['run']
