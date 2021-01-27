# a list is collection of items in a particular order
# you can print a list out at once in python

# empty list

cars = []

# filled list
# movies = ['RED', 'Die Hard', 'Avengers', 'Taken']
# print(movies)
# for i in range(0, len(movies)):
#     print(f'The title of the movie is :{movies[i].upper()}')

# change element of a list
# movies[0] = 'Terminator'
# print(movies)

# append to a list
# movies.append('Rambo')
# print(movies)

count = 0
while True:
    print("Enter a car manufacturer")
    car = input().title()
    cars.append(car)
    count += 1
    if count >= 5:
        break

for i in range(0, len(cars)):
    print(f"The {i} car is {cars[i]}")

# print(cars)

# you can remove an element with either del() or pop() method
# use pop() to store the removed item in another label
# you can also call the remove()
# method if the index of the element is not known
