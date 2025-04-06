import tkinter
from tkinter import *

win = Tk()
win.geometry("400x400")
win.title("Main window")

def topwin():
    t = Toplevel()
    t.geometry("200x200")
    t.title("Top window")
    label2 = Label(t,text="This is the top window",font=("Arial",17,"normal"))
    label2.place(x=10,y=100)

label1 = Label(win,text="This is the main window",font=("Arial",23,"normal"))
label1.place(x=10,y=100)

button1 = Button(win,text="Click me",command=topwin)
button1.place(x=10,y=140)

win.mainloop()