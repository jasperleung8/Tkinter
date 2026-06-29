from tkinter import *
from time import strftime

window = Tk()
window.config(background="Light Blue")
window.geometry("500x200")

def getTime():
    time = strftime("%I:%M:%S %p")
    text.config(text=time)
    text.after(1000,getTime)

text = Label(window,text="",font=("Lato",50),bg="White",fg="Black")
text.pack(pady=50)

getTime()

window.mainloop()