pizza_toppings = []
done = False
while not done:
    pizzaTopping = input("Enter a topping (Enter quit to stop): ")
    if pizzaTopping == 'quit':
        done = True
    else:
        pizza_toppings.append(pizzaTopping)

print("Your toppings are: ")
for topping in pizza_toppings:
    print(topping)