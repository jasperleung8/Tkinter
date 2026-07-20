from tkinter import*
from tkinter.ttk import*

def show():
    global num, choice, option
    message.config(text=f"You have ordered {num.get()} {choice.get()} {option.get()} Pizza(s) ")

window = Tk()
window.geometry("300x400")

num = IntVar()
choice = StringVar()

text = Label(window,text="Order your pizza here!",font=("Lato",15))
text.pack(pady=10)

text = Label(window,text="Choose your pizza:")
text.pack(pady=5)

pizzas = ["pepperoni","margherita","pineapple"]

option = StringVar()
menu = OptionMenu(window,option,*pizzas)
option.set("pepperoni")
menu.pack()

r1 = Radiobutton(window,text="Small",variable=choice,value="Small")
r2 = Radiobutton(window,text="Medium",variable=choice,value="Medium")
r3 = Radiobutton(window,text="Large",variable=choice,value="Large")

r1.pack()
r2.pack()
r3.pack()

choice.set("Large")

text = Label(window,text="Enter Amount:")
text.pack(pady=5)

box = Combobox(window,textvariable=num,width=4)
box.pack()

box["values"] = tuple(range(1,11))
num.set(10)

ok = Button(window,text="Order",command=show)
ok.pack(pady=10)

message = Label(window,text="")
message.pack()

window.mainloop()
