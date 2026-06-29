from tkinter import *
from tkinter import messagebox
import time

window = Tk()

def start():
    hours.config(state="disabled")
    minutes.config(state="disabled")
    seconds.config(state="disabled")
    button.config(state="disabled")

    try :
        total = (int(h.get())*60*60) + (int(m.get())*60) + int(s.get())
    except:
        messagebox.showerror(message="Enter a number!")
    
    while total >= 0 :
        mins,secs = divmod(total,60)
        hrs = 0
        if minutes > 60:
            hrs,mins = divmod(total,60)
        
        h.set(hrs)
        m.set(mins)
        s.set(secs)
        window.update()
        time.sleep(1)

def reset():
    h.set("00")
    m.set("00")
    s.set("00")

h = StringVar()
m = StringVar()
s = StringVar()
reset()

hours = Entry(window,textvariable=h)
minutes = Entry(window,textvariable=m)
seconds = Entry(window,textvariable=s)
button = Button(window,text="Start!",command=start)

hours.grid(row=0,column=0)
minutes.grid(row=0,column=1)
seconds.grid(row=0,column=2)
button.grid(row=1,column=1)

window.mainloop()