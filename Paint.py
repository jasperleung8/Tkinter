from tkinter import *
from tkinter.colorchooser import askcolor

window = Tk()

def UsePen():
    activateButton(pen)

def UseErser():
    activateButton(erser,True)

def UseColour():
    global selectedColour

    activateButton(colour)
    selectedColour = askcolor(color=selectedColour)[1]

def activateButton(button,eraserMode=False):
    global activeButton, erserActive
    
    print("1")
    activeButton.config(relief=RAISED)
    activeButton = button
    print("2")
    activeButton.config(relief=SUNKEN)
    print("3")
    erserActive = eraserMode

def draw(event):
    global oldx, oldy, selectedColour

    if erserActive:
        selectedColour = "white"
    if oldx and oldy:
        drawing.create_line(oldx,oldy,event.x,event.y,width=slider.get(),fill=selectedColour,capstyle=ROUND,smooth=True)
    oldx = event.x
    oldy = event.y

def release(event):
    global oldx, oldy

    oldx = None
    oldy = None

    

pen = Button(window,text="Pen",command=UsePen)
colour = Button(window,text="Colour",command=UseColour)
erser = Button(window,text="Erser",command=UseErser)
slider = Scale(window,from_=1,to=35,orient=HORIZONTAL)

pen.grid(column=0,row=0)
colour.grid(column=1,row=0)
erser.grid(column=2,row=0)
slider.grid(column=3,row=0)

drawing = Canvas(window,bg="white")
drawing.grid(column=0,row=1,columnspan=4)




#setup

oldx = None
oldy = None

selectedColour = "black"
thickness = 5
slider.set(5)

activeButton = pen
pen.config(relief=SUNKEN)
erserActive = False

drawing.bind("<B1-Motion>",draw)
drawing.bind("<ButtonRelease-1>",release)


window.mainloop()
