import argparse
from gendiff.formaters.formater_stylish import formater_stylish
from gendiff.formaters.formater_plain import formater_plain
from gendiff.formaters.formater_json import formater_json
from gendiff.scripts.parser_file import parser_file
from gendiff.scripts.build_diff import build_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', default='stylish', help='set format of output')
    args = parser.parse_args()
    print(args)
    print(generate_diff(args.first_file, args.second_file, args.format))


def generate_diff(file1, file2, format='stylish'):
    data1 = parser_file(file1)
    data2 = parser_file(file2)
    if data1 == 'Error' or data2 == 'Error':
        return print('Файла не существует')
    diff = build_diff(data1, data2)
    if format == 'stylish':
        return formater_stylish(diff)
    elif format == 'plain':
        return '\n'.join(formater_plain(diff))
    elif format == 'json':
        return formater_json(diff)
    else:
        raise ValueError('Unknown format!!!')


if __name__ == '__main__':
    main()
