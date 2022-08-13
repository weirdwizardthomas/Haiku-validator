import os
import argparse

from haiku_validator.haiku_validation import get_haiku


def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)

    with open(arg, 'r') as file:
        return file.read()


def get_arguments():
    parser = argparse.ArgumentParser()

    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument('-f', '--file', dest='text', type=lambda x: is_valid_file(parser, x),
                             help='File to check for haiku.')
    input_group.add_argument('-t', '--text', type=str, help='Plain text to check for haiku.')

    return parser.parse_args()


if __name__ == '__main__':
    arguments = get_arguments()

    haiku = get_haiku(arguments.text)

    if haiku:
        print(haiku)
    else:
        print('No haiku detected.')
