import Exercise2Class as e2


def main():

    man = "Apple"
    mod = "iPhone X"
    retail = 300

    phone = e2.CellPhone(man, mod, retail)

    print()

    print("The manufacturer of the phone is: ", phone.get__manufact())

    print("The retail number of the phone is: ", phone.get__model())

    print("The retail price of the phone is: ", phone.get__retail_price)

    phone.set__manufact()
    phone.set__model()
    phone.set__retail_price()

    print("The manufacturer of the phone is now: ", phone.get__manufact())

    print("The retail number of the phone is now: ", phone.get__model())

    print("The retail price of the phone is now: ", phone.get__retail_price)


main()
