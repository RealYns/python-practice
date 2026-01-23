def greet_user(names):
    for name in names:
        msg = "Greeting, " + name.title() + "!"
        print(msg)

usernames = ['john', 'alucard', 'seras']
greet_user(usernames)