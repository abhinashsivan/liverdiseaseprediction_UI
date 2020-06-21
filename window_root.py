'''
this is a ui for liver disease prediction ML project.
made by abhinash sivan.

'''

from PIL import Image, ImageTk
import PIL.Image
from Tkinter import *
from tkinter import ttk
from window_symptoms import open_window_get_symptoms

global l1

def get_symptoms():

    lis = open_window_get_symptoms()
    global l1
    l1=[]
    l1=lis.copy()
    return

def model():
    pass
def open_window_about():
    pass

#splash_window

# splash_window = Tk()
# splash_window.geometry("1100x840")
# splash_window.title("LIVER DISEASE PREDICTION USING ML")
# img = ImageTk.PhotoImage(PIL.Image.open('UI-Materials/SD.png'))
# panel = Label(splash_window, image=img)
# panel.pack(side="top", fill="both", expand="yes")
# splash_window.after(3000, lambda: splash_window.destroy())
# splash_window.mainloop()


#root_window

root = Tk()
global i
root.geometry("1100x840")
root.title("LIVER DISEASE PREDICTION USING ML")

Heading = Label(root, text="LIVER DISEASE PREDICTION USING MACHINE LEARNING", font="Cooper 30", padx=10)
Heading.grid(row=0, column=0, columnspan=2, padx=20, pady=15)


MainFrame = Frame(root, padx=40, pady=60)

Frame1 = Frame(MainFrame)

button_record = Button(Frame1, text="ENTER SYMPTOMS", width=20,font="times 20", padx=40, pady=20, command=get_symptoms)
button_record.grid(row=1,column=0,pady=20)
button_process = Button(Frame1, text="PREDICT", width=20, font="times 20", padx=40, pady=20, command=model)
button_process.grid(row=2,column=0 , pady=20)
button_recognise = Button(Frame1, text="ABOUT", width=20, font="times 20", padx=40, pady=20, command=open_window_about)
button_recognise.grid(row=3,column=0 , pady=20)

Frame1.grid(row=1,column=0 )

MainFrame.grid(row=1,column=0 )

liver_img = ImageTk.PhotoImage(PIL.Image.open('UI-Materials/l.jpg'))
panel = Label(root, image=liver_img)
panel.grid(row=1, column=3)


root.mainloop()

