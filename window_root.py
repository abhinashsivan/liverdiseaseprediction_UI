'''
this is a ui for liver disease prediction ML project.

'''

from PIL import Image, ImageTk
import PIL.Image
from Tkinter import *
from tkinter import ttk

splash_window = Tk()
splash_window.geometry("1100x650")
splash_window.title("LIVER DISEASE PREDICTION USING ML")
img = ImageTk.PhotoImage(PIL.Image.open('UI-Materials/SD.png'))
panel = Label(splash_window, image=img)
panel.pack(side="top", fill="both", expand="yes")
splash_window.after(3000, lambda: splash_window.destroy())
splash_window.mainloop()

root = Tk()
global i
root.geometry("1100x650")
root.resizable(0, 0)
root.title("LIVER DISEASE PREDICTION USING ML")

MainFrame = Frame(root, bg="#6699cc", padx=40, pady=60)
MainFrame.pack(fill="both", expand=True)

Heading = Label(MainFrame, text="LIVER DISEASE PREDICTION USING MACHINE LEARNING", bg="#6699cc", font="Cooper", padx=10, pady=10)
Heading.pack()

Frame1 = Frame(MainFrame, bg="#6699cc")


def get_symotoms(args):
    pass
def model():
    pass
def open_window_about():
    pass


button_record = Button(Frame1, text=" ENTER SYMPTOMS", font="times 20", padx=40, pady=20, bg="#3d7ab6", command=get_symotoms)
button_record.pack(fill="x", pady=20)
button_process = Button(Frame1, text=" PREDICT ", font="times 20", padx=40, pady=20, bg="#3d7ab6",
                        command=model)
button_process.pack(fill="x", pady=20)
button_recognise = Button(Frame1, text=" ABOUT ", font="times 20", padx=40, pady=20, bg="#3d7ab6", command=open_window_about)
button_recognise.pack(fill="x", pady=20)

Frame1.pack(fill="x")


root.mainloop()
