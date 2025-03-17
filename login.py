from tkinter import *

window = Tk()
window.title("Login")
window.geometry("450x300")
window.config(background="Orange")

username = Label(window,
                 text="Username :").place(x=40,
                                          y=60)

password = Label(window,
                 text="Password :").place(x=40,
                                          y=100)

Login_button = Button(window,
                      text="Login!").place(x=40,
                                           y=130)

Username_input = Entry(window,
                      width=30).place(x=110,
                                           y=60)

password_input = Entry(window,show="*",
                      width=30).place(x=110,
                                           y=100)

window.mainloop()






