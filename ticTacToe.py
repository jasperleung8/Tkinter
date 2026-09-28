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


def Win(player):
    showinfo(message=f"{player} won!")
    gameScreen.pack_forget()
    startScreen.pack()
    box1.config(text="")
    box2.config(text="")
    box3.config(text="")
    box4.config(text="")
    box5.config(text="")
    box6.config(text="")
    box7.config(text="")
    box8.config(text="")
    box9.config(text="")

def Draw():
    showinfo(message=f"Draw!")
    gameScreen.pack_forget()
    startScreen.pack()
    box1.config(text="")
    box2.config(text="")
    box3.config(text="")
    box4.config(text="")
    box5.config(text="")
    box6.config(text="")
    box7.config(text="")
    box8.config(text="")
    box9.config(text="")

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
    
def checkDraw():
    for pos in Gameboard:
        if Gameboard[pos].cget("text") == "":
            return False
    return True

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

    botTurn()

def playerTurn(box):
    global currentPlayer
    if currentPlayer == playerMarker:
        print("SSDFGHGFFGHGCFJHGDGSDGFDFDGF",Gameboard[box].cget("text"))
        if Gameboard[box].cget("text") == "":
            Gameboard[box].config(text=playerMarker)
            win = checkWin(playerMarker)
            if win:
                Win(playerMarker)
            elif checkDraw():
                Draw()
            else:
                currentPlayer = botMarker
                botTurn()          
        else:
            showerror(text="Please choose another box")
        

def botTurn():
    global currentPlayer

    for pos in Gameboard:
        if Gameboard[pos].cget("text") == "":
            Gameboard[pos].config(text=botMarker)
            if checkWin(botMarker):
                print()
                Win(botMarker)
            elif checkDraw():
                Draw()
            else:
                Gameboard[pos].config(text="")

    for pos in Gameboard:
        if Gameboard[pos].cget("text") == "":
            Gameboard[pos].config(text=playerMarker)
            if checkWin(playerMarker):
                Gameboard[pos].config(text=botMarker)
                currentPlayer = playerMarker
                return
            else:
                Gameboard[pos].config(text="")
        
    if Gameboard[5].cget("text") == "":
        Gameboard[5].config(text=botMarker)
        currentPlayer = playerMarker
        return
    
    for coner in [1,3,7,9]:
        if Gameboard[coner].cget("text") == "":
            Gameboard[coner].config(text=botMarker)
            currentPlayer = playerMarker
            return
    
    for pos in Gameboard:
        if Gameboard[pos].cget("text") == "":
            Gameboard[pos].config(text=botMarker)
            currentPlayer = playerMarker
            return



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
box9.grid(row=2,column=2)



gameScreen.mainloop()
