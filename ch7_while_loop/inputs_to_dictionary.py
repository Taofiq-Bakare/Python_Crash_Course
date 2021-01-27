# the program takes in the user's name and response
# and store them as the key and value into a dictionary

# create an empty dictionary

name_mountain = {}

# instantiate the flag
# and constants

flag = True
name_prompt = "What is your name? "
mountain_prompt = "Which mountain would like to climb? "

# instantiate the loop

while flag:
    name = input(name_prompt)
    mountain = input(mountain_prompt)

    name_mountain[name] = mountain

    # find out if there is anyone else interested in the polls
    question = input("would anyone else like to take the poll? ")
    if question == 'no':
        flag = False

for name, mountain in name_mountain.items():
    print(f"{name.title()} would like to climb mountain {mountain}")
