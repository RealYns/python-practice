def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_model(completed_models):
    print("\nThese are the following models: ")
    for model in completed_models:
        print(model)

uncompleted_list = ['backpack', 'slippers', 'door']
completed_list = []

print_models(uncompleted_list[:], completed_list)

show_completed_model(completed_list)