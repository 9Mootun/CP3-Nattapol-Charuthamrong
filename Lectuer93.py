from tkinter import *

def sayHelloWorld():
    print("Hello World !!!")

mainwindow = Tk()
button = Button(mainwindow,text = "Clcik me",command = sayHelloWorld)
button.place(x = 60, y = 20)
mainloop()

mainwindow2 = Tk()
button2 = Button(mainwindow2,text = "Clcik me",command = sayHelloWorld)
button2.place(x = 60, y = 20)
mainloop()