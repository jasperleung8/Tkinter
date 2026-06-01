from tkinter import *
import calendar

window = Tk()

def show():
    calendar_window = Tk()
    calendar_year = int(year.get())
    info = calendar.calendar(calendar_year)
    data = Text(calendar_window,height=600)
    data.insert(END,info)
    data.pack()
    calendar_window.mainloop()

window.geometry("400x400")
window.config(background="blue")
window.title("Calendar app")

title = Label(window,text="Calendar")
title.pack()
text = Label(window,text="Year")
text.pack(pady=3)

year = Entry(window)
year.pack(pady=8)

button = Button(window,text="show calendar",command=show)
button.pack(pady=13)
# button2 = Button(window,text="Close",command=window.destroy)
button2 = Button(window,text="Close",command=exit)
button2.pack(pady=15)
window.mainloop()