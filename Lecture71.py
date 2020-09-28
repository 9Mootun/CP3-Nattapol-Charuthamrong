menuList = []
priceList = []
i = 0
def showBill():
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])
def totalprice():
    total =0
    for i in list(priceList):
        total = int(i) + total
    print("Total Price (THB) =", total)
while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()
totalprice()

