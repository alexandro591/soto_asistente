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

render = ImageTk.PhotoImage(logo)

logo_label = Label(app, image=render)
logo_label.configure(background='black')
logo_label.image = render
logo_label.place(x=W/2-55, y=80)

######################################
entry_name = Label(app, text="Nombre", font=("Helvetica", 12), fg = "white")
entry_name.configure(anchor="center", background='black')
entry_name.place(x=200, y=200)

name = Entry(app)
name.place(x=200, y=220)
######################################

######################################
entry_name = Label(app, text="Teléfono", font=("Helvetica", 12), fg = "white")
entry_name.configure(anchor="center", background='black')
entry_name.place(x=200, y=250)

phone = Entry(app)
phone.place(x=200, y=270)
######################################

######################################
entry_name = Label(app, text="Correo", font=("Helvetica", 12), fg = "white")
entry_name.configure(anchor="center", background='black')
entry_name.place(x=200, y=300)

email = Entry(app)
email.place(x=200, y=320)
######################################

###################################### TECLADO ####################################

x = 550
y = 220

Q = Button(app, text = "Q", height = 1, width = 2)
Q.place(x=x, y=y)
x = x+45

W = Button(app, text = "W", height = 1, width = 2)
W.place(x=x, y=y)
x = x+45

E = Button(app, text = "E", height = 1, width = 2)
E.place(x=x, y=y)
x = x+45

R = Button(app, text = "R", height = 1, width = 2)
R.place(x=x, y=y)
x = x+45

T = Button(app, text = "T", height = 1, width = 2)
T.place(x=x, y=y)
x = x+45

Y = Button(app, text = "Y", height = 1, width = 2)
Y.place(x=x, y=y)
x = x+45

U = Button(app, text = "U", height = 1, width = 2)
U.place(x=x, y=y)
x = x+45

I = Button(app, text = "I", height = 1, width = 2)
I.place(x=x, y=y)
x = x+45

O = Button(app, text = "O", height = 1, width = 2)
O.place(x=x, y=y)
x = x+45

P = Button(app, text = "P", height = 1, width = 2)
P.place(x=x, y=y)

x = 550
y = 250

#####################################################
A = Button(app, text = "A", height = 1, width = 2)
A.place(x=x, y=y)
x = x+45

S = Button(app, text = "S", height = 1, width = 2)
S.place(x=x, y=y)
x = x+45

D = Button(app, text = "D", height = 1, width = 2)
D.place(x=x, y=y)
x = x+45

F = Button(app, text = "F", height = 1, width = 2)
F.place(x=x, y=y)
x = x+45

G = Button(app, text = "G", height = 1, width = 2)
G.place(x=x, y=y)
x = x+45

H = Button(app, text = "H", height = 1, width = 2)
H.place(x=x, y=y)
x = x+45

J = Button(app, text = "J", height = 1, width = 2)
J.place(x=x, y=y)
x = x+45

K = Button(app, text = "K", height = 1, width = 2)
K.place(x=x, y=y)
x = x+45

L = Button(app, text = "L", height = 1, width = 2)
L.place(x=x, y=y)
x = x+45

_N = Button(app, text = "Ñ", height = 1, width = 2)
_N.place(x=x, y=y)

x = 620
y = 280

##############################################
Z = Button(app, text = "Z", height = 1, width = 2)
Z.place(x=x, y=y)
x = x+45

X = Button(app, text = "X", height = 1, width = 2)
X.place(x=x, y=y)
x = x+45

C = Button(app, text = "C", height = 1, width = 2)
C.place(x=x, y=y)
x = x+45

V = Button(app, text = "V", height = 1, width = 2)
V.place(x=x, y=y)
x = x+45

B = Button(app, text = "B", height = 1, width = 2)
B.place(x=x, y=y)
x = x+45

N = Button(app, text = "N", height = 1, width = 2)
N.place(x=x, y=y)
x = x+45

M = Button(app, text = "M", height = 1, width = 2)
M.place(x=x, y=y)
x = x+45

app.mainloop()

