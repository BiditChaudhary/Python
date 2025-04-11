from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk

root = Tk()
root.geometry("500x500")
upload = Image.open("schoolcinema.png")
upload = upload.resize((300,300))
img = ImageTk.PhotoImage(upload)

label = Label(root,image=img)
label.place(x=100,y=10)

label2 = Label(root,text="Hello! Welcome to the denomination calculator!",font=("cursive",14,"bold"))
label2.pack()

def msg():
    msgbox = messagebox.showinfo("Information","This window will calculate the denomination of the notes required in the amount you input:")
    if msgbox == 'ok':
        toplevel()


button = Button(root,text="Click here to proceed",command=msg)
button.pack()

def toplevel():

    def calculate_denomination():
        entry2.delete(0,END)
        entry3.delete(0,END)
        entry4.delete(0,END)
        global amount
        amount = int(entry1.get())
        note2000 = amount // 2000
        amount = amount % 2000
        note500 = amount // 500
        amount = amount % 500
        note100 = amount // 100
        entry2.insert(END,note2000)
        entry3.insert(END,note500)
        entry4.insert(END,note100)
        

    top = Toplevel()
    top.geometry("500x500")
    top.title("Top window")
    label3 = Label(top,text="Enter the amount")

    entry1 = Entry(top)
    label3.place(x=100,y=100)
    entry1.place(x=200,y=100)

    button2 = Button(top,text="Calculate",command=calculate_denomination)
    button2.place(x=300,y=100)

    label4 = Label(top,text="The denominaton calculator")
    label5 = Label(top,text="2000")
    label6 = Label(top,text="500")
    label7 = Label(top,text="100")

    entry2 = Entry(top)
    entry3 = Entry(top)
    entry4 = Entry(top)

    label4.place(x=150,y=140)
    label5.place(x=100,y=180)
    label6.place(x=100,y=200)
    label7.place(x=100,y=220)

    entry2.place(x=200,y=180)
    entry3.place(x=200,y=200)
    entry4.place(x=200,y=220)






root.mainloop()