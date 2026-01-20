cities = {
    'safi' : {
        'country' : 'morocco' ,
        'population' : 308508 ,
        'fun fact' : 'It has a world class beach for surfing.'
    } ,
    'casablanca' : {
        'country' : 'morocco' ,
        'population' : 3200000 ,
        'fun fact' : 'Largest city in morocco.'
    } ,
    'new york' : {
        'country' : 'united states of america' ,
        'population' : 20000000 ,
        'fun fact' : 'Largest city in USA.'
    } ,

}

for name, city_info in cities.items():
    print("\n" +name.title() + ":")

    print("\t" + city_info['country'].title())
    print("\t" + str(city_info['population']))
    print("\t" + city_info['fun fact'].title())