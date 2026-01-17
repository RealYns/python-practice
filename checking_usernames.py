current_users = ['John', 'esdeath', 'alucard', 'OKOMGYESGOOD', 'coolgamer32']

new_users = ['alucard', 'JOHN', 'HMMYES', 'HUMONGUSNOOBUSAMONGUS', '95ny']

lower_current = [item.lower() for item in current_users]

for new_user in new_users:
    if new_user.lower() in lower_current:
        print("Enter a new username.")
    else:
        print("This username is available")