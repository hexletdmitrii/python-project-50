import json
from gendiff.scripts.parser_file import parser_file


def formater_json(file1, file2):
    file1 = parser_file(file1)
    file2 = parser_file(file2)
    def build_diff(file1, file2):
        result = []
        keys = sorted(set(file1.keys()) | set(file2.keys()))

        for key in keys:
            if key not in file1:
                result.append({"key": key, "action_type": "added", "value": file2[key]})
            elif key not in file2:
                result.append({"key": key, "action_type": "removed", "value": file1[key]})
            elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
                result.append({"key": key, "action_type": "children", "value": build_diff(file1[key], file2[key])})
            elif file1[key] != file2[key]:
                result.append({"key": key, "action_type": "changed", "value": file1[key], "new_value": file2[key]})
            else:
                result.append({"key": key, "action_type": "not_changed", "value": file1[key]})
        return result

    result = build_diff(file1, file2)
    return json.dumps(result, indent=4)
