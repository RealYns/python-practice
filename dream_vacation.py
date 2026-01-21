responses = {}

poll = True

while poll:
    name = input("\nWhat's your name: ")
    response = input("\nWhich place do you wanna visit: ")

    responses[name] = response

    repeat = input("Would you like to let the next person take the poll:")

    if repeat == 'no':
        poll = False

print("\nList of names and the place they wanna visit")
for name, response in responses.items():
    print(name.title() + ": " + response.title())