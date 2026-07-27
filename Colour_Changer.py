from tkinter import *

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

def change():
    idx = list.curselection()
    colour = list.get(idx)
    window.config(bg=colour)
    


bar = Scrollbar(window)
bar.grid(row=0,column=0)

list = Listbox(window,yscrollcommand=bar.set)
list.grid(row=0,column=1,rowspan=3)

save = Button(window,text="Change",command=change)
save.grid(row=0,column=2,padx=15)

add = Button(window,text="Add",command=addItem)
add.grid(row=1,column=2,padx=15)

item = Entry(window)
item.grid(row=2,column=2,columnspan=2)

remove = Button(window,text="Remove",command=deleteItem)
remove.grid(row=1,column=3)


window.mainloop()