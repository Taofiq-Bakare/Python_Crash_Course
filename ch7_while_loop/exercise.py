# deli

sandwich_orders = [
    'tuna sandwich',
    'pastrami',
    'peanut butter sandwich',
    'jam sandwich',
    'pastrami',
    'honey sandwich',
    'pastrami',
]

finished_sandwiches = []

# remove the pastramis from the list

while 'pastramis' in sandwich_orders:
    sandwich_orders.remove('pastramis')

# notify user that there is no more pastramis
# and if they want to make another order

flag = True
prompt = "There is no more pastramis"
prompt += "\n Enter 'yes' to continue with your order: "

while flag:
    response = input(prompt)
    if response == 'yes':
        print('Thanks, and we shall proceed with your order now')
        flag = False

while sandwich_orders:
    finished = sandwich_orders.pop()
    finished_sandwiches.append(finished)
    print(f" I made you {finished.title()}")
print('')
print('I made the following sandwiches: \n')
for made in finished_sandwiches:
    print(f"{made.title()}")
