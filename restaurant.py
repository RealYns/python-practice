class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant's name is " + self.restaurant_name.title() + ", that serves " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        print("Open")

restaurant_0 = Restaurant('Urban Ember', 'Barbeque')
print(restaurant_0.restaurant_name.title())
print(restaurant_0.cuisine_type.title())

restaurant_0.describe_restaurant()
restaurant_0.open_restaurant()

restaurant_1 = Restaurant('Saffron Garden', 'Indian cuisine')
restaurant_1.describe_restaurant()

restaurant_2 = Restaurant('La Piazza Verde', 'Italian cuisine')
restaurant_2.describe_restaurant()

restaurant_3 = Restaurant('Golden Wok', 'Chinese cuisine')
restaurant_3.describe_restaurant()
