from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("400x400")
root.title("Image")

upload = Image.open("schoolcinema.png")
upload = upload.resize((300,300))

Image = ImageTk.PhotoImage(upload)
label1 = Label(root,image=Image)
label1.pack()

label2 = Label(root,text="GEMS",font=("courier",24,"bold"))
label2.place(x=20,y=310)

root.mainloop()