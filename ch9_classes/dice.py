"""
Exercise 9-13

"""
from random import randint as rd
from random import choice as ch
from typing import Counter


class Die:
    """
    A simple class to model a die
    """

    def __init__(self):
        self.sides = 6

    def roll_die(self):
        """
        a function to print random
        die cast
        """
        print(f"You rolled {rd(1, self.sides)}")


# player_1 = Die()

# """
# Print the die cast by the players
# """
# for die in range(1, 11):
#     player_1.roll_die()

lottery = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e')

winning_ticket = []
my_ticket = (1, 9, 9, 'b')
stop = False
count = 0


while winning_ticket != my_ticket:
    count += 1
    for i in range(0, 4):
        random_picks = ch(lottery)
        winning_ticket.append(random_picks)
        print(f"The program has ran {count} times")

print(f"The winner is ticket number {winning_ticket}")
# print(f"Random{rand_generated}")


# print(f"The winner of the lottery is {ticket}")
