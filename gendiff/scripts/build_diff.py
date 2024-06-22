def build_diff(data1, data2):
    result = []

    if not isinstance(data1, dict):
        data1 = {}
    if not isinstance(data2, dict):
        data2 = {}

    for key in sorted(set(data1.keys()) | set(data2.keys())):
        value1 = data1.get(key)
        value2 = data2.get(key)
        if key not in data1:
            result.append({
                'key': key,
                'action_type': 'added',
                'value': value2
            })
        elif key not in data2:
            result.append({
                'key': key,
                'action_type': 'removed',
                'value': value1
            })
        elif isinstance(value1, dict) and isinstance(value2, dict):
            result.append({
                'key': key,
                'action_type': 'children',
                'value': build_diff(value1, value2)
            })
        elif value1 == value2:
            result.append({
                'key': key,
                'action_type': 'not_changed',
                'value': value1
            })
        else:
            result.append({
                'key': key,
                'action_type': 'changed',
                'value': value1,
                'new_value': value2
            })
    return result
