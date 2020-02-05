from tkinter import *
from PIL import ImageTk, Image
import time
import webbrowser
import os

# import random

what = 0

mainhub = Tk()
mainhub.title('OuiCareMemeCare')

pf = Frame(mainhub, height=-1200)
pf.grid()

img = ImageTk.PhotoImage(Image.open("simple.png"))
img2 = ImageTk.PhotoImage(Image.open("simple2.png"))

image_list = [img, img2]

labeling = Label(image=img)
labeling.grid(row=0, column=0, columnspan=4)


def goodies():
    return


def goodTimes():
    return


def badTimes():
    return


def openNew1():
    return


def openNew2():
    return


def openNew3():
    return


def windowOpen():
    return


def openNew5():
    return


goodVibes = Button(mainhub, text="I'm Feeling Happy", command=openNew1)
badVibes = Button(mainhub, text="I'm Feeling Sad", command=openNew2)
idcVibes = Button(mainhub, text="I don't care about feeling. I'm in it for the goodies.", command=openNew3)
exitButton = Button(mainhub, text="Don't press me.", command=lambda:[windowOpen(), mainhub.quit()])

goodVibes.grid(row=1, column=1)
badVibes.grid(row=1, column=2)
idcVibes.grid(row=1, column=0)
exitButton.grid(row=1, column=3)

mainhub.mainloop()
