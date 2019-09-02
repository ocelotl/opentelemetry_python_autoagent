from pkg_resources import iter_entry_points

from click import command, option


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
def run(plugin):

    print('Using plugin: {}'.format(plugin))


__all__ = ['run']
