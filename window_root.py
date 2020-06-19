'''
this is a ui for liver disease prediction ML project.

'''

from PIL import Image, ImageTk
import PIL.Image
from Tkinter import *
from tkinter import ttk
from bar import bar

splash_window = Tk()
splash_window.geometry("1100x650")
splash_window.title("LIVER DISEASE PREDICTION USING ML")
img = ImageTk.PhotoImage(PIL.Image.open('SD.png'))
panel = Label(splash_window, image=img)
panel.pack(side="top", fill="both", expand="yes")
splash_window.after(3000, lambda: splash_window.destroy())
progress = ttk.Progressbar(splash_window, orient=HORIZONTAL, length=1100, mode='determinate')
progress.pack()
bar(progress, splash_window)
splash_window.mainloop()
