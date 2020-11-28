import subprocess
from tkinter import *
from PIL import Image, ImageTk
from os import path

W = 1020
H = 532

def addContact(e):
    try:
        subprocess.check_call('python3 /home/pi/soto_hmi/addcontact.py'.split(" "))
    except:
        subprocess.check_call('python3 addcontact.py'.split(" "))
def videoGame(e):
    try:
        subprocess.check_call('python3 /home/pi/soto_hmi/tic-tac-toe/main.py'.split(" "))
    except:
        subprocess.check_call('python3 tic-tac-toe/main.py'.split(" "))
def videoCall(e):
    try:
        if path.exists("/home/pi/soto_hmi/videocall.html"):
            subprocess.check_call('sensible-browser /home/pi/soto_hmi/videocall.html'.split(" "))
        else:
            subprocess.check_call('sensible-browser videocall.html'.split(" "))
    except:
        subprocess.check_call('sensible-browser videocall.html'.split(" "))

app = Tk()
app.geometry(str(W) + "x" + str(H))
app.title("Soto asistente")
app.configure(background='black')

######################################
name_label = Label(app, text="Soto Asistente", font=("Helvetica", 16), fg = "white")
name_label.configure(anchor="center", background='black')
name_label.place(x=W/2-65, y=40)

try:
    logo = Image.open("/home/pi/soto_hmi/img/logo.png")
except:
    logo = Image.open("img/logo.png")

logo = logo.resize((120,120))

render = ImageTk.PhotoImage(logo)

logo_label = Label(app, image=render)
logo_label.configure(background='black')
logo_label.image = render
logo_label.place(x=W/2-55, y=80)
######################################

######################################
command_name_label = Label(app, text="Añadir un contacto", font=("Helvetica", 12), fg = "white")
command_name_label.configure(anchor="center", background='black')
command_name_label.place(x=70, y=370)

try:
    image_label = Image.open("/home/pi/soto_hmi/img/contact.png")
except:
    image_label = Image.open("img/contact.png")

image_label = image_label.resize((80,80))

render = ImageTk.PhotoImage(image_label)

command_label = Label(app, image=render)
command_label.bind("<Button-1>",addContact)
command_label.configure(background='black')
command_label.image = render
command_label.place(x=100, y=280)
######################################

######################################
command_name_label = Label(app, text="Video Llamada", font=("Helvetica", 12), fg = "white")
command_name_label.configure(anchor="center", background='black')
command_name_label.place(x=285, y=370)

try:
    image_label = Image.open("/home/pi/soto_hmi/img/videocall.png")
except:
    image_label = Image.open("img/videocall.png")

image_label = image_label.resize((80,80))

render = ImageTk.PhotoImage(image_label)

command_label = Label(app, image=render)
command_label.bind("<Button-1>",videoCall)
command_label.configure(background='black')
command_label.image = render
command_label.place(x=300, y=280)
######################################

######################################
command_name_label = Label(app, text="Juegos", font=("Helvetica", 12), fg = "white")
command_name_label.configure(anchor="center", background='black')
command_name_label.place(x=485, y=370)

try:
    image_label = Image.open("/home/pi/soto_hmi/img/games.png")
except:
    image_label = Image.open("img/games.png")

image_label = image_label.resize((78,80))

render = ImageTk.PhotoImage(image_label)

command_label = Label(app, image=render)
command_label.bind("<Button-1>",videoGame)
command_label.configure(background='black')
command_label.image = render
command_label.place(x=470, y=280)
######################################

######################################
command_name_label = Label(app, text="Recordatorios", font=("Helvetica", 12), fg = "white")
command_name_label.configure(anchor="center", background='black')
command_name_label.place(x=635, y=370)

try:
    image_label = Image.open("/home/pi/soto_hmi/img/calendar.png")
except:
    image_label = Image.open("img/calendar.png")

image_label = image_label.resize((80,80))

render = ImageTk.PhotoImage(image_label)

command_label = Label(app, image=render)
command_label.bind("<Button-1>",videoCall)
command_label.configure(background='black')
command_label.image = render
command_label.place(x=650, y=280)
######################################

######################################
command_name_label = Label(app, text="Control de voz", font=("Helvetica", 12), fg = "white")
command_name_label.configure(anchor="center", background='black')
command_name_label.place(x=800, y=370)

try:
    image_label = Image.open("/home/pi/soto_hmi/img/mic.png")
except:
    image_label = Image.open("img/mic.png")

image_label = image_label.resize((60,80))

render = ImageTk.PhotoImage(image_label)

command_label = Label(app, image=render)
command_label.bind("<Button-1>",videoCall)
command_label.configure(background='black')
command_label.image = render
command_label.place(x=820, y=280)
######################################

app.mainloop()

