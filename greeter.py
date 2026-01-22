def get_formatted_name(first_name, last_name):

 full_name = first_name + ' ' + last_name
 return full_name

while True:
    print("\nPlease tell us your name:")
    print("\nQ to quit")
    f_name = input("First name: ")
    if f_name == 'Q':
        break
    l_name = input("Last name: ")
    if l_name == 'Q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")