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

def write(key, delete = False):
    if not delete:
        if selection.get() == 1:
            name.insert('end', key)
        if selection.get() == 2:
            email.insert('end', key)
        if selection.get() == 3:
            phone.insert('end', key)
    else:
        if selection.get() == 1:
            _text = name.get()
            name.delete(0, 'end')
            name.insert(0, _text[:-1])
        if selection.get() == 2:
            _text = email.get()
            email.delete(0, 'end')
            email.insert(0, _text[:-1])
        if selection.get() == 3:
            _text = phone.get()
            phone.delete(0, 'end')
            phone.insert(0, _text[:-1])

x = 535
y = 220

_1 = Button(app, text = "1", height = 1, width = 2, command = lambda : write("1"))
_1.place(x=x, y=y)
x = x+45

_2 = Button(app, text = "2", height = 1, width = 2, command = lambda : write("2"))
_2.place(x=x, y=y)
x = x+45

_3 = Button(app, text = "3", height = 1, width = 2, command = lambda : write("3"))
_3.place(x=x, y=y)
x = x+45

_4 = Button(app, text = "4", height = 1, width = 2, command = lambda : write("4"))
_4.place(x=x, y=y)
x = x+45

_5 = Button(app, text = "5", height = 1, width = 2, command = lambda : write("5"))
_5.place(x=x, y=y)
x = x+45

_6 = Button(app, text = "6", height = 1, width = 2, command = lambda : write("6"))
_6.place(x=x, y=y)
x = x+45

_7 = Button(app, text = "7", height = 1, width = 2, command = lambda : write("7"))
_7.place(x=x, y=y)
x = x+45

_8 = Button(app, text = "8", height = 1, width = 2, command = lambda : write("8"))
_8.place(x=x, y=y)
x = x+45

_9 = Button(app, text = "9", height = 1, width = 2, command = lambda : write("9"))
_9.place(x=x, y=y)
x = x+45

_0 = Button(app, text = "0", height = 1, width = 2, command = lambda : write("0"))
_0.place(x=x, y=y)

x = 515
y = 250
#################################################


Q = Button(app, text = "Q", height = 1, width = 2, command = lambda : write("q"))
Q.place(x=x, y=y)
x = x+45

W = Button(app, text = "W", height = 1, width = 2, command = lambda : write("w"))
W.place(x=x, y=y)
x = x+45

E = Button(app, text = "E", height = 1, width = 2, command = lambda : write("e"))
E.place(x=x, y=y)
x = x+45

R = Button(app, text = "R", height = 1, width = 2, command = lambda : write("r"))
R.place(x=x, y=y)
x = x+45

T = Button(app, text = "T", height = 1, width = 2, command = lambda : write("t"))
T.place(x=x, y=y)
x = x+45

Y = Button(app, text = "Y", height = 1, width = 2, command = lambda : write("y"))
Y.place(x=x, y=y)
x = x+45

U = Button(app, text = "U", height = 1, width = 2, command = lambda : write("u"))
U.place(x=x, y=y)
x = x+45

I = Button(app, text = "I", height = 1, width = 2, command = lambda : write("i"))
I.place(x=x, y=y)
x = x+45

O = Button(app, text = "O", height = 1, width = 2, command = lambda : write("o"))
O.place(x=x, y=y)
x = x+45

P = Button(app, text = "P", height = 1, width = 2, command = lambda : write("p"))
P.place(x=x, y=y)
x = x+45

DEL = Button(app, text = "DEL", height = 1, width = 2, command = lambda : write("DEL", True))
DEL.place(x=x, y=y)
x = x+45

x = 540
y = 280

#####################################################
A = Button(app, text = "A", height = 1, width = 2, command = lambda : write("a"))
A.place(x=x, y=y)
x = x+45

S = Button(app, text = "S", height = 1, width = 2, command = lambda : write("s"))
S.place(x=x, y=y)
x = x+45

D = Button(app, text = "D", height = 1, width = 2, command = lambda : write("d"))
D.place(x=x, y=y)
x = x+45

F = Button(app, text = "F", height = 1, width = 2, command = lambda : write("f"))
F.place(x=x, y=y)
x = x+45

G = Button(app, text = "G", height = 1, width = 2, command = lambda : write("g"))
G.place(x=x, y=y)
x = x+45

H = Button(app, text = "H", height = 1, width = 2, command = lambda : write("h"))
H.place(x=x, y=y)
x = x+45

J = Button(app, text = "J", height = 1, width = 2, command = lambda : write("j"))
J.place(x=x, y=y)
x = x+45

K = Button(app, text = "K", height = 1, width = 2, command = lambda : write("k"))
K.place(x=x, y=y)
x = x+45

L = Button(app, text = "L", height = 1, width = 2, command = lambda : write("l"))
L.place(x=x, y=y)
x = x+45

_N = Button(app, text = "Ñ", height = 1, width = 2, command = lambda : write("ñ"))
_N.place(x=x, y=y)

x = 560
y = 310

##############################################
AT = Button(app, text = "@", height = 1, width = 2, command = lambda : write("@"))
AT.place(x=x, y=y)
x = x+45

Z = Button(app, text = "Z", height = 1, width = 2, command = lambda : write("z"))
Z.place(x=x, y=y)
x = x+45

X = Button(app, text = "X", height = 1, width = 2, command = lambda : write("x"))
X.place(x=x, y=y)
x = x+45

C = Button(app, text = "C", height = 1, width = 2, command = lambda : write("c"))
C.place(x=x, y=y)
x = x+45

V = Button(app, text = "V", height = 1, width = 2, command = lambda : write("v"))
V.place(x=x, y=y)
x = x+45

B = Button(app, text = "B", height = 1, width = 2, command = lambda : write("b"))
B.place(x=x, y=y)
x = x+45

N = Button(app, text = "N", height = 1, width = 2, command = lambda : write("n"))
N.place(x=x, y=y)
x = x+45

M = Button(app, text = "M", height = 1, width = 2, command = lambda : write("m"))
M.place(x=x, y=y)
x = x+45

PT = Button(app, text = ".", height = 1, width = 2, command = lambda : write("."))
PT.place(x=x, y=y)
x = x+45

x = 630
y = 340

#####################################################

UPDASH = Button(app, text = "-", height = 1, width = 2, command = lambda : write("-"))
UPDASH.place(x=x, y=y)
x = x+45

SPACE = Button(app, text = "SPACE", height = 1, width = 20, command = lambda : write(" "))
SPACE.place(x=x, y=y)
x = x+185

LOWDASH = Button(app, text = "_", height = 1, width = 2, command = lambda : write("_"))
LOWDASH.place(x=x, y=y)
x = x+45

#####################################################
selection = IntVar(None, 1)

select_label = Label(app, text = "¿Qué desea modificar?", background = "black", fg = "white")
select_label.place(x=220, y=370)

name_radio = Radiobutton(app, text = "Modificar nombre", width = 20, variable=selection, value=1)
name_radio.place(x=200, y=400)

phone_radio = Radiobutton(app, text = "Modificar teléfono", width = 20, variable=selection, value=3)
phone_radio.place(x=200, y=430)

email_radio = Radiobutton(app, text = "Modificar email", width = 20, variable=selection, value=2)
email_radio.place(x=200, y=460)

###########################################################

save = Button(app, text = "Guardar", height = 1, width = 20, command = lambda : save())
save.place(x=680, y=400)

_exit = Button(app, text = "Salir", height = 1, width = 20, command = lambda : _exit())
_exit.place(x=680, y=430)

app.mainloop()

