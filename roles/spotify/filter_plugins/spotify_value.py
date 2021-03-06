def spotify_value(value):
    if isinstance(value, str):
        return f'"{value}"'
    elif isinstance(value, bool):
        return 'true' if value else 'false'
    else:
        return str(value)


class FilterModule(object):
    def filters(self):
        return {'spotify_value': spotify_value}
