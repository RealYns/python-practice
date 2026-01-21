prompt = "\nWhat's your age: "

active = True

while active:
    age = int(input(prompt))
    if age < 3:
        print("Ticket's price: 0 $")
    elif age >= 3 and age <= 12:
        print("Ticket's price: 10 $")
    else:
        print("Ticket's price: 15 $")
    active = False