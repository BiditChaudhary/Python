from tkinter import *

win = Tk()

win.title("Tkinter Window")
win.geometry("400x200")
label1 = Label(win,text="Welcome to the Tkinter window",fg="blue")
entry = Entry()
button = Button(win,text="Enter",fg="red")

label1.pack(pady=20)
entry.pack(pady=20)
button.pack(pady=20)

win.mainloop()