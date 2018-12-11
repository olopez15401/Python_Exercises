def make_sandwich(*ingredients):
    print("Your sandwich has the following ingredients: ")
    for ingredient in ingredients:
        print(ingredient.title())

make_sandwich('bacon','turkey','provolone','lettuce','chipotle mayo')
