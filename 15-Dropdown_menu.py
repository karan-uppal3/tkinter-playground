from tkinter import *

root = Tk()

clicked = StringVar()
clicked.set("Monday")

def show(val):
    print(clicked.get())

options = [
    "Monday", 
    "Tuesday", 
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

drop = OptionMenu(root, clicked,*options,command=show)
drop.pack()

root.mainloop()