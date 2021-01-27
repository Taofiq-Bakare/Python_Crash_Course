

# alien_0 = {'color': 'green', 'points': '5'}


# # add new elements to the dictionary

# alien_0['x_axis'] = 0
# alien_0['y_axis'] = 25
# alien_0['speed'] = 'medium'

# print(f"The new dictionary is {alien_0}")
# # print the new dicitionary

# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3

# alien_0['x_axis'] = alien_0['x_axis'] + x_increment

# print(f"The new position is {alien_0['x_axis']}")

# A dictionary of similar objects

# favorite_language = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phill': 'python',
# }


# for name, language in favorite_language.items():
#     print(f"\n{name.title()}'s favorite language is {language} ")


people = [
    {'daniel': 'black'},
    {'sam': 'pink'},
    {'sindel': 'white'}
]

for name in people:
    print(f"{name.keys()} has {name.values()}")
    # print(name.keys())
