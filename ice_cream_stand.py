from restaurant import Restaurant


class IceCreamStand(Restaurant):
    def __init__(self, stand_name, icecream_type):
        super().__init__(stand_name, icecream_type)
        self.flavour = ['chocolate', 'vanilla', 'bubblegum', 'lemon']

    def show_flavour(self):

        print("Flavours: ")
        for flavour in self.flavour:
            print(flavour.title())

stand_0 = IceCreamStand('Ice Cream Guy', 'Cone')
stand_0.show_flavour()
stand_0.describe_restaurant()