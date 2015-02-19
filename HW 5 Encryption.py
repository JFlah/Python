# John M Flaherty HW 5 Encryption

from Tkinter import *

root = Tk()
root.title("Encryption")

ordered   = "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(),.<>;:[{]}'\""
scrambled = "y});4%vb79PTBX<]n:M{.rN8*udtc(RWGeDA&kQm3@U^,Cfa#5HYEjI>6[2q iZJVxg\"FKlp0S1$LzhsO!w'o"

def encrypt():
    result = ""
    myString = messageEntry.get()
    for index in range(len(myString)):
        for k in range(len(ordered)):
            if myString[index]==ordered[k]:
                result += scrambled[k]          
    messageEntry.delete(0,END)
    messageEntry.insert(0, result)

def decrypt():
    result = ""
    myString = messageEntry.get()
    for index in range(len(myString)):
        for k in range(len(scrambled)):
            if myString[index]==scrambled[k]:
                result += ordered[k]          
    messageEntry.delete(0,END)
    messageEntry.insert(0, result)

def clear():
    messageEntry.delete(0, END)

encryptButton = Button(root, text="Encrypt", command=encrypt)
encryptButton.grid(row=0,column=0)

decryptButton = Button(root, text="Decrypt", command=decrypt)
decryptButton.grid(row=0,column=1)

clearButton = Button(root, text="Clear", command=clear)
clearButton.grid(row=0,column=2)

messageEntry = Entry(root)
messageEntry.grid(row=1, column=0, columnspan=3, sticky="WE")

root.mainloop()
    
