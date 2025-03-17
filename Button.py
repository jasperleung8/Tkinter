from tkinter import *

window = Tk()

window.geometry("100x100")

button = Button (window,text="Delete window",bd=5,background="red",command=window.destroy)

button.pack(side="left")

window.mainloop()