from Tkinter import *
from FractionClass import *

root = Tk()
root.title("Fraction Calculator")

def add():
    fraction1,fraction2 = getFractions()
    result    = fraction1.add(fraction2)
    insertResult(result)
    
def subtract():
    fraction1,fraction2 = getFractions()
    result    = fraction1.sub(fraction2)
    insertResult(result)
    
def multiply():
    fraction1,fraction2 = getFractions()
    result    = fraction1.mul(fraction2)
    insertResult(result)
    
def divide():
    fraction1,fraction2 = getFractions()
    result    = fraction1.div(fraction2)
    insertResult(result)

def getFractions():
    fraction1 = Fraction(int(numEntry1.get()),int(denEntry1.get()))
    fraction2 = Fraction(int(numEntry2.get()),int(denEntry2.get()))
    return fraction1,fraction2

def insertResult(solution):
    numEntry3.delete(0,END)
    denEntry3.delete(0,END)
    numEntry3.insert(0,solution.numerator)
    denEntry3.insert(0,solution.denominator)

numEntry1 = Entry(root, width=5, justify=RIGHT)
numEntry1.grid(row=1, column=1, sticky="E")
denEntry1 = Entry(root, width=5, justify=LEFT )
denEntry1.grid(row=1, column=3, sticky="W")
numEntry2 = Entry(root, width=5, justify=RIGHT)
numEntry2.grid(row=2, column=1, sticky="E")
denEntry2 = Entry(root, width=5, justify=LEFT )
denEntry2.grid(row=2, column=3, sticky="W")
numEntry3 = Entry(root, width=5, justify=RIGHT)
numEntry3.grid(row=4, column=1, sticky="E")
denEntry3 = Entry(root, width=5, justify=LEFT )
denEntry3.grid(row=4, column=3, sticky="W")

Label(root, text="Fraction Calculator"        ).grid(row=0,column=1,sticky="WE",columnspan=3)
Label(root, text="___________________________").grid(row=3,column=0,sticky="WE",columnspan=5)

Label(root, text="/").grid(row=1,column=2)
Label(root, text="/").grid(row=2,column=2)
Label(root, text="/").grid(row=4,column=2)

Button(root, text="Add",      command=add     ).grid(row=1, column=5, sticky="EW")
Button(root, text="Subtract", command=subtract).grid(row=2, column=5, sticky="EW")
Button(root, text="Multiply", command=multiply).grid(row=3, column=5, sticky="EW")
Button(root, text="Divide",   command=divide  ).grid(row=4, column=5, sticky="EW")

root.mainloop()
