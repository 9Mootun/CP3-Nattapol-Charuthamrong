from tkinter import *
import math

bmiresult = 0

def leftClickButton(event):
    bmiresult = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    if bmiresult < 18.5 :
        labelResult.configure(text="น้ำหนักต่ำกว่าเกณฑ์")
    elif bmiresult >= 18.6 and bmiresult < 23:
        labelResult.configure(text="น้ำหนักปกติ เหมาะสม")
    elif bmiresult >= 23 and bmiresult < 25:
        labelResult.configure(text="น้ำหนักเกิน")
    elif bmiresult >= 25 and bmiresult < 30:
        labelResult.configure(text="อ้วน")
    elif bmiresult >= 30:
        labelResult.configure(text="อ้วนมาก")

MainWindow = Tk()
labelHeight = Label(MainWindow, text="ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)

labelWeigth = Label(MainWindow, text="น้ำหนัก (Kg.)")
labelWeigth.grid(row=1,column=0)

textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)

textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)

calculateButton = Button(MainWindow,text = "คำนวน")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2,column=0)

labelResult = Label(MainWindow,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)


MainWindow.mainloop()