from tkinter import *
import random

options = ["Rock","Paper","Scissors"]
playerscore = 0
compscore = 0


def game(playerChoice):
    global playerscore,compscore

    compSelected = random.choice(options)
    if playerChoice == compSelected:
        message.config(text="Tie")
    elif (playerChoice=="Rock" and compSelected=="Scissors") or (playerChoice=="Paper" and compSelected=="Rock") or (playerChoice=="Sicissors" and compSelected=="Paper"):
        message.config(text="You Win!")
        playerscore = playerscore+1
    else:
        message.config(text="You lose")
        compscore = compscore+1

    youSelected_text2.config(text=playerChoice)
    compSelected_text2.config(text=compSelected)
    yourScore_text2.config(text=playerscore)
    compScore_text2.config(text=compscore)



window = Tk()
window.geometry("500x500")
topframe = Frame(window)
topframe.pack()

title = Label(topframe,text="Rock Paper Scissors!",font=("Comfortaa",30))
title.pack()

leftframe = Frame(window)
leftframe.pack(side="left",padx=20)

text = Label(leftframe,text="Select an option",font=("Comfortaa",20))
rockButton = Button(leftframe,text="Rock",width=10,command=lambda:game(options[0]))
paperButton = Button(leftframe,text="Paper",width=10,command=lambda:game(options[1]))
scissorsButton = Button(leftframe,text="Scissors",width=10,command=lambda:game(options[2]))

text.pack(pady=16)
rockButton.pack(pady=8)
paperButton.pack(pady=8)
scissorsButton.pack(pady=8)

rightframe = Frame(window)
rightframe.pack(side="right",padx=80)

youSelected_text = Label(rightframe,text="You selected:")
youSelected_text2 = Label(rightframe)
compSelected_text = Label(rightframe,text="Computer selected:")
compSelected_text2 = Label(rightframe)

yourScore_text = Label(rightframe,text="Your Score:")
yourScore_text2 = Label(rightframe)
compScore_text = Label(rightframe,text="Computer Score:")
compScore_text2 = Label(rightframe)

youSelected_text.pack(pady=5)
youSelected_text2.pack(pady=5)
compSelected_text.pack(pady=5)
compSelected_text2.pack(pady=5)

yourScore_text.pack(pady=5)
yourScore_text2.pack(pady=5)
compScore_text.pack(pady=5)
compScore_text2.pack(pady=5)

bottomframe = Frame(window)
bottomframe.pack(side="bottom")

message = Label(bottomframe)
message.pack()


window.mainloop()