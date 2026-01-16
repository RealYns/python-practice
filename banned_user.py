banned_users = ['andrew', 'carolina', 'david']
user = 'alucard'

if user in banned_users:
    print(user.title() + ", you are banned.")
else:
    print(user.title() + ", you can post a response if you wish.")