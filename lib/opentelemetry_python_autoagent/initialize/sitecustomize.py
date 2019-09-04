from pkg_resources import iter_entry_points


for entry_point in iter_entry_points(
    group='opentelemetry_python_autoagent_10'
):

    try:

        entry_point.load()().monkeypatch()

    except Exception as error:

        print(entry_point.name)
        print(error)
