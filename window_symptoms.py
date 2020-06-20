import tkinter as tk
from tkinter import *
from tkinter import ttk


def open_window_get_symptoms():

    window_symptoms = Tk()
    window_symptoms.geometry("1100x650")
    window_symptoms.title("LIVER DISEASE PREDICTION USING ML")
    v1 = tk.IntVar()
    v2 = tk.IntVar()

    f0=Frame(window_symptoms)
    text = Label(f0, text="- choose patient's age group -", padx=10, pady=5)
    text.grid(row=0,column=0)
    combo = ttk.Combobox(f0, values=[" <40 ", "40<=age<50"], width=10)
    combo.grid(row=1, column=0)
    f0.grid(row=0, column=0, pady=10)

    f1=Frame(window_symptoms)
    tk.Label(f1,
             text="""Select Gender""",padx=20).grid(row=0, column=0)

    tk.Radiobutton(f1,text="MALE  ",padx=20,variable=v1,value=1).grid(row=1, column=0, sticky=W)

    tk.Radiobutton(f1, text="FEMALE ", padx=20, variable=v1, value=2).grid(row=2, column=0, sticky=W)
    f1.grid(row=1, column=0, pady=10)

    f2=Frame(window_symptoms)
    tk.Label(f2,
             text="""SAY YES/ NO""", padx=20).grid(row=1, column=0)

    tk.Radiobutton(f2, text="YES", padx=20, variable=v2, value=1).grid(row=2, column=0, sticky=W)

    tk.Radiobutton(f2, text="NO ", padx=20, variable=v2, value=2).grid(row=3, column=0, sticky=W)
    f2.grid(row=2, column=0, pady=10)

    window_symptoms.mainloop()






open_window_get_symptoms()

