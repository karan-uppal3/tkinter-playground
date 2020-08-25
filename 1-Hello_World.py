from tkinter import *

"""
Here everything is a widget, similar to GTK
The main widget that should always be created is called root
"""

root = Tk()

# This adds a title to the window
root.title("Hello")

myLabel = Label(root,text="Hello World!") # creating a label widget

"""
Now we want to put the label into the main window
"""

myLabel.pack() # pack the widget into the window depending on its size

"""
Now we will need to create an event loop so as to detect mouse
and keyboard events and also make the window stay
"""

root.mainloop()