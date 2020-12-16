import subprocess
from tkinter import *
from PIL import Image, ImageTk
from os import path

W = 300
H = 180

root = Tk()
try:
    img = ImageTk.PhotoImage(Image.open("faces/normal.png").resize((W, H), Image.ANTIALIAS))
except:
    img = ImageTk.PhotoImage(Image.open("/home/pi/soto_hmi/faces/normal.png").resize((W, H), Image.ANTIALIAS))

panel = Label(root, image = img)
panel.pack()
root.mainloop()