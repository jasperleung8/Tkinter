from tkinter import *

window = Tk()

bar = Scrollbar(window)
bar.pack(side=LEFT,fill=Y)

list = Listbox(window,yscrollcommand=bar.set)
list.pack(side=RIGHT)

bar.config(command=list.yview)

for i in range(1,50):
    list.insert(END,i)

window.mainloop()