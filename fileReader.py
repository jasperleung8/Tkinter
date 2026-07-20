from tkinter import *
from tkinter.filedialog import *

window = Tk()
window.geometry("500x300")

def addItem():
    list.insert(END,item.get())
    item.delete(0,END)

def deleteItem():
    idx = list.curselection()
    idx = idx[::-1]
    if idx:
        for i in idx:
            list.delete(i)

def saveFile():
    file = asksaveasfile(defaultextension="*.txt")
    if file is not None:
        for item in list.get(0,END):
            print(item.strip(),file=file)
        list.delete(0,END)


bar = Scrollbar(window)
bar.grid(row=0,column=0)

list = Listbox(window,yscrollcommand=bar.set,selectmode=MULTIPLE)
list.grid(row=0,column=1)

save = Button(window,text="Save",command=saveFile)
save.grid(row=0,column=2,padx=15)

load = Button(window,text="Load")
load.grid(row=0,column=3)

add = Button(window,text="Add",command=addItem)
add.grid(row=1,column=2,padx=15)

item = Entry(window)
item.grid(row=2,column=2,columnspan=2)

remove = Button(window,text="Remove",command=deleteItem)
remove.grid(row=1,column=3)


window.mainloop()