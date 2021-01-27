"""
A program to dump load json file
"""
import json


def write_username():
    """
    A function to dump username in a json file
    """
    username = input("What is your name? ")
    file_path = 'username.json'
    with open(file_path, 'w') as f:
        json.dump(username, f)
    return username


def load_username(file_path):
    """
    A function to load user's name from
    json file
    """
    file_path = 'username.json'
    with open(file_path) as f:
        name = json.load(f)
        return name

        # print(f"Welcome back {name}")


def append_username(file_path, name):
    with open(file_path, 'a') as f:
        f.write(name.title())
        f.write("\n")


file = 'username.json'

try:
    name = load_username(file)
except FileNotFoundError:
    username = input("What is your name? ")
    write_username(file, username)
else:
    print(f"Welcome back {name}")


# load_username(file)
