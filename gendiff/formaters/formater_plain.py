from gendiff.formaters.formater_string import formater_string


def upgrade_str(value):
    if isinstance(value, dict):
        return '[complex value]'
    new_value = repr(value) if isinstance(value, str) else value
    return formater_string(new_value)


def formater_plain(diff):
    def build_diff(diff, parent=''):
        result = []
        for node in diff:
            action_type, key = node.get('action_type'), node.get('key')
            value, new_value = node.get("value"), node.get('new_value')
            full_key = f"{parent}.{key}" if parent else key
            if action_type == 'children':
                result.extend(build_diff(value, full_key))
            elif action_type == 'added':
                result.append(f"Property '{full_key}' was added with value: {upgrade_str(value)}")
            elif action_type == 'removed':
                result.append(f"Property '{full_key}' was removed")
            elif action_type == 'changed':
                result.append(
                    f"Property '{full_key}' was updated. From {upgrade_str(value)} to {upgrade_str(new_value)}"
                )
        return result
    return build_diff(diff)
