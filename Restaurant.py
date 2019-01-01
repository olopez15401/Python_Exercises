class Restaurant():

    def __init__(self,name,cuisine_type):
        self.restaurant_name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name)
        print("Food type: " + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name + " is now open!")

    def set_number_served(self,number_served):
        self.number_served = number_served

    def increment_number_served(self, number_served):
        self.number_served += number_served

"""
outback = Restaurant('Outback','Casual dining')
outback.describe_restaurant()
outback.open_restaurant()
outback.increment_number_served(10)
print(str(outback.number_served))
"""