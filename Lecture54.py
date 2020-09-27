def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return showMenu()
    else:
        print("Password incorrect Please try again!!!")
        return login()

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return menuSelect()

def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        print("Please choose product before vat calculate!!!")
        priceCalculator()
    elif userSelected == 2:
        priceCalculator()
    else:
        return userSelected

def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    print("Total Price Include VAT (THB) = ", result)
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    print("Price summary (THB) = ", price1 + price2)
    return vatCalculator(price1 + price2)

login()