from tkinter import *
from tkinter.messagebox import *

window = Tk()

currentPlayer = None

playerMarker = None
botMarker = None

gameScreen = Frame(window)

box1 = Button(gameScreen,text="",command=lambda:playerTurn(1))
box2 = Button(gameScreen,text="",command=lambda:playerTurn(2))
box3 = Button(gameScreen,text="",command=lambda:playerTurn(3))
box4 = Button(gameScreen,text="",command=lambda:playerTurn(4))
box5 = Button(gameScreen,text="",command=lambda:playerTurn(5))
box6 = Button(gameScreen,text="",command=lambda:playerTurn(6))
box7 = Button(gameScreen,text="",command=lambda:playerTurn(7))
box8 = Button(gameScreen,text="",command=lambda:playerTurn(8))
box9 = Button(gameScreen,text="",command=lambda:playerTurn(9))

Gameboard = {1:box1,2:box2,3:box3,
             4:box4,5:box5,6:box6,
             7:box7,8:box8,9:box9}


def checkWin(mark):
    if (Gameboard[1].cget("text") == Gameboard[2].cget("text") and Gameboard[1].cget("text") == Gameboard[3].cget("text") and Gameboard[1].cget("text") == mark):
        return True
    elif (Gameboard[4].cget("text") == Gameboard[5].cget("text") and Gameboard[4].cget("text") == Gameboard[6].cget("text") and Gameboard[4].cget("text") == mark):
        return True
    elif (Gameboard[7].cget("text") == Gameboard[8].cget("text") and Gameboard[7].cget("text") == Gameboard[9].cget("text") and Gameboard[7].cget("text") == mark):
        return True
    elif (Gameboard[1].cget("text") == Gameboard[4].cget("text") and Gameboard[1].cget("text") == Gameboard[7].cget("text") and Gameboard[1].cget("text") == mark):
        return True
    elif (Gameboard[2].cget("text") == Gameboard[5].cget("text") and Gameboard[2].cget("text") == Gameboard[8].cget("text") and Gameboard[2].cget("text") == mark):
        return True
    elif (Gameboard[3].cget("text") == Gameboard[6].cget("text") and Gameboard[3].cget("text") == Gameboard[9].cget("text") and Gameboard[3].cget("text") == mark):
        return True
    elif (Gameboard[1].cget("text") == Gameboard[5].cget("text") and Gameboard[1].cget("text") == Gameboard[9].cget("text") and Gameboard[1].cget("text") == mark):
        return True
    elif (Gameboard[7].cget("text") == Gameboard[5].cget("text") and Gameboard[7].cget("text") == Gameboard[3].cget("text") and Gameboard[7].cget("text") == mark):
        return True
    else:
        return False

def playerStart():
    global playerMarker,botMarker,currentPlayer
    playerMarker = "x"
    botMarker = "o"
    currentPlayer = playerMarker

    startScreen.pack_forget()
    gameScreen.pack()

def botStart():
    global playerMarker,botMarker,currentPlayer
    playerMarker = "o"
    botMarker = "x"
    currentPlayer = botMarker

    startScreen.pack_forget()
    gameScreen.pack()

def playerTurn(box):
    global currentPlayer
    if currentPlayer == playerMarker:
        print("SSDFGHGFFGHGCFJHGDGSDGFDFDGF",Gameboard[box].cget("text"))
        if Gameboard[box].cget("text") != "":
            Gameboard[box].config(text=playerMarker)
            # currentPlayer = botMarker
        else:
            showerror(text="Please choose another box")


startScreen = Frame(window)

title = Label(startScreen,text="Who do you what to go first?")
playerButton = Button(startScreen,text="Player",command=playerStart)
botButton = Button(startScreen,text="Bot",command=botStart)

title.pack(pady=10)
playerButton.pack()
botButton.pack()

startScreen.pack()

box1.grid(row=0,column=0)
box2.grid(row=0,column=1)
box3.grid(row=0,column=2)
box4.grid(row=1,column=0)
box5.grid(row=1,column=1)
box6.grid(row=1,column=2)
box7.grid(row=2,column=0)
box8.grid(row=2,column=1)
box9.grid(row=2,column=2)



gameScreen.mainloop()