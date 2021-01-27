# passing the asterisk allows for passing multiple
# input to a function as demonstrated below

# def sandwhich(*items):
#     for item in items:
#         print(f"- {item.title()}")


# sandwhich('bread', 'butter', 'jam', 'honey')


""" user profile"""


# def build_profile(first, last, **describe):
#     describe['first_name'] = first
#     describe['last_name'] = last
#     return describe


# user_profile = build_profile(
#     'taofiq', 'bakare', location='malaysia', field='engineering')
# print(user_profile)

""" cars"""


def make_cars(manufacturer, model_name, **car_info):
    car_info['Company'] = manufacturer
    car_info['Model'] = model_name
    return car_info


cars = make_cars('toyota', 'suv', color='black', year=int('2015'))
print(cars)
