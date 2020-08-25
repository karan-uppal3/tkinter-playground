from tkinter import *

root = Tk()

# creating input field
e = Entry(root,width=50,bg="blue",fg="white",borderwidth=5)
e.pack()

# This puts default text into your box
e.insert(0,"Enter your name")

"""
e.get() will return the text that is written in the input field
"""

def myClick():
    myLabel = Label(root,text="Hello "+e.get())
    myLabel.pack()

myButton = Button(root,text="Enter your name",command=myClick)

myButton.pack()

root.mainloop()