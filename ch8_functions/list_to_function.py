# pass a list to a function


# create a function that prompts the user
# it prints and remove the current job
# the jon is then appended to the completed task

def print_task(unprinted_designs, completed_designs):

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_designs.append(current_design)

# create a function that summarizes the completed models


def completed_models(completed_designs):
    """ Show printed models"""
    print("\n The following models have been printed:")
    for completed_model in completed_designs:
        print(completed_model)


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_designs = []

print_task(unprinted_designs, completed_designs)
completed_models(completed_designs)
