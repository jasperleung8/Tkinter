from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *

window = Tk()
window.geometry("500x400")

addressbook = {}

def add():
    key = name.get()
    if key == "" :
        showerror(message="Enter a name")
    else:
        if key not in addressbook:
            list.insert(END,key)
        addressbook[key] = (address.get(),mobile.get(),email.get(),birthday.get())
    print(addressbook)


topframe = Frame(window)
topframe.pack()

title = Label(topframe,text="Address Book",font=("Lato",20))
save = Button(topframe,text="Save")
load = Button(topframe,text="Load")
title.grid(row=0,column=0)
save.grid(row=0,column=1,padx=20)
load.grid(row=0,column=2)

leftframe = Frame(window)
leftframe.pack(side=LEFT,padx=10)

list = Listbox(leftframe)
edit = Button(leftframe,text="Edit")
delete = Button(leftframe,text="Delete")
list.grid(row=0,column=0,columnspan=2)
edit.grid(row=1,column=0)
delete.grid(row=1,column=1)


rightframe = Frame(window)
rightframe.pack(side=RIGHT,padx=10)

nametext = Label(rightframe,text="Name: ")
addresstext = Label(rightframe,text="Address: ")
mobiletext = Label(rightframe,text="Mobile: ")
emailtext = Label(rightframe,text="Email: ")
birthdaytext = Label(rightframe,text="Birthday: ")

name = Entry(rightframe)
address = Entry(rightframe)
mobile = Entry(rightframe)
email = Entry(rightframe)
birthday = Entry(rightframe)

nametext.grid(row=0,column=0)
addresstext.grid(row=1,column=0)
mobiletext.grid(row=2,column=0)
emailtext.grid(row=3,column=0)
birthdaytext.grid(row=4,column=0)

name.grid(row=0,column=1)
address.grid(row=1,column=1)
mobile.grid(row=2,column=1)
email.grid(row=3,column=1)
birthday.grid(row=4,column=1)

add = Button(rightframe,text="Add/Update",command=add)
add.grid(row=5,column=0,columnspan=2)



window.mainloop()