prompt = "\nEnter toppings.\nEnter quit.\n"

while True:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print(message.title() + " has been added to your pizza!")