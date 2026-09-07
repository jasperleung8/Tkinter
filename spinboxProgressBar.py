from tkinter import*
from tkinter.ttk import*
from time import sleep

window = Tk()

def start():
    for i in range(1,101,5):
        bar["value"]=i
        window.update_idletasks()
        sleep(1)

box = Spinbox(window,from_=0,to=100)
box.pack()

bar = Progressbar(window,orient=HORIZONTAL,length=100,mode="determinate")
bar.pack()

button = Button(window,text="Start!",command=start)
button.pack()

window.mainloop()