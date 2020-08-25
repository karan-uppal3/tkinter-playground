from tkinter import *
root = Tk()

# This is how you can have an exit button
button_quit = Button(root,text="Exit Program",command=root.quit)
button_quit.pack()

root.mainloop()