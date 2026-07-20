from tkinter import *
from tkinter.filedialog import *

window = Tk()

def save():
    asksaveasfile(defaultextension='*.txt')

def open():
    file = askopenfile(filetypes=[("Python Files","*.py"),("Text document","*.txt")])
    print(file.read())


open = Button(window,text="Open",command=open)
save = Button(window,text="Save",command=save)

open.pack()
save.pack()

window.mainloop()