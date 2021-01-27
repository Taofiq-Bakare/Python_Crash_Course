# make a list containing a series of short messages
# pass the list to a function that prints each message


""" create function that sends the message"""


def send_messages(messages, send_messages):
    while messages:
        current_message = messages.pop()
        print(f"The current message is: {current_message}")
        send_messages.append(current_message)


""" create function that prints the message"""


def show_messages(messages):
    for message in messages:
        print(message)


""" make the list and call the function"""

messages = ['call me back', 'what are you doing? ', 'what is your name? ']
sent_messages = []


send_messages(messages[:], sent_messages)
show_messages(messages)
