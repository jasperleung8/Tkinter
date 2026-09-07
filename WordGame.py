from tkinter import *
from tkinter.messagebox import *
import random

window = Tk()
window.geometry("300x400")

words = [
    "ability", "account", "address", "against", "already", "balance", "between", "billion", "blanket", "brother",
    "brought", "building", "cabinet", "capital", "careful", "central", "century", "certain", "chamber", "chapter",
    "channel", "charity", "chicken", "climate", "college", "company", "compare", "concept", "concern", "control",
    "country", "culture", "current", "defense", "deliver", "desktop", "develop", "diamond", "digital", "discuss",
    "disease", "display", "dynamic", "economy", "element", "evening", "exactly", "example", "factory", "feature",
    "federal", "feeling", "fiction", "finance", "foreign", "forward", "freedom", "further", "gallery", "general",
    "genuine", "grammar", "gravity", "harvest", "healthy", "history", "horizon", "hundred", "husband", "imagine",
    "improve", "include", "instead", "journal", "journey", "justice", "kitchen", "language", "laundry", "leather",
    "library", "license", "machine", "magazine", "manager", "market", "medical", "meeting", "mention", "message",
    "million", "mineral", "miracle", "missing", "monitor", "morning", "musical", "mystery", "network", "neutral"
]

def newWord():
    global words
    word = random.choice(words)
    char_list = list(word)
    random.shuffle(char_list)
    return [''.join(char_list),word]

def new():
    global randomWord
    answer.delete(0,END)
    randomWord = newWord()
    wordText.config(text="What is this word? \n\n"+randomWord[0])


def check():
    global randomWord
    if answer:
        if answer.get() == randomWord[1]:
            showinfo(message="Correct! Well done!")
        else:
           showwarning(message="Wrong answer.")
        new()
    else:
        showwarning(message="Please enter Something")


title = Label(window,text="Word Game!",font=("Lato",25))
title.pack(pady=10)

randomWord = newWord()
wordText = Label(window,text="What is this word? \n\n"+randomWord[0],font=("Lato",15))
wordText.pack(pady=25)

answer = Entry(window)
answer.pack()

ok = Button(window,text="Ok",command=check)
ok.pack()

window.mainloop()


