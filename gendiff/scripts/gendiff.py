import argparse


parser = argparse.ArgumentParser(description = 'Compares two configuration files and shows a difference.')
parser.add_argument('first_file')
parser.add_argument('second_file')
print(parser.parse_args())