from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
import os

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
    clearAll()

def clearAll():
    name.delete(0,END)
    address.delete(0,END)
    mobile.delete(0,END)
    email.delete(0,END)
    birthday.delete(0,END)

def reset():
    clearAll()
    addressbook.clear()
    list.delete(0,END)
    title.config(text="Address Book")



def save():
    file = asksaveasfile(defaultextension="*.txt")
    if file is not None:
        print(addressbook,file=file)
        reset()
    else:
        showwarning(message="Please sclect file")
    

def load():
    global addressbook
    file = askopenfile(filetypes=[("Text document","*.txt")])
    if file is not None:
        reset()
        addressbook = eval(file.read())
        for name in addressbook:
            list.insert(END,name)
        title.config(text=os.path.basename(file.name))
    else:
        showwarning(message="Please sclect file")

def delete():
    idx = list.curselection()
    if idx:
        for id in idx[::-1]:
            name2 = list.get(id)
            del addressbook[name2]
            list.delete(id)
    else:
        showwarning(message="Please select a name")

def edit():
    idx = list.curselection()
    if idx:
        if len(idx) > 1 :
            showwarning(message="Please select only one name")
        else:
            clearAll()
            name2 = list.get(idx)
            details = addressbook[name2]
            name.insert(0,name2)
            address.insert(0,details[0])
            mobile.insert(0,details[1])
            email.insert(0,details[2])
            birthday.insert(0,details[3])
    else:
        showwarning(message="Please select a name")

def info(event):
    window2 = Toplevel(window)
    idx = list.curselection()
    if idx:
        if len(idx) > 1 :
            showwarning(message="Please select only one name")
        else:
            name2 = list.get(idx)
            details = addressbook[name2]
            text = "Name:"+name2+"\nAddress:"+details[0]+"\nMobile:"+details[1]+"\nEmail:"+details[2]+"Birthday:"+details[3]
            text2 = Label(window2,text=text)
            text2.pack()


topframe = Frame(window)
topframe.pack()

title = Label(topframe,text="Address Book",font=("Lato",20))
save = Button(topframe,text="Save",command=save)
load = Button(topframe,text="Load",command=load)
title.grid(row=0,column=0)
save.grid(row=0,column=1,padx=20)
load.grid(row=0,column=2)

leftframe = Frame(window)
leftframe.pack(side=LEFT,padx=10)

list = Listbox(leftframe)
list.bind("<<ListboxSelect>>",info)
edit = Button(leftframe,text="Edit",command=edit)
delete = Button(leftframe,text="Delete",command=delete)
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