from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
import os

window = Tk()
window.geometry("500x600")

StudentLog = {}

def add():
    key = name.get()
    if key == "" :
        showerror(message="Enter a name")
    else:
        if key not in StudentLog:
            list.insert(END,key)
        StudentLog[key] = (mathsScore.get(),englishScore.get(),scienceScore.get(),historyScore.get())
    print(StudentLog)
    clearAll()

def clearAll():
    name.delete(0,END)
    mathsScore.delete(0,END)
    englishScore.delete(0,END)
    scienceScore.delete(0,END)
    historyScore.delete(0,END)

def reset():
    clearAll()
    StudentLog.clear()
    list.delete(0,END)
    title.config(text="Student Log")



def save():
    file = asksaveasfile(defaultextension="*.txt")
    if file is not None:
        print(StudentLog,file=file)
        reset()
    else:
        showwarning(message="Please sclect file")
    

def load():
    global StudentLog
    file = askopenfile(filetypes=[("Text document","*.txt")])
    if file is not None:
        reset()
        StudentLog = eval(file.read())
        for name in StudentLog:
            list.insert(END,name)
        title.config(text=os.path.basename(file.name))
    else:
        showwarning(message="Please sclect file")

def delete():
    idx = list.curselection()
    if idx:
        for id in idx[::-1]:
            name2 = list.get(id)
            del StudentLog[name2]
            list.delete(id)
    else:
        showwarning(message="Please select a name")

def edit():
    idx = list.curselection()
    if idx:
        if len(idx) > 1 :
            showwarning(message="Please select only one name")
        else:
            clearAll()
            name2 = list.get(idx)
            details = StudentLog[name2]
            name.insert(0,name2)
            mathsScore.insert(0,details[0])
            englishScore.insert(0,details[1])
            scienceScore.insert(0,details[2])
            historyScore.insert(0,details[3])
    else:
        showwarning(message="Please select a name")

def info(event):
    window2 = Toplevel(window)
    idx = list.curselection()
    if idx:
        if len(idx) > 1 :
            showwarning(message="Please select only one name")
        else:
            name2 = list.get(idx)
            details = StudentLog[name2]
            text = "Name:"+name2+"\nMaths Score:"+details[0]+"\nEnglish Score:"+details[1]+"\nScience Score:"+details[2]+"\nHistory Score:"+details[3]
            text2 = Label(window2,text=text)
            text2.pack()


topframe = Frame(window)
topframe.pack(pady=20)

title = Label(topframe,text="Student Log",font=("Lato",20))
save = Button(topframe,text="Save",command=save)
load = Button(topframe,text="Load",command=load)
title.grid(row=0,column=0)
save.grid(row=0,column=1,padx=20)
load.grid(row=0,column=2)

list = Listbox(window,width=40,height=10)
list.bind("<<ListboxSelect>>",info)
list.pack(pady=20)


bottomFrame = Frame(window)
bottomFrame.pack()

nametext = Label(bottomFrame,text="Name: ")
addresstext = Label(bottomFrame,text="Maths Score: ")
englishScoretext = Label(bottomFrame,text="English Score: ")
scienceScoretext = Label(bottomFrame,text="Science Score: ")
historyScoretext = Label(bottomFrame,text="History Score: ")

name = Entry(bottomFrame)
mathsScore = Entry(bottomFrame)
englishScore = Entry(bottomFrame)
scienceScore = Entry(bottomFrame)
historyScore = Entry(bottomFrame)

nametext.grid(row=0,column=0)
addresstext.grid(row=1,column=0)
englishScoretext.grid(row=2,column=0)
scienceScoretext.grid(row=3,column=0)
historyScoretext.grid(row=4,column=0)

name.grid(row=0,column=1)
mathsScore.grid(row=1,column=1)
englishScore.grid(row=2,column=1)
scienceScore.grid(row=3,column=1)
historyScore.grid(row=4,column=1)

add = Button(bottomFrame,text="Add/Update",command=add)
edit = Button(bottomFrame,text="Edit",command=edit)
delete = Button(bottomFrame,text="Delete",command=delete)

add.grid(row=5,column=0,pady=15)
edit.grid(row=5,column=1,pady=15)
delete.grid(row=5,column=2,pady=15)



window.mainloop()
