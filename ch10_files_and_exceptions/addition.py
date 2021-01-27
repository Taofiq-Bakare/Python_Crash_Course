"""
A simple program to catch non-integer input
"""


while True:
    print("Enter 'q' to quit the program")
    number_1 = input("Enter the first number ")
    if number_1 == 'q':
        break

    number_2 = input("Enter the second number ")
    if number_2 == 'q':
        break
    try:
        answer = int(number_1) + int(number_2)
    except ValueError:
        print("Please enter a numerical value")
    else:
        print(f"The answer is {answer}")
