# keyword arguments

# def names(name1='taofiq', name2):
#     print(f"The first name is {name1.title()}")
#     print(f"The second name is {name2.title()}")


# names(name1="taofiq", name2="Fathiat")


# def formated_name(first_name, last_name, middle_name=''):
#     if middle_name:
#         full_name = f"{first_name.title()} {middle_name.title()} {last_name.title()}"
#     else:
#         full_name = f"{first_name.title()} {last_name.title()}"

#     return full_name


# name = "taofiq"
# name2 = "adeola"
# name3 = "bakare"

# full_name = formated_name(name, name3)
# print(full_name)


# a function that returns a dictionary

def user_info(first_name, last_name, age=None):
    info = {
        'First name': first_name.title(),
        'Last name': last_name.title(),
    }

    if age:
        info['Age'] = age

    return info


answer = user_info('Taofiq', 'Bakare', age=20)
print(f"The user info is: {answer}")
