prompt = "\nEnter the name of a city that you visited.\nEnter quit when you are finished.\n"



while True:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print("I'd love to go to " + message.title())