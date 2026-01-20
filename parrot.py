prompt = "\nTell me something, and i will repeat it back at you:\nEnter 'Quit' to end the program.\n"

active = True
while active:
    message = input(prompt)

    if message == ('Quit'):
        active = False
    else:
        print(message)