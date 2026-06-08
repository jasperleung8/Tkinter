from tkinter import*
from tkinter import messagebox

window = Tk()

messagebox.showinfo(title="Hello",message="hi there!")
messagebox.showwarning(message="Warning!")
messagebox.showerror(message="Error")

answer = messagebox.askquestion(message="Are you sure?")
print(answer)

answer2 = messagebox.askokcancel(message="Are you actually sure?") #ok = true cancal = false
print(answer2)

answer3 = messagebox.askyesno(message="Really?")
print(answer3)

answer4 = messagebox.askretrycancel(message="Error")
print(answer4)
window.mainloop()