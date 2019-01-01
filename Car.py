def make_car(brand,model,**options):
    car = {}
    car['brand'] = brand
    car['model'] = model
    for key, value in options.items():
        car[key] = value
    return car

car = make_car('Mazda','RX-7',convertible = True, color = 'black',turbo = False)
print(car)
