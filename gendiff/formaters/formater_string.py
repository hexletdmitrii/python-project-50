def formater_string(value):
    if value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    elif not isinstance(value, dict):
        return str(value)
