
favorite_language = {
    'jen' : 'c' ,
    'jonas' : 'python' ,
    'aliyah' : 'c++' ,
    'edward' : 'python' ,
}

friends = ['jonas', 'aliyah']

for name in favorite_language.keys():
    print(name.title())
    if name in friends:
        print("Hello " + name.title() + ", I see that your favorite language is " + favorite_language[name].title() + "!")

if 'erin' not in favorite_language.keys():
    print("Erin, please take a vote.")

for name in favorite_language.keys():
    print(name.title() + ", Thank you for taking the poll.")

print("The following languages have been mentioned.")

for language in set(favorite_language.values()): #set() so we won't print the same word twice
    print(language.title())