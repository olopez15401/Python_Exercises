class Restaurant():

    def __init__(self,name,cuisine_type):
        self.restaurant_name = name
        self.cuisine_type = cuisine_type

    
    def describe_restaurant(self):
        print(self.restaurant_name)
        print("Food type: " + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name + " is now open!")


outback = Restaurant('Outback','Casual dining')
outback.describe_restaurant()
outback.open_restaurant()