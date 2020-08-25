from tkinter import *
root = Tk()

def clicked(val):
    myLabel = Label(root, text=val)
    myLabel.pack()  

"""
Radio buttons are used to select only 1 option from multiple
options. Here a variable r is declared with value 1 to keep
track of the selected option. 
"""
pizza = StringVar()
pizza.set("Cheese")
"""
You can do this manually by adding options:
r = IntVar()
Radiobutton(root,text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).grid(row=0,column=0)
Radiobutton(root,text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).grid(row=1,column=0)
"""
MODES = [
    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion"),
    ("Capsicum","Capsicum")
]

for text, mode in MODES:
    Radiobutton(root,text=text, variable=pizza, value=mode, command=lambda: clicked(pizza.get())).pack(anchor=W)

root.mainloop()