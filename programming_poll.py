active = True

while active:
    print("Press q to leave.")
    prompt = input("Why do you line programming?\n")
    if prompt == 'q':
        active = False
    else:
        print("Not bad for a reason huh.")
        filename = 'responses.txt'
        with open(filename, 'a') as file_object:
            file_object.write(prompt.title() + "\n")