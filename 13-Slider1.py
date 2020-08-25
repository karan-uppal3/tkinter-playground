from tkinter import *

root = Tk()

def slide():
    Label(root,text=horizontal.get()).pack()
    Label(root,text=vertical.get()).pack()
    root.geometry(str(horizontal.get())+"x"+str(vertical.get()))


vertical = Scale(root, from_=200 , to=400)
vertical.pack()

horizontal = Scale(root, from_=200, to=400, orient=HORIZONTAL)
horizontal.pack()


Button(root,text="Click me!", command=slide).pack()

root.mainloop()