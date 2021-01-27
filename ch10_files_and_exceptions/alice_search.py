"""
A program to search through 
"Alice in wonderland"
"""


def count_words(path, encoding):
    """
    A function to count the word in a document
    """
    try:
        with open(path, encoding=encoding) as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Sorry, {path} doest not exist")
    else:
        print(f"There are {len(content.split())} words in {path}")


file_paths = ['alice_in_wonderland.txt',
              'A_Tale_of_Two_Cities.txt',
              'The Importance of Being Earnest.txt',
              'Moby Dick; or The Whale.txt', ]

encoding = "utf-8"

for book in file_paths:
    count_words(book, encoding)
    # print(book)
