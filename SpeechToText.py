from tkinter import *
import speech_recognition as sr
import sounddevice as sd

window = Tk()
window.geometry("300x400")

speech = sr.Recognizer()
sampleRate = 16000

audioList = []
listening = None

def addAudio(data,frames,time,status):
    audioList.append(data)
    print("add")
    print(audioList)

def convert():
    if not audioList:
        output.insert(END,"No Speech recorded")
        return
    try :
        audioBytes = b"".join(audioList)
        audio = sr.AudioData(audioBytes,sample_rate=sampleRate,sample_width=2)
        speechtext = sr.recognize_google(audio)
        output.insert(END,speechtext)
    except:
        print()

    

def listen():
    global listening
    stream = sd.InputStream(sampleRate,channels=1,dtype="int16",callback=addAudio)
    stream.start()
    print("listen")

def countDown(count):
    if count > 0:
        text.config(text="Get Ready "+str(count))
        window.after(1000,countDown,count-1)
    else:
        text.config(text="Speak now")
    listen()

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

stop = Button(window,text="Stop recoding",state="disabled",command=convert)
stop.pack()

save = Button(window,text="Save")
save.pack()

text = Label(window,text="Start recording",font=("Comfortaa",15))
text.pack(pady=10)

window.mainloop()