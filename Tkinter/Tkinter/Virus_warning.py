import tkinter
from tkinter import *
from tkinter import messagebox


root = Tk()

def Virus():
    messagebox.showwarning("Virus alert!","Scan now!")

root.geometry("400x400")
root.title("Message box")
label1 = Label(root,text="This is a Message box window",font=("georgia",20,"normal"))
label1.pack()

button = Button(root,text="Scan",command=Virus)
button.pack()

root.mainloop()