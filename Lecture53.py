def vatcalculate(price):
    result = price+ (price * 7 / 100)
    return result
print(vatcalculate(int(input("Enter price : "))))