from tkinter import *
from tkinter import messagebox
from random import randint

def ok():
    if int(guess.get()) == num:
        messagebox.showinfo(message=f"Well done! You have guessed the number!")
        exit()
    elif int(guess.get()) >= num:
        messagebox.showinfo(message=f"Your guess is too high. Try again")
    else:
        messagebox.showinfo(message=f"Your guess is too low. Try again")


def start():
    global guess, num

    num = randint(1,20)
    messagebox.showinfo(title="Hello",message=f"Hi there {name.get()}! I am thinking of a number from 1 to 20. Can you guess?")
    
    game = Tk()
    game.geometry("500x300")

    text3 = Label(game,text="Put in a number a hit the guess button!")
    guess = Entry(game)
    confirm = Button(game,text="Guess!",command=ok)

    text3.pack(pady=10)
    guess.pack()
    confirm.pack()     

    game.mainloop()

home = Tk()
home.geometry("500x300")

text = Label(home,text="Welcome!")
text2 = Label(home,text="Enter your name:")
name = Entry(home)
button = Button(home,text="Ok",command=start)

text.pack()
text2.pack(pady=15)
name.pack()
button.pack()
home.mainloop()