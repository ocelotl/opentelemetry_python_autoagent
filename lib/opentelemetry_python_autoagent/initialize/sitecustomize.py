from pkg_resources import iter_entry_points

# FIXME avoid a hard dependency on a client like this one, create a
# plugin-based interface to handle this


for entry_point in iter_entry_points(
    group='opentelemetry_python_autoagent_10'
):

    entry_point.load()().monkeypatch()
