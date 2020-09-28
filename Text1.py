list1 = [10,20,30,40,50]
"""
print(type(list1[0]))
for i in range(len(list1)):
    print(type(list1[i]))
for z in list1:
    print(type(z))
for x in range(5):
    print(list1[x])
    """
numadd = int(input("Add num ="))
list1.append(numadd)
print(list1)