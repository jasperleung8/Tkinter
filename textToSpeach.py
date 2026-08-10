from tkinter import *
from gtts import gTTS
# from playsound import playsound

window = Tk()
window.geometry("300x400")

def convert():
    text2 = entry.get()
    speech = gTTS(text2,lang="fr")
    speech.save("speech.mp3")

# def play():
#     playsound("speech.mp3")

title = Label(window,text="Text to speach",font=("Comfortaa",25))
title.grid(row=0,column=0,columnspan=2,pady=15)

text = Label(window,text="Put your text here and press ok")
text.grid(row=1,column=0)

entry = Entry(window)
entry.grid(row=2,column=0)

ok = Button(window,text="Ok",command=convert)
ok.grid(row=2,column=1)

# play = Button(window,text="Play")
# play.grid(row=3,column=0,pady=5)

window.mainloop()

