from tkinter import *
root = Tk()

from PIL import ImageTk , Image

my_img1 = ImageTk.PhotoImage(Image.open("1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("3.jpeg"))
my_img4 = ImageTk.PhotoImage(Image.open("4.jpeg"))
my_img5 = ImageTk.PhotoImage(Image.open("5.jpeg"))

imgs = [ my_img1 , my_img2 , my_img3 , my_img4 , my_img5 ]

i = 0

def forward(num):
    global my_label
    my_label.grid_forget()
    if num == len(imgs)-1:
        num = 0
    else:
        num = num + 1
    global i
    i = num
    my_label = Label(image=imgs[num])
    my_label.grid(row=0,column=0,columnspan=3)

    status = Label(root,text="Image "+str(num+1)+" of "+str(len(imgs)), bd=1,relief=SUNKEN, anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)

def back(num):
    global my_label
    my_label.grid_forget()
    if num == 0:
        num = len(imgs) - 1
    else :
        num = num - 1
    global i
    i = num
    my_label = Label(image=imgs[num])
    my_label.grid(row=0,column=0,columnspan=3)
    status = Label(root,text="Image "+str(num+1)+" of "+str(len(imgs)), bd=1,relief=SUNKEN, anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)

my_label = Label(image=imgs[i])
my_label.grid(row=0,column=0,columnspan=3)
status = Label(root,text="Image "+str(i+1)+" of "+str(len(imgs)), bd=1,relief=SUNKEN, anchor=E)
status.grid(row=2,column=0,columnspan=3,sticky=W+E)

button_back = Button(root,text="<<",command=lambda: back(i) )
button_exit = Button(root,text="Exit",command=root.quit)
button_forward = Button(root,text=">>",command=lambda : forward(i) )

button_back.grid(row=1,column=0,pady=10)
button_exit.grid(row=1,column=1,pady=10)
button_forward.grid(row=1,column=2,pady=10)

root.mainloop()