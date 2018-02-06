###########################################
# DESCRIPTION:
# Counts the number of lines and chars in the text file
#
# Example:
# countlines.py file.txt
###########################################

from sys import argv

script, file_name = argv


def count_lines(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
        line_count = sum(1 for line in lines)
    print("Line count: ", line_count)


def count_chars(file_name):
    with open(file_name, "r") as file:
        file_data = file.read()
        char_count = sum(1 for char in file_data)
    print("Character count: ", char_count)


def count_all(file_name):
    count_lines(file_name)
    count_chars(file_name)


if __name__ == "__main__":
    count_all(file_name)
