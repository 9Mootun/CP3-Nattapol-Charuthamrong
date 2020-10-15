from tkinter import *
from forex_python.converter import CurrencyRates
import math

"""
bmiresult = 0

def leftClickButton(event):
    bmiresult = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    if bmiresult < 18.5 :
        labelResult.configure(text="น้ำหนักต่ำกว่าเกณฑ์")
    elif bmiresult >= 18.5 and bmiresult < 23:
        labelResult.configure(text="สมส่วน")
    elif bmiresult >= 23 and bmiresult < 25:
        labelResult.configure(text="น้ำหนักเกิน")
    elif bmiresult >= 25 and bmiresult < 30:
        labelResult.configure(text="โรคอ้วน")
    elif bmiresult >= 30:
        labelResult.configure(text="โรคอ้วนอันตราย")
"""




# create a root window.
top = Tk()
top.title("Currency Converter")

# Combobox creation
#n = tk.StringVar()
monthchoosen = Combobox(window, width=27, textvariable=n)

# Adding combobox drop down list
monthchoosen['values'] = (' January',
						  ' February',
						  ' March',
						  ' April',
						  ' May',
						  ' June',
						  ' July',
						  ' August',
						  ' September',
						  ' October',
						  ' November',
						  ' December')
monthchoosen.grid(column = 1, row = 5)
monthchoosen.current()


"""
# create listbox object
listbox = Listbox(top, height = 5,
				width = 15,
				bg = "grey",
				activestyle = 'dotbox',
				font = "Helvetica",
				fg = "yellow")

listbox1 = Listbox(top, height = 5,
				width = 15,
				bg = "grey",
				activestyle = 'dotbox',
				font = "Helvetica",
				fg = "yellow")
"""
# Define the size of the window.
top.geometry("300x250")
"""
# Define a label for the list.
label = Label(top, text = " Currency I Have")
label1 = Label(top, text = " Currency I Want")
# insert elements by their
# index and names.
listbox.insert(1, "USD")
listbox.insert(2, "JPY")
listbox.insert(3, "THB")
listbox.insert(4, "SGD")
listbox.insert(5, "EUR")

listbox1.insert(1, "USD")
listbox1.insert(2, "JPY")
listbox1.insert(3, "THB")
listbox1.insert(4, "SGD")
listbox1.insert(5, "EUR")

# pack the widgets

label.grid(row = 1, column = 1)
label1.grid(row = 1, column = 2)
listbox.grid(row = 2, column = 1,sticky = W,columnspan = 3)
listbox1.grid(row = 2, column = 2)
"""
# Display untill User
# exits themselves.

top.mainloop()

"""
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
"""