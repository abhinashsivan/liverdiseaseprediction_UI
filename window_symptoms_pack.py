import tkinter as tk
from tkinter import *
from tkinter import ttk

global v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17

global lis


def proceed():
    global v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17

    global lis
    lis = []
    # age_feature_value

    # other_feature_value
    lis.append(v1.get())
    lis.append(v2.get)
    lis.append(v3.get)
    lis.append(v4.get)
    lis.append(v5.get)
    lis.append(v6.get)

    lis.append(v7.get)
    lis.append(v8.get)
    lis.append(v9.get)
    lis.append(v10.get)
    lis.append(v12.get)
    lis.append(v13.get)

    lis.append(v14.get)
    lis.append(v15.get)
    lis.append(v16.get)
    lis.append(v17.get)

    print("v1 isssssssssssss")
    print (v1)

    return lis


def open_window_get_symptoms():
    window_symptoms = Toplevel()
    window_symptoms.geometry("1100x840")
    window_symptoms.title("LIVER DISEASE PREDICTION USING ML")

    global v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17

    v1 = tk.IntVar()
    v2 = tk.IntVar()
    v3 = tk.IntVar()
    v4 = tk.IntVar()
    v5 = tk.IntVar()
    v6 = tk.IntVar()
    v7 = tk.IntVar()
    v8 = tk.IntVar()
    v9 = tk.IntVar()
    v10 = tk.IntVar()
    v11 = tk.IntVar()
    v12 = tk.IntVar()
    v13 = tk.IntVar()
    v14 = tk.IntVar()
    v15 = tk.IntVar()
    v16 = tk.IntVar()
    v17 = tk.IntVar()

    text = Label(window_symptoms, text="Kindly enter the patient's details below --", font="times 20", padx=10, pady=5)
    text.pack(fill='x', side="top")

    # first column

    f0 = Frame(window_symptoms)

    text = Label(f0, text="Choose patient's age group -                  ", padx=3, pady=10)
    text.pack()
    combo = ttk.Combobox(f0, values=["age<40", "40<=age<50", "50<=age<60", "60<=age<70", "70<=age<80", "80<=age<90",
                                     "age>90"], width=20)
    combo.pack(pady=16)

    tk.Label(f0,
             text="""Select the patient's Gender                    """, padx=20).pack(pady=10)

    tk.Radiobutton(f0, text="   MALE  ", padx=20, variable=v1, value=1).pack()

    tk.Radiobutton(f0, text="FEMALE ", padx=20, variable=v1, value=2).pack()

    tk.Label(f0,
             text="""Does the patient suffer from Jaundice ?""", padx=20).pack(pady=10)

    tk.Radiobutton(f0, text="YES", padx=20, variable=v2, value=1).pack()

    tk.Radiobutton(f0, text="NO ", padx=20, variable=v2, value=2).pack()

    tk.Label(f0,
             text="""Does the patient  suffer from Acitis ?""", padx=20).pack(pady=10)

    tk.Radiobutton(f0, text="YES", padx=20, variable=v3, value=1).pack()

    tk.Radiobutton(f0, text="NO ", padx=20, variable=v3, value=2).pack()
    f0.pack(pady=13)

    tk.Label(f0,
             text="""Does the patient suffer from Hepatic \nEncephalopathy ?""", padx=20).pack(pady=10)

    tk.Radiobutton(f0, text="YES", padx=20, variable=v4, value=1).pack()

    tk.Radiobutton(f0, text="NO ", padx=20, variable=v4, value=2).pack()
    f0.pack()

    tk.Label(f0,
             text="""Does the patient suffer from Fever ?""", padx=20).pack(pady=10)

    tk.Radiobutton(f0, text="YES", padx=20, variable=v5, value=1).pack()

    tk.Radiobutton(f0, text="NO ", padx=20, variable=v5, value=2).pack()
    f0.pack(anchor=tk.W, side="left")

    # second_column

    f0 = Frame(window_symptoms)

    tk.Label(f0,
             text="""Does the patient suffer from Jaundice ?""", padx=20).pack(pady=10)

    tk.Radiobutton(f0, text="YES", padx=20, variable=v2, value=1).pack()

    tk.Radiobutton(f0, text="NO ", padx=20, variable=v2, value=2).pack()

    tk.Label(f0,
             text="""Select the patient's Gender                    """, padx=20).pack(pady=10)

    tk.Radiobutton(f0, text="   MALE  ", padx=20, variable=v1, value=1).pack()

    tk.Radiobutton(f0, text="FEMALE ", padx=20, variable=v1, value=2).pack()

    tk.Label(f0,
             text="""Does the patient suffer from Jaundice ?""", padx=20).pack(pady=10)

    tk.Radiobutton(f0, text="YES", padx=20, variable=v2, value=1).pack()

    tk.Radiobutton(f0, text="NO ", padx=20, variable=v2, value=2).pack()

    tk.Label(f0,
             text="""Does the patient  suffer from Acitis ?""", padx=20).pack(pady=10)

    tk.Radiobutton(f0, text="YES", padx=20, variable=v3, value=1).pack()

    tk.Radiobutton(f0, text="NO ", padx=20, variable=v3, value=2).pack()
    f0.pack(pady=13)

    tk.Label(f0,
             text="""Does the patient suffer from Hepatic \nEncephalopathy ?""", padx=20).pack(pady=10)

    tk.Radiobutton(f0, text="YES", padx=20, variable=v4, value=1).pack()

    tk.Radiobutton(f0, text="NO ", padx=20, variable=v4, value=2).pack()
    f0.pack()

    tk.Label(f0,
             text="""Does the patient suffer from Fever ?""", padx=20).pack(pady=10)

    tk.Radiobutton(f0, text="YES", padx=20, variable=v5, value=1).pack()

    tk.Radiobutton(f0, text="NO ", padx=20, variable=v5, value=2).pack()
    f0.pack(anchor=tk.W, side="left")

    # third_col

    f0 = Frame(window_symptoms)

    tk.Label(f0,
             text="""Does the patient suffer from Jaundice ?""", padx=20).pack(pady=10)

    tk.Radiobutton(f0, text="YES", padx=20, variable=v2, value=1).pack()

    tk.Radiobutton(f0, text="NO ", padx=20, variable=v2, value=2).pack()

    tk.Label(f0,
             text="""Select the patient's Gender                    """, padx=20).pack(pady=10)

    tk.Radiobutton(f0, text="   MALE  ", padx=20, variable=v1, value=1).pack()

    tk.Radiobutton(f0, text="FEMALE ", padx=20, variable=v1, value=2).pack()

    tk.Label(f0,
             text="""Does the patient suffer from Jaundice ?""", padx=20).pack(pady=10)

    tk.Radiobutton(f0, text="YES", padx=20, variable=v2, value=1).pack()

    tk.Radiobutton(f0, text="NO ", padx=20, variable=v2, value=2).pack()

    tk.Label(f0,
             text="""Does the patient  suffer from Acitis ?""", padx=20).pack(pady=10)

    tk.Radiobutton(f0, text="YES", padx=20, variable=v3, value=1).pack()

    tk.Radiobutton(f0, text="NO ", padx=20, variable=v3, value=2).pack()
    f0.pack(pady=13)

    tk.Label(f0,
             text="""Does the patient suffer from Hepatic \nEncephalopathy ?""", padx=20).pack(pady=10)

    tk.Radiobutton(f0, text="YES", padx=20, variable=v4, value=1).pack()

    tk.Radiobutton(f0, text="NO ", padx=20, variable=v4, value=2).pack()
    f0.pack()

    tk.Label(f0,
             text="""Does the patient suffer from Fever ?""", padx=20).pack(pady=10)

    tk.Radiobutton(f0, text="YES", padx=20, variable=v5, value=1).pack()

    tk.Radiobutton(f0, text="NO ", padx=20, variable=v5, value=2).pack()
    f0.pack(anchor=tk.W, side="left")

    f1 = Frame(window_symptoms)

    button_confirm = Button(f1, text="CONFIRM", font="times 20", padx=40, pady=20, command=proceed)
    button_confirm.pack(fill="x", pady=200)

    button_back = Button(f1, text="BACK", font="times 20", padx=40, pady=20, command=lambda : window_symptoms.destroy())
    button_back.pack(fill="x")

    f1.pack(anchor=tk.E)

    window_symptoms.mainloop()

    return lis


open_window_get_symptoms()
