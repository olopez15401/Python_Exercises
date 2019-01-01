from Restaurant import Restaurant
class Ice_Cream_Stand(Restaurant):
    
    def __init__(self,name,cuisine_type='Ice Cream Stand'):
        super().__init__(name,cuisine_type)
        self.flavors = ['vanilla','chocolate','pistachio']

    def list_flavors(self):
        print("Available flavors:")
        for flavor in self.flavors:
            print(flavor)
    
my_stand = Ice_Cream_Stand("Baskin Robbins")
my_stand.describe_restaurant()
my_stand.list_flavors()