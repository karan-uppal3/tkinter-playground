from tkinter import *
root = Tk()

"""
Frame puts a box with some border into the window
"""
frame = LabelFrame(root,text="This is my frame...", padx=50,pady=50)
frame.pack(padx=100,pady=100)

b = Button(frame, text="Don't click! ")
b.grid(row=0,column=0)

b2 = Button(frame, text="Don't click me too! ")
b2.grid(row=1,column=1)

root.mainloop()