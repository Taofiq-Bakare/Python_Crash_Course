# Write a program that polls users about their dream vacation.
# Write a prompt similar to If you could visit one place in the world,
#  where would you go?
# Include a block of code that prints the results of the poll.

# create and empty dictionary
# to store the name and response of the respondent

response = {}


# create a loop to ask input of respondents
# and ask if there are other interested in the poll

name_prompt = "What is your name? "
location_prompt = "If you could visit anywhere in the world "
location_prompt += "\nwhere would it be? "

while True:
    name = input(name_prompt)
    location = input(location_prompt)

    response[name.title()] = location.title()

    others = input("Anyone else interested in the polls? ")
    if others == 'no':
        break
print("")

for name, location in response.items():
    print(f"{name.title()}'s dream vacation spot is {location.title()}")
