# Practical 08, Lab Assignment 2
# Copy the contents of a Python script into another file without comments.

import os


def copy_python_without_comments(source_path, destination_path):
    if not os.path.isfile(source_path):
        print(f"Source file not found: {source_path}")
        return

    with open(source_path, 'r', encoding='utf-8') as source_file:
        lines = source_file.readlines()

    cleaned_lines = []
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith('#'):
            continue
        if '#' in line:
            before_comment = line.split('#', 1)[0]
            if before_comment.strip():
                cleaned_lines.append(before_comment.rstrip() + '\n')
            continue
        cleaned_lines.append(line)

    with open(destination_path, 'w', encoding='utf-8') as destination_file:
        destination_file.writelines(cleaned_lines)

    print(f"Copied '{source_path}' to '{destination_path}' without comments.")
    print('\nSource file content:')
    print(''.join(lines))
    print('\nDestination file content:')
    print(''.join(cleaned_lines))


if __name__ == '__main__':
    source = input('Enter the source Python file name: ').strip()
    destination = input('Enter the destination file name: ').strip()
    copy_python_without_comments(source, destination)
