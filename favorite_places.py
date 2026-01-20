favorite_places = {
    'aliyah' : ['new york', 'morocco', 'bali'] ,
    'jonathan' : ['germany', 'paris', 'hawaii'] ,
    'alexander' : ['london', 'russia', 'alaska'] ,
}

print("Can you name me your favorite places?")

for name, fav in favorite_places.items():
    print("\n" + name.title() + ":")
    for place in fav:
        print(place)