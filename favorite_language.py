
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

language_poll = ['jen', 'jonas', 'aliyah', 'alex', 'jack']

for poll in language_poll:
    if poll in favorite_language.keys():
        print("\nThank you for voting, " + poll.title())
    else:
        print("\nYou still haven't voted, " + poll.title())

favorite_language = {
    'jen' : ['c', 'rust'] ,
    'jonas' : ['python', 'php'] ,
    'aliyah' : ['c++', 'java'] ,
    'edward' : ['python', 'c'] ,
}

for name, languages in favorite_language.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())
