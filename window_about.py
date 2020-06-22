from Tkinter import *
from tkdocviewer import *

def open_window_about():

    window_about=Toplevel()
    window_about.geometry("820x600")
    window_about.title("about")
    v=DocViewer(window_about)
    v.pack(side="top",expand=1,fill="both")

    v.display_file("UI-Materials/about.pdf")

    button_quit = Button(window_about, text="EXIT", command= lambda :window_about.destroy())

    button_quit.pack(side="bottom")

    window_about.mainloop()
