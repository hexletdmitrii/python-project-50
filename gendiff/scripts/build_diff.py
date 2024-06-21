def build_diff(data1, data2):
    result = []
    for key in sorted(set(data1.keys() | data2.keys())):
        value1 = data1.get(key)
        value2 = data2.get(key)
        if key not in data1.keys():
            result.append({
                'key': key,
                'action_type': 'added',
                'value': data2.get(key)
            })
        elif key not in data2.keys():
            result.append({
                'key': key,
                'action_type': 'removed',
                'value': data1.get(key)
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
