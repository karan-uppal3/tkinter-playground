from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root,text="Yay! You clicked a button")
    myLabel.pack()

"""
A button like everything is a widget and is created
as follows:
"""

myButton = Button(root,text="Press me",padx=50,pady=50,command=myClick,fg="blue",bg="red")  
# state = DISABLED makes the button unable to be clicked
# padx = 50 adds padding in horizontal direction, we can do same with pady
# command = <function_name> executes the function on click
# fg and bg are foreground and background colors

myButton.pack()

root.mainloop()