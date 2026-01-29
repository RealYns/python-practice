active = True

while active:
    prompt = input("What's your name: \n")
    print("Press q to leave.\n")
    if prompt == 'q':
        active = False
    else:
        print("Greeting, " + prompt.title())
        filename = 'guest_book.txt'
        with open(filename, 'a') as file_object:
            file_object.write(prompt.title() + " just visited\n")
