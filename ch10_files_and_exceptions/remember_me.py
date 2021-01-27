import json


def get_new_username(file):
    """
    This function gets new
    username from the user
    """
    new_name = input("What is your name? ")

    with open(file, 'w') as f:
        json.dump(new_name, f)
    return new_name


def get_stored_name(file):
    """
    this functions retrieves 
    the stored name
    """
    try:
        with open(file) as f:
            stored_name = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return stored_name


def greet_user(file):
    """
    This function checks for the username
    and displays it with a greeting.
    """
    old_name = get_stored_name(file)
    new_name = get_new_username(file)
    if old_name == new_name:
        print(f"Welcome back {old_name}")
    else:
        print(f"Hello {new_name}")


def quit(letter):
    """
    This function checks if the 
    user had already keyed in his/her name
    """
    return letter


file_path = "usernames.json"
count = 0
while True:
    count += 1
    greet_user(file_path)
    if count == 3:
        break
