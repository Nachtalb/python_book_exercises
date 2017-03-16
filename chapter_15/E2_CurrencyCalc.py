from tkinter import *

window = Tk()
currency = StringVar()
money = StringVar()
exchangerate = {"gbp": 0.86758037, "usd": 1.073275}


def calculate(*args):
    global currency, money
    print(args)
    print(money.get())
    if money.get().isnumeric():
        res = float(money.get()) * exchangerate[currency.get()]
    else:
        res = "Error"
    newAmount.config(text=str(res))


help = Label(window, text="Type in the amount of money in euro, choose the new currency", height=2)
newAmount = Label(window, text="0.00", height=2)

moneyfield = Entry(window, text=money)
moneyfield.bind("<KeyRelease>", calculate)

dollar = Radiobutton(window, text="US Dollar - $", value="usd", variable=currency, command=calculate)
gbp = Radiobutton(window, text="GB Pound - £", value="gbp", variable=currency, command=calculate)
dollar.select()

help.pack()
moneyfield.pack()
dollar.pack()
gbp.pack()
newAmount.pack()

window.mainloop()