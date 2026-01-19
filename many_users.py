users = {
    'eminence' : {
        'first_name' : 'John' ,
        'last_name' : 'Smith' ,
        'location' : 'Train?' ,
    } ,
    'alucard' : {
        'first_name' : 'Dracula' ,
        'last_name' : 'The impaler' ,
        'location' : 'London' ,
    } ,
}

for username, user_info in users.items():
    print("\nUsername: " + username.title())
    full_name = user_info['first_name'] + " " + user_info['last_name']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())