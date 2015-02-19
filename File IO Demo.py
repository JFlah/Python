# File I/O Demo

from Tkinter import *

window = Tk()
window.title("Mini Notepad")

def read():
    try:
        fin = open(fileNameEntry.get(), "r") # r for read, must already exist
        text = fin.read()
        fin.close()
        clear()
        contentText.insert("1.0", text)
    except:
        print "Unable to read file", fileNameEntry.get()
    
def save():
    try:
        text = contentText.get("1.0", END)
        # Row 1 (first). col 0 (first)
        fout = open(fileNameEntry.get(), "w") # w for write, r for read, write to it
        fout.write(text)
        fout.close() # must close
    except:
        print "Unable to write file", fileNameEntry.get()
    
def clear():
    contentText.delete("1.0", END)

# GUI

fileNameEntry = Entry(window, justify=CENTER)
fileNameEntry.grid(row=0, column=0, sticky = "NSEW")

readButton = Button(window, text="Read", command=read)
readButton.grid(row=0, column=1, sticky = "NSEW")

saveButton = Button(window, text="Save", command=save)
saveButton.grid(row=0, column=2, sticky = "NSEW")

clearButton = Button(window, text="Clear", command=clear)
clearButton.grid(row=0, column=3, sticky = "NSEW")

contentText = Text(window, width=40, height=20)
contentText.grid(row=1, column=0, columnspan=4, sticky = "NSEW")

window.mainloop()
