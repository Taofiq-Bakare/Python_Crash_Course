import json

file_path = "fav_number.json"


def favorite_number(file):
    """
    prompts user for favorite number 
    """
    number = input("What is your favorite number? ")
    with open(file, 'w') as f:
        json.dump(number, f)
    return int(number)


def display_number(file):
    """
    Displays the user's favorite number
    """
    with open(file) as f:
        number = json.load(f)
    print(f"Your favorite number is {number}")


def check_number(file):
    """
    check if the user already entered
    favorite number
    """
    with open(file) as f:
        number = favorite_number(file)
        if json.load(f) == number:
            print(f"Your favorite number is {number}")


try:
    check_number(file_path)
except FileNotFoundError:
    pass
else:
    display_number(file_path)
