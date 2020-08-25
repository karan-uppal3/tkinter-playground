from tkinter import *

root = Tk()

myLabel1 = Label(root,text="Hello World!")
myLabel2 = Label(root,text="My name is John Doe")

"""
There is a grid system that helps you to position widgets 
"""

myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=5)

"""
The positing is relative, if there is nothing in column 1,2,3,4 and 
you put widgets in 0 and 5, it'll be the same as putting widgets in 
only 0 and 1
"""

"""
Another thing one can do is directly initialise the widget and make 
it appear on the window using:
myLabel1 = Label(root,text="Hello World!").grid(row=0,column=0)
myLabel2 = Label(root,text="My name is John Doe").grid(row=1,column=5)
"""

root.mainloop()