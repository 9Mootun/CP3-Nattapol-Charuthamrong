import tkinter as tk
from tkinter import ttk
from forex_python.converter import CurrencyRates
from tkinter import messagebox
import datetime
c = CurrencyRates()
convert_result = 0
x = datetime.datetime.now()

def leftClickButton(event):
    if combo1.get() == "USD" :
        convert_result = float(amountinput.get()) * c.get_rate('USD','THB')
        Labeloutput.configure(text = convert_result)
    elif combo1.get() == "JPY" :
        convert_result = float(amountinput.get()) * c.get_rate('JPY','THB')
        Labeloutput.configure(text=convert_result)
    elif combo1.get() == "EUR" :
        convert_result = float(amountinput.get()) * c.get_rate('EUR','THB')
        Labeloutput.configure(text=convert_result)
    elif combo1.get() == "SGD" :
        convert_result = float(amountinput.get()) * c.get_rate('SGD','THB')
        Labeloutput.configure(text=convert_result)


app = tk.Tk()
app.geometry('400x200')
app.title("Foreign Currency Converter")

#image arrow1&2
img = tk.PhotoImage(file = r"C:\Users\nattapol.ch\Downloads\arrow.png")
img1 = img.subsample(2, 2)
img2 = tk.Label(app,image=img1)
img2.grid(column = 1 , row = 1,padx = 1)
img3 = tk.Label(app, image=img1)
img3.grid(column = 1 , row = 3,padx = 1)
#Label 1&2&3
labelTop = tk.Label(app,
                    text="Currency I Have")
labelTop.grid(column=0, row=0)

labelTop1 = tk.Label(app,
                    text="Currency I Want")
labelTop1.grid(column=2, row=0)
label_thb = tk.Label(app, text = "THB")
label_thb.grid(column=2, row=1,columnspan = 1,padx = 10)

Labeloutput = tk.Label(app, text ="Amount output")
Labeloutput.grid(column = 2, row = 3, pady = 5, columnspan = 1)

#Combobox 1&2
combo1 = ttk.Combobox(app,
                            values=[
                                "USD",
                                "JPY",
                                "EUR",
                                "SGD"])

combo1.grid(column=0, row=1, columnspan = 1,padx = 10)
combo1.current(1)


#Entry1
amountinput = tk.Entry(app)
amountinput.grid(column = 0, row = 3,columnspan = 1,pady = 5)

#Button1
calculateButton = tk.Button(app,text = "Convert")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=4,column=0,rowspan = 1, columnspan = 1)
app.mainloop()

