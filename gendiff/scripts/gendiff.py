import argparse
import json
from pathlib import Path
import yaml


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    file1 = parser_file(args.first_file)
    file2 = parser_file(args.second_file)
    print(generate_diff(file1, file2))


def parser_file(file_name):
    script_dir = Path(__file__).parent.parent
    file_path = script_dir / 'tests' / 'fixtures' / file_name
    if file_name.endswith('json'):
        with open(file_path) as f:
            return json.load(f)
    elif file_name.endswith('yml') or file_name.endswith('yaml'):
        with open(file_path) as f:
            return yaml.safe_load(f)
    elif file_name.endswith('txt'):
        with open(file_path) as f:
            return f.read()


def generate_diff(file1, file2, deep=1):
    set1 = set(file1.keys())
    set2 = set(file2.keys())
    result = []
    space = ' ' * (deep - 1)
    for key in sorted(set1 | set2):
        if key in set1 and key in set2 and (
            isinstance(file1[key], dict) and isinstance(file2[key], dict)
        ):
            result.append(f'{space}    {key}: {{\n{generate_diff(file1[key], file2[key], deep + 4)}\n{space}    }}')
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


if __name__ == '__main__':
    main()
