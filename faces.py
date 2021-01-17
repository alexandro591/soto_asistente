import subprocess
import sys
from tkinter import *
from PIL import Image, ImageTk
from os import path

W = 300
H = 180

root = Tk()
root.title("Soto asistente")
root.geometry(str(W)+'x'+str(H)+"+360+150")
root.attributes("-topmost", True)
try:
    img = ImageTk.PhotoImage(Image.open("faces/"+sys.argv[1]+".png").resize((W, H), Image.ANTIALIAS))
except:
    img = ImageTk.PhotoImage(Image.open("/home/pi/soto_hmi/faces/"+sys.argv[1]+".png").resize((W, H), Image.ANTIALIAS))

panel = Label(root, image = img)
panel.pack()
root.mainloop()