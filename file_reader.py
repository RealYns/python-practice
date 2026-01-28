filename = 'learning_python.txt'
count = 0
while count < 3:
    with open(filename) as file_object:
        contents =file_object.read()
        print(contents.rstrip())
    count += 1
print("\n")
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
print("\n")
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.strip())
print("\n")
with open(filename) as file_object:
    contents = file_object.read()
    contents = contents.replace('python', 'c')

    print(contents.rstrip())