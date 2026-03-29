# Practical 08, Lab Assignment 1
# Read one text file and write its contents into another text file in uppercase.

import os


def copy_file_to_uppercase(source_path, destination_path):
    if not os.path.isfile(source_path):
        print(f"Source file not found: {source_path}")
        return

    with open(source_path, 'r', encoding='utf-8') as source_file:
        content = source_file.read()

    with open(destination_path, 'w', encoding='utf-8') as destination_file:
        destination_file.write(content.upper())

    print(f"Contents of '{source_path}' were copied to '{destination_path}' in uppercase.")


if __name__ == '__main__':
    source = input('Enter the source text file name: ').strip()
    destination = input('Enter the destination text file name: ').strip()

    copy_file_to_uppercase(source, destination)
