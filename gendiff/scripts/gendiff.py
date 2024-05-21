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


def generate_diff(file1, file2):
    set1 = set(file1.keys())
    set2 = set(file2.keys())
    result = '{'
    for i in sorted(set1 | set2):
        if file1.get(i) == file2.get(i):
            result = result + '\n    ' + i + ': ' + str(file1[i]).lower()
        if (
            i in set1 - set2 or
            (i in set1 and i in set2 and file1.get(i) != file2.get(i))
        ):
            result = result + '\n  - ' + i + ': ' + str(file1[i]).lower()
        if (
            i in set2 - set1 or
            (i in set1 and i in set2 and file1.get(i) != file2.get(i))
        ):
            result = result + '\n  + ' + i + ': ' + str(file2[i]).lower()
    result = result + '\n}'
    return result


if __name__ == '__main__':
    main()
