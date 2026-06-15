from tkinter import *

window = Tk()
window.geometry("600x300")
window.title("Currency Converter")

def convert():
    if Pounds.get().isnumeric():
        Dollars = int(Pounds.get())*1.35
        text3.config(text=f"In Dollars:                                 {Dollars}",foreground="Black")
        text3.place(x=100,y=120)
        button.place(x=100,y=150)
        button2.place(x=430,y=150)
    else:
        text3.config(text="Please Enter a number",foreground="Red")
        text3.place(x=100,y=120)
        button.place(x=100,y=150)
        button2.place(x=430,y=150)
    button.config(text="Clear",command=clear)

def clear():
    button.place(x=100,y=130)
    button2.place(x=430,y=130)
    text3.config(text="")
    button.config(text="Convert",command=convert)


text = Label(window,text="Currency Converter",font=("Comfortaa",30))
text.place(x=170,y=30)
text2 = Label(window,text="Enter Pounds : ",font=("Comfortaa",15),foreground="Grey")
text2.place(x=100,y=90)

Pounds = Entry(window)
Pounds.place(x=300,y=90)

text3 = Label(window,text="In Dollars:",font=("Comfortaa",15),foreground="Black")

button = Button(window,text="Convert",foreground="Black",command=convert)
button.place(x=100,y=130)
button2 = Button(window,text="Exit",foreground="Grey",command=window.quit)
button2.place(x=430,y=130)

window.mainloop()