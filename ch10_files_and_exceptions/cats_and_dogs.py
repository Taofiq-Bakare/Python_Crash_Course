"""
A program to read texts from file
"""


def read_lines(paths):
    """ A function to read line"""
    try:
        with open(paths, encoding='utf-8') as f:
            content = f.readlines()
    except FileNotFoundError:
        print(f"File {paths} does not exists")
        # pass
    else:
        for line in content:
            print(f"{line.title().rstrip()}")


example = 'ch10_files_and_exceptions\cats.txts'
file_names = ['ch10_files_and_exceptions\cats.txt',
              'ch10_files_and_exceptions\cats.txts',
              'ch10_files_and_exceptions\dog.txt', ]

for book in file_names:
    read_lines(book)
