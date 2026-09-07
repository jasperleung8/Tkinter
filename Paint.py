from tkinter import *

window = Tk()

pen = Button(window,text="Pen")
colour = Button(window,text="Colour")
erser = Button(window,text="Erser")
slider = Scale(window,from_=1,to=35,orient=HORIZONTAL)

pen.grid(column=0,row=0)
colour.grid(column=1,row=0)
erser.grid(column=2,row=0)
slider.grid(column=3,row=0)

drawing = Canvas(window,bg="white")
drawing.grid(column=0,row=1,columnspan=4)

window.mainloop()
