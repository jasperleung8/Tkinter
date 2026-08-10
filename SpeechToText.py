from tkinter import *
import speech_recognition as sr

window = Tk()
window.geometry("300x400")

def countDown(count):
    if count > 0:
        text.config(text="Get Ready "+str(count))
        window.after(1000,countDown,count-1)
    else:
        text.config(text="Speak now")

def start():
    record.config(state="disabled")
    countDown(3)
    stop.config(state="normal")
    


title = Label(window,text="Speech To Text",font=("Comfortaa",20))
title.pack(pady=10)

output = Text(window,width=30,height=15)
output.pack()
output.insert(END,"Start recording to turn your speech into text!")

record = Button(window,text="Start recoding",command=start)
record.pack()

stop = Button(window,text="Stop recoding",state="disabled")
stop.pack()

save = Button(window,text="Save")
save.pack()

text = Label(window,text="Start recording",font=("Comfortaa",15))
text.pack(pady=10)

window.mainloop()