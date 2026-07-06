from tkinter import *
from time import strftime
from random import choice

window = Tk()
window.config(background="Light Blue")
window.geometry("500x400")

colours = ["Red","Yellow","Green","blue","Dark Green","Dark Blue","Purple","Pink","Light Blue","Black","White"]

def getTime():
    time = strftime("%I:%M:%S %p")
    date = strftime("%a, %d of %b, %Y")

    text.config(text=time,bg=choice(colours),fg=choice(colours))
    text2.config(text=date,bg=choice(colours),fg=choice(colours))
    text.after(1000,getTime)

text = Label(window,text="",font=("Lato",50),bg=choice(colours),fg=choice(colours))
text2 = Label(window,text="",font=("Lato",30),bg=choice(colours),fg=choice(colours))
title = Label(window,text="The Clock",font=("Lato",35),bg="Light Blue",fg="Black")
title.pack()
text.pack(pady=30)
text2.pack(pady=5)

getTime()

window.mainloop()
