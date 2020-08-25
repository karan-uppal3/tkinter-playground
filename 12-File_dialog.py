from tkinter import *
from tkinter import filedialog
root = Tk()

def openfiles():
    root.filename = filedialog.askopenfilename(initialdir=".",title="Select a file", filetypes=(('png files','*.png'),('jpg files','*.jpg')) )
    Label(root,text=root.filename).pack()

Button(root,text="Open File",command=openfiles).pack()

root.mainloop()