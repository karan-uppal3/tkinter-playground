from tkinter import *

root = Tk()

def slide(var):
    Label(root,text=horizontal.get()).pack()
    Label(root,text=vertical.get()).pack()
    root.geometry(str(horizontal.get())+"x"+str(vertical.get()))


vertical = Scale(root, from_=200 , to=400, command=slide)
vertical.pack()

horizontal = Scale(root, from_=200, to=400, orient=HORIZONTAL, command=slide)
horizontal.pack()

root.mainloop()