from gendiff.formaters.formater_string import formater_string


def formater_stylish(diff):
    def build_stylish(diff, deep=1):
        result = []
        space = ' ' * (deep - 1)
        for node in diff:
            action_type, key = node.get('action_type'), node.get('key')
            value, new_value = node.get("value"), node.get('new_value')

            if action_type == 'children':
                result.append(f'{space}    {str(key)}: {{\n{build_stylish(value, deep + 4)}\n{space}    }}')
            elif action_type == 'added':
                result.append(f'{space}  + {str(key)}: {string(value, deep + 4)}')
            elif action_type == 'removed':
                result.append(f'{space}  - {str(key)}: {string(value, deep + 4)}')
            elif action_type == 'changed':
                result.append(f'{space}  - {str(key)}: {string(value, deep + 4)}')
                result.append(f'{space}  + {str(key)}: {string(new_value, deep + 4)}')
            elif action_type == 'not_changed':
                result.append(f'{space}    {str(key)}: {string(value, deep + 4)}')
        if deep == 1:
            return '{\n' + '\n'.join(result) + '\n}'
        return '\n'.join(result)
    return build_stylish(diff)


def string(value, deep=1):
    if not isinstance(value, dict):
        return formater_string(value)
    space = ' ' * (deep - 1)
    result = ['{']
    for key in value.keys():
        result.append(f'{space}    {key}: {string(value[key], deep + 4)}')
    result.append(space + '}')
    return '\n'.join(result)
