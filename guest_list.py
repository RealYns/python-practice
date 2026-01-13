people = ['kurt cobain', 'adolf hitler', 'hmmm idk']

message = "I invite " + people[0].title() + "!"

print(message)

message = "I invite " + people[-2].title() + " (just joking haha!!)."

print(message)

message = "I invite.... " + people[-1] +  "??"

print(message)

removed = people.pop(1).title()

print(removed + " can't make it (fortunately!).")

people.insert(1, 'joseph staline')

message = "I invite " + people[0].title() + "!"

print(message)

message = "I invite " + people[-2].title() + " (for fuck sake)."

print(message)

message = "I invite.... " + people[-1] +  "??"

print(message)

people.insert(0, 'dummy 1')

people.insert(2, 'dummy 2')

people.append('dummy 3')

print(people)

message = "I invite " + people[0].title() + "!"

print(message)

message = "I invite " + people[1].title() + " (just joking haha!!)."

print(message)

message = "I invite.... " + people[2] +  "??"

print(message)

message = "I invite " + people[3].title() + "!"

print(message)

message = "I invite " + people[4].title() + " (just joking haha!!)."

print(message)

message = "I invite.... " + people[5] +  "??"

print(message)

print("I can only invite 2 people")

kicked = people.pop()

print("Bye bye " + kicked.title())

kicked = people.pop()

print("Bye bye " + kicked.title())

kicked = people.pop()

print("Bye bye " + kicked.title())

kicked = people.pop()

print("Bye bye " + kicked.title())

print(people[0].title() + ' and ' + people[1].title() + ', you are still invited to dinner!!')

del people[0]



print(people)

print(len(people))











