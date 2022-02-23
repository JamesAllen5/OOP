import CellphoneClass as cc


def main():

    man = "Apple"
    mod = "iPhone X"
    retail = 300

    phone = cc.CellPhone(man, mod, retail)

    print("Here is the datat that you entered:")
    print("Manufacturer:", phone.get_manufact())
    print("Model number:", phone.get_model())
    print("Retail price:", phone.get_retail_price())

    phone.set__manufact()
    phone.set__model()
    phone.set__retail_price()

    print("The manufacturer of the phone is now: ", phone.get__manufact())
    print("The retail number of the phone is now: ", phone.get__model())
    print("The retail price of the phone is now: ", phone.get__retail_price)

    print(phone)


main()
