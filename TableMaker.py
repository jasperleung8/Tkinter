from tkinter import *
from tkinter.ttk import *

window = Tk()
window.geometry("400x400")

title = Label(window,text="Maths Table Genarator",font=("Lato",30))
text = Label(window,text="Number and Range:",font=("Lato",15))

title.grid(row=0,column=0,columnspan=3,pady=10)
text.grid(row=1,column=0)

num = IntVar()
choice = IntVar()

def genarate():
    table = ""
    for i in range(1,choice.get()+1):
        result = num.get() * i
        table = table + f"{num.get()} X {i} = {result} \n"

    text2.config(text=table)

    

box = Combobox(window,textvariable=num,width=4)
box.grid(row=1,column=1)

box["values"] = tuple(range(1,11))
num.set(5)

r10 = Radiobutton(window,text="10",variable=choice,value=10)
r20 = Radiobutton(window,text="20",variable=choice,value=20)
r30 = Radiobutton(window,text="30",variable=choice,value=30)

r10.grid(row=2,column=0)
r20.grid(row=2,column=1)
r30.grid(row=2,column=2)

choice.set(10)

button = Button(window,text="Ok",command=genarate)
button.grid(row=3,column=0,columnspan=3)

text2 = Label(window,text="")
text2.grid(row=4,column=0,columnspan=3)

window.mainloop()
