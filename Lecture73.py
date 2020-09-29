systemmenu = {"ข้าวไก่ทอด":40,"ข้าวหมูทอด":34,"ข้าวปลาทอด":45}
menuList = []
def showBill():
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1])

while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName, systemmenu[menuName]])

def totalprice():
    total = 0
    i = 0
    for i in range(len(menuList)):
        total += menuList[i][1]
    print("Total Price (THB) =",total)


showBill()
totalprice()

