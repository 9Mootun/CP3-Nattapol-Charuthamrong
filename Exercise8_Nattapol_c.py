username = "customer"
password = 12345
print("--------------------------------------------------------")
print("************** Welcome to Tony's Minimart **************")
print("--------------------------------------------------------")
print("     Item             Product List                 Price")
print("       1              Soda                          15  ")
print("       2              Beer                          60  ")
print("       3              Soft drink                    25  ")
print("--------------------------------------------------------")
orderinput = int(input("Please Select your Order : "))
if orderinput == 1:
    quantityinput1 = int(input("Please enter Quantity : "))
    if quantityinput1 >= 0:
        print(">>> Price Summary =", 15 * quantityinput1, "THB")
elif orderinput == 2:
    quantityinput2 = int(input("Please enter Quantity : "))
    if quantityinput2 >= 0:
        print(">>> Price Summary =", 60 * quantityinput2, "THB")
elif orderinput == 3:
    quantityinput3 = int(input("Please enter Quantity : "))
    if quantityinput3 >= 0:
        print(">>> Price Summary =", 25 * quantityinput3, "THB")
else:print("---------------- Invalid Item --------------------------")
