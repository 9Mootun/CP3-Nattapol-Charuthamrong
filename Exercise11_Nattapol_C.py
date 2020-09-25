pyramid = int(input("Enter your pyramid floor : "))
text = ""
runnum = pyramid
for x in range(pyramid):
    runnum = runnum - 1
    print(" " * runnum + "*" * (2*x+1))

