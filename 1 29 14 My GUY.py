# Bank account GUI 1/29/14

from Tkinter import *

root = Tk()
root.title("Bank Account")

def addMoney():
    amount = float(amountEntry.get())
    balance = float(balanceEntry.get())
    newBalance = amount + balance
    balanceEntry.delete(0, END)
    balanceEntry.insert(0, newBalance)

def subMoney():
    amount = float(amountEntry.get())
    balance = float(balanceEntry.get())
    newBalance = balance - amount
    balanceEntry.delete(0, END)
    balanceEntry.insert(0, newBalance)

depositButton = Button(root, text="Deposit", command=addMoney)
depositButton.grid(row=0, column=0)

amountEntry = Entry(root)
amountEntry.grid(row=0, column=1)
amountEntry.insert(0, "0.00")

withdrawButton = Button(root, text="Withdraw", command = subMoney)
withdrawButton.grid(row=0, column=2)

balanceButton = Label(root, text="Balance:")
balanceButton.grid(row=1, column=0)

balanceEntry = Entry(root)
balanceEntry.grid(row=1, column=1, columnspan=2, sticky="WE") #spans two columns
balanceEntry.insert(0, "0.00")

# Sticky uses N,E,S,W to show how far to each direction you 'stick' it

# To change an Entry: balanaceEntry.insert(0, thetext) 0 inserts at pos 0
# usually first: balanceEntry.delete(0,END) deletes everything 0 to end

root.mainloop()





