from gendiff.scripts.parser_file import parser_file


def formater_stylish(file1_, file2_):
    file1_ = parser_file(file1_)
    file2_ = parser_file(file2_)
    def build_diff(file1, file2, deep=1):
        def string(value, deep=1):
            if value is None:
                return 'null'
            if isinstance(value, bool):
                return str(value).lower()
            if not isinstance(value, dict):
                return str(value)
            space = ' ' * (deep - 1)
            result = ['{']
            for key in value.keys():
                result.append(f'{space}    {key}: {string(value[key], deep + 4)}')
            result.append(space + '}')
            return '\n'.join(result)
        set1 = set(file1.keys())
        set2 = set(file2.keys())
        result = []
        space = ' ' * (deep - 1)
        for key in sorted(set1 | set2):
            if key in set1 and key in set2 and (
                isinstance(file1[key], dict) and isinstance(file2[key], dict)
            ):
                result.append(f'{space}    {key}: {{\n{build_diff(file1[key], file2[key], deep + 4)}\n{space}    }}')
            else:
                if key in set1 and key in set2 and file1.get(key) == file2.get(key):
                    result.append(f'{space}    {key}: {string(file1[key], deep + 4)}')
                else:
                    if key in set1:
                        result.append(f'{space}  - {key}: {string(file1[key], deep + 4)}')
                    if key in set2:
                        result.append(f'{space}  + {key}: {string(file2[key], deep + 4)}')
        if deep == 1:
            return '{\n' + '\n'.join(result) + '\n}'
        return '\n'.join(result)
    return build_diff(file1_, file2_)
