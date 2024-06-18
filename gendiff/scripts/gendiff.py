import argparse
from gendiff.formaters.formater_stylish import formater_stylish
from gendiff.formaters.formater_plain import formater_plain
from gendiff.formaters.formater_json import formater_json
from pathlib import Path
import yaml
import json


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', default='stylish', help='set format of output')
    args = parser.parse_args()
    file1 = parser_file(args.first_file)
    file2 = parser_file(args.second_file)
    print(args)
    print(generate_diff(file1, file2, args.format))


def generate_diff(file1, file2, format='stylish'):
    if format == 'stylish':
        return formater_stylish(file1, file2)
    elif format == 'plain':
        return '\n'.join(formater_plain(file1, file2))
    elif format == 'json':
        return formater_json(file1, file2)
    else:
        raise ValueError('Unknown format!!!')


def parser_file(file_name):
    if '/' in file_name:
        file_path = file_name
    else:
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


if __name__ == '__main__':
    main()
