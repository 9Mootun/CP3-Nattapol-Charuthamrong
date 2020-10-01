from tkinter import *

def sayHelloWorld():
    print("Hello World !!!")

mainwindow = Tk()
button = Button(mainwindow,text = "Clcik me",command = sayHelloWorld).grid(row=0,column=1)

button2 = Button(mainwindow,text = "Clcik me",command = sayHelloWorld).grid(row=1,column=1)

mainloop()

