"""
learning to use the powerful
tryExcept

"""

print(" This simple calculator will divide two integers")
print("Enter 'q' to quit the program")

while True:
    numerator = input("Enter the numerator ")
    if numerator == 'q':
        break

    denominator = input("Enter the denominator ")
    if denominator == 'q':
        break

    try:
        ans = int(numerator) / int(denominator)
    except ZeroDivisionError:
        print("You cannot divide by zero")
    else:
        print(f"The answer is {ans}")
