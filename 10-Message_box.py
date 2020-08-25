from tkinter import *
from tkinter import messagebox
root = Tk()

# showinfo , showwarning , showerror , askquestion , askokcancel , askyesno

def popup():
    response = messagebox.askyesno("This is my Popup!","Hello world!")
    Label(root,text=response).pack()

Button(root,text="Popup",command=popup).pack()


root.mainloop()