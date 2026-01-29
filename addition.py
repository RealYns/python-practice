print("Enter 2 numbers and i will perform addition:\n")
print("Enter q to leave.\n")

while True:
    first_num = input("Enter first number: ")
    if first_num == 'q':
        break

    second_num = input("Enter second number: ")
    if second_num == 'q':
        break

    try:
        total = int(first_num) + int(second_num)
        print("This is the sum: " + str(total))
    except ValueError:
        print("Please enter numbers")