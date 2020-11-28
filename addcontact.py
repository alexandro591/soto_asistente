import subprocess
from tkinter import *
from PIL import Image, ImageTk

W = 1020
H = 532

app = Tk()
app.geometry(str(W) + "x" + str(H))
app.title("Soto asistente")
app.configure(background='black')

######################################
name_label = Label(app, text="Añadir un contacto", font=("Helvetica", 16), fg = "white")
name_label.configure(anchor="center", background='black')
name_label.place(x=W/2-65, y=40)

try:
    logo = Image.open("/home/pi/soto_hmi/img/logo.png")
except:
    logo = Image.open("img/logo.png")

logo = logo.resize((120,120))

entry_name = Label(app, text="Nombre:", font=("Helvetica", 12), fg = "white")
entry_name.configure(anchor="center", background='black')
entry_name.place(x=200, y=250)


render = ImageTk.PhotoImage(logo)

logo_label = Label(app, image=render)
logo_label.configure(background='black')
logo_label.image = render
logo_label.place(x=W/2-55, y=80)
######################################

app.mainloop()

