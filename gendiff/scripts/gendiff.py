import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    script_dir = Path(__file__).parent
    script_dir = script_dir.parent
    file_path1 = script_dir / 'tests' / 'fixtures' / args.first_file
    file_path2 = script_dir / 'tests' / 'fixtures' / args.second_file
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))
    print(generate_diff(file1, file2))


def generate_diff(file1, file2):
    set1 = set(file1.keys())
    set2 = set(file2.keys())
    result = 'gendiff filepath1.json filepath2.json\n{'
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
