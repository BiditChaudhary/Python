import tkinter
from tkinter import *
window = Tk()
window.title("Grid system")
window.geometry("200x300")
t = 1
for i in range(1,4):
    window.rowconfigure(i,weight=1,minsize=50)
    for j in range(1,4):
        window.columnconfigure(j,weight=0,minsize=50)
        label = Label(window, relief = RAISED, bg = 'green',fg = "red", text = t, width = 3)
        t += 1
        label.grid(row = i, column= j)

window.mainloop()
