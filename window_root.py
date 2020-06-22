'''
this is a ui for liver disease prediction ML project.
made by abhinash sivan.

'''

from PIL import Image, ImageTk
import PIL.Image
from window_about import open_window_about
from bar import  bar
import tkMessageBox
from Tkinter import *
from tkinter import ttk
from window_symptoms import open_window_get_symptoms
from model import open_window_model

global feature_list


def get_symptoms():

    open_window_get_symptoms()

    return


def model():

    open_window_model()
    return


def open_about():
    open_window_about()

    return


# splash_window

splash_window = Tk()
splash_window.geometry("1240x590")
splash_window.title("LIVER DISEASE PREDICTION USING ML")
img = ImageTk.PhotoImage(PIL.Image.open('UI-Materials/sd2.png'))
panel = Label(splash_window, image=img)
panel.pack(side="top", fill="both", expand="yes")
splash_window.after(3000, lambda: splash_window.destroy())

progress = ttk.Progressbar(splash_window, orient=HORIZONTAL, length=1280, mode='determinate')
progress.pack(ipady=45)
bar(progress, splash_window)

splash_window.mainloop()


# root_window

root = Tk()
global i
root.geometry("1100x840")
root.title("LIVER DISEASE PREDICTION USING ML")
root.config(bg="#ffffff")

Heading = Label(root, text="LIVER DISEASE PREDICTION USING MACHINE LEARNING", font="Cooper 30", bg="#ffffff", padx=10)
Heading.pack(fill='x', pady=10)

MainFrame = Frame(root, padx=40, pady=60, bg="#ffffff")

Frame1 = Frame(MainFrame, bg="#ffffff")

button_record = Button(Frame1, text="ENTER SYMPTOMS", width=20, font="times 20", padx=40, pady=20, command=get_symptoms)
button_record.pack(pady=20)
button_process = Button(Frame1, text="PREDICT", width=20, font="times 20", padx=40, pady=20, command=model)
button_process.pack(pady=20)
button_recognise = Button(Frame1, text="ABOUT", width=20, font="times 20", padx=40, pady=20, command=open_about)
button_recognise.pack(pady=20)

Frame1.pack()

MainFrame.pack(side="left")

liver_img = ImageTk.PhotoImage(PIL.Image.open('UI-Materials/l.jpg'))
panel = Label(root, image=liver_img, borderwidth=0, highlightthickness=0)
panel.pack(side="right")

root.mainloop()
