from gendiff.scripts.parser_file import parser_file


def formater_plain(file1_, file2_):
    file1_ = parser_file(file1_)
    file2_ = parser_file(file2_)
    def build_diff(file1, file2, parent=''):
        result = []
        keys = sorted(set(file1.keys()) | set(file2.keys()))
        for key in keys:
            full_key = f"{parent}.{key}" if parent else key
            if key not in file1:
                value = '[complex value]' if isinstance(file2[key], dict) else repr(file2[key]).lower()
                result.append(f"Property '{full_key}' was added with value: {value}")
            elif key not in file2:
                result.append(f"Property '{full_key}' was removed")
            elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
                result.extend(build_diff(file1[key], file2[key], full_key))
            elif file1[key] != file2[key]:
                old_value = '[complex value]' if isinstance(file1[key], dict) else repr(file1[key]).lower()
                new_value = '[complex value]' if isinstance(file2[key], dict) else repr(file2[key]).lower()
                if new_value == 'none':
                    new_value = 'null'
                result.append(f"Property '{full_key}' was updated. From {old_value} to {new_value}")
        return result
    return build_diff(file1_, file2_)
