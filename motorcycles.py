list = ['hollow knight', 'roblox', 'league of legends']

list.insert(0, 'metal gear rising')

print(list)

del list[-2]

print(list)

list.append('dark souls')

print(list)

list_popped = list.pop()

print(list_popped)

print(list)

list_popped = list.pop(0)

message = "i didn't play " + list_popped + " for a while"

print(message)

print(list)

list.remove('league of legends')

print(list)

list.append('dark souls')

print(list)

hard_game = 'dark souls'

list.remove(hard_game)

print(list)
print(hard_game + " is too hard for me!")
