person = 2

if person < 2:
    print("This person is a baby.")
elif person == 2 or person < 4:
    print("This person is a toddler.")
elif person == 4 or person < 13:
    print("This person is a kid.")
elif person == 13 or person < 20:
    print("This person is a teenager.")
elif person == 20 or person < 65:
    print("This person is an adult.")
elif person >= 65:
    print("This person is an elder.")
else:
    print("Invalid.")