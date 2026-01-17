usernames = ['coolgamerboy', 'snyyyns', 'T1 OK YES GOOD', 'esdeathh', 'admin']

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Welcome back admin, Would you like to take a look at the status?")
        else:
            print("Welcome back " + username + ".")
else:
    print("The usernames list is empty.")