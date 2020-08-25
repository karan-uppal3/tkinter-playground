from tkinter import *

root = Tk()

var = StringVar()

def onClick():
    myLabel = Label(root, text=var.get()).pack()

c = Checkbutton(root, text="Option 1", variable=var, onvalue="On",offvalue="Off",command=onClick)
c.deselect()
c.pack()

root.mainloop()