from Restaurant import *

my_restaurant = Restaurant('Susheeh','Fine')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.increment_number_served(20)
print(str(my_restaurant.number_served))