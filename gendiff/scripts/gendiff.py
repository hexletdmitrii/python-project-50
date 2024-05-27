import argparse
from gendiff.formaters.formater_stylish import formater_stylish
from gendiff.formaters.formater_plain import formater_plain
from gendiff.formaters.formater_json import formater_json
from gendiff.scripts.parser_file import parser_file


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


if __name__ == '__main__':
    main()
