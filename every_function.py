computer_parts = ['graphic card', 'processor', 'motherboard', 'ssd', 'ram']

computer_parts.sort()

print(computer_parts)

bought = computer_parts.pop()

print("i already bought " + bought + ".")

print(computer_parts)

computer_parts.append('case')

print(computer_parts)

computer_parts.sort()

print(computer_parts)

del computer_parts[3]

print(computer_parts)

print(len(computer_parts))

message = "I need to buy " + computer_parts[0].upper() + ", " + computer_parts[-3].upper() + ", " + computer_parts[2].upper() + " and " + computer_parts[3].upper() + "."

print(message)

