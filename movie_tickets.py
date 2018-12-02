def chargeTicket(age):
    price = 15
    if age < 3:
        price = 0 #free
    if age >= 3 and age < 12:
        price = 10
    return price

def main():
    print(chargeTicket(2))
    print(chargeTicket(5))
    print(chargeTicket(29))

main()