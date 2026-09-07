from tkinter import*

window = Tk()

menu = Menu(window)
file = Menu(menu)
menu.add_cascade(label="File",menu=file)
file.add_command(label="New file",command=None)
file.add_command(label="New window",command=None)
file.add_separator()
file.add_command(label="Save")
file.add_command(label="Save as")
file.add_command(label="Open")
file.add_separator()
file.add_command(label="Close",command=window.destroy)

edit = Menu(menu)
menu.add_cascade(label="Edit",menu=edit)
edit.add_command(label="Undo")
edit.add_command(label="Redo")
file.add_separator()
edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")
file.add_separator()
edit.add_command(label="Find")
edit.add_command(label="Replace")
file.add_separator()
edit.add_command(label="Font")
edit.add_command(label="Emojis")

window.config(menu=menu)

window.mainloop()