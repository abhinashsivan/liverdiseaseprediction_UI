import tkinter as tk
from tkinter import *
from tkinter import ttk

global v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17

def proceed():
    global v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17

    print(v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17)

    return



def open_window_get_symptoms():

    window_symptoms = Tk()
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
    text.grid(row=0, columnspan=4, sticky=W)


    #first column

    f0=Frame(window_symptoms)
    text = Label(f0, text="Choose patient's age group -", padx=3, pady=5)
    text.grid(row=0,column=0)
    combo = ttk.Combobox(f0, values=["age<40", "40<=age<50", "50<=age<60", "60<=age<70", "70<=age<80", "80<=age<90",
                                     "age>90"], width=20)
    combo.grid(row=1, column=0)
    f0.grid(row=1, column=0, pady=5, sticky=W)

    f1=Frame(window_symptoms)
    tk.Label(f1,
             text="""Select the patient's Gender""",padx=20).grid(row=0, column=0)

    tk.Radiobutton(f1,text="MALE  ",padx=20,variable=v1,value=1).grid(row=1, column=0, sticky=W)

    tk.Radiobutton(f1, text="FEMALE ", padx=20, variable=v1, value=2).grid(row=2, column=0, sticky=W)
    f1.grid(row=2, column=0, pady=13, sticky=W)

    f2=Frame(window_symptoms)
    tk.Label(f2,
             text="""Does the patient suffer from Jaundice ?""", padx=20).grid(row=1, column=0)

    tk.Radiobutton(f2, text="YES", padx=20, variable=v2, value=1).grid(row=2, column=0, sticky=W)

    tk.Radiobutton(f2, text="NO ", padx=20, variable=v2, value=2).grid(row=3, column=0, sticky=W)
    f2.grid(row=3, column=0, pady=13, sticky=W)

    f3 = Frame(window_symptoms)
    tk.Label(f3,
             text="""Does the patient  suffer from Acitis ?""", padx=20).grid(row=0, column=0)

    tk.Radiobutton(f3, text="YES", padx=20, variable=v3, value=1).grid(row=1, column=0, sticky=W)

    tk.Radiobutton(f3, text="NO ", padx=20, variable=v3, value=2).grid(row=2, column=0, sticky=W)
    f3.grid(row=4, column=0, pady=13, sticky=W)

    f4 = Frame(window_symptoms)
    tk.Label(f4,
             text="""Does the patient suffer from Hepatic \nEncephalopathy ?""", padx=20).grid(row=0, column=0)

    tk.Radiobutton(f4, text="YES", padx=20, variable=v4, value=1).grid(row=1, column=0, sticky=W)

    tk.Radiobutton(f4, text="NO ", padx=20, variable=v4, value=2).grid(row=2, column=0, sticky=W)
    f4.grid(row=5, column=0, pady=13, sticky=W)

    f5 = Frame(window_symptoms)
    tk.Label(f5,
             text="""Does the patient suffer from Fever ?""", padx=20).grid(row=0, column=0)

    tk.Radiobutton(f5, text="YES", padx=20, variable=v5, value=1).grid(row=1, column=0, sticky=W)

    tk.Radiobutton(f5, text="NO ", padx=20, variable=v5, value=2).grid(row=2, column=0, sticky=W)
    f5.grid(row=6, column=0, pady=13, sticky=W)

    #second_column

    f_ = Frame(window_symptoms)
    f6 = Frame(f_)
    tk.Label(f6,
             text="""Does the patient show signs of physical weakness ?""", padx=20).grid(row=0, column=0)

    tk.Radiobutton(f6, text="YES", padx=20, variable=v6, value=1).grid(row=1, column=0, sticky=W)

    tk.Radiobutton(f6, text="NO ", padx=20, variable=v6, value=2).grid(row=2, column=0, sticky=W)
    f6.grid(sticky=W)
    f_.grid(row=1, column=1, pady=28, sticky=W)

    f7 = Frame(window_symptoms)
    tk.Label(f7,
             text="""Are there any symbols of drawsiness in patient ?""", padx=20).grid(row=0, column=0)

    tk.Radiobutton(f7, text="YES", padx=20, variable=v7, value=1).grid(row=1, column=0, sticky=W)

    tk.Radiobutton(f7, text="NO ", padx=20, variable=v7, value=2).grid(row=2, column=0, sticky=W)
    f7.grid(row=2, column=1, pady=10, sticky=W)


    f8 = Frame(window_symptoms)
    tk.Label(f8,
             text="""Does the patient suffer from Nausea ?""", padx=20).grid(row=0, column=0)

    tk.Radiobutton(f8, text="YES", padx=20, variable=v8, value=1).grid(row=1, column=0, sticky=W)

    tk.Radiobutton(f8, text="NO ", padx=20, variable=v8, value=2).grid(row=2, column=0, sticky=W)
    f8.grid(row=3, column=1, pady=10, sticky=W)

    f9 = Frame(window_symptoms)
    tk.Label(f9,
             text="""Does the patient have the condition of Hypertension ?""", padx=20).grid(row=0, column=0)

    tk.Radiobutton(f9, text="YES", padx=20, variable=v9, value=1).grid(row=1, column=0, sticky=W)

    tk.Radiobutton(f9, text="NO ", padx=20, variable=v9, value=2).grid(row=2, column=0, sticky=W)
    f9.grid(row=4, column=1, pady=10, sticky=W)

    f10 = Frame(window_symptoms)
    tk.Label(f10,
             text="""Does the patient suffer from Abdominal Distension ?""", padx=20).grid(row=0, column=0)

    tk.Radiobutton(f10, text="YES", padx=20, variable=v10, value=1).grid(row=1, column=0, sticky=W)

    tk.Radiobutton(f10, text="NO ", padx=20, variable=v10, value=2).grid(row=2, column=0, sticky=W)
    f10.grid(row=5, column=1, pady=10, sticky=W)

    f11 = Frame(window_symptoms)
    tk.Label(f11,
             text="""Is there decreased urine secretion recently ?""", padx=20).grid(row=0, column=0)

    tk.Radiobutton(f11, text="YES", padx=20, variable=v11, value=1).grid(row=1, column=0, sticky=W)

    tk.Radiobutton(f11, text="NO ", padx=20, variable=v11, value=2).grid(row=2, column=0, sticky=W)
    f11.grid(row=6, column=1, pady=10, sticky=W)


    #third_column

    f12 = Frame(window_symptoms)
    tk.Label(f12,
             text="""Is there symptoms of Altered Sensorium ?""", padx=20).grid(row=0, column=0)

    tk.Radiobutton(f12, text="YES", padx=20, variable=v12, value=1).grid(row=1, column=0, sticky=W)

    tk.Radiobutton(f12, text="NO ", padx=20, variable=v12, value=2).grid(row=2, column=0, sticky=W)
    f12.grid(row=1, column=3, pady=10, sticky=W)

    f13 = Frame(window_symptoms)
    tk.Label(f13,
             text="""Is there any abdominal pain ?""", padx=20).grid(row=0, column=0)

    tk.Radiobutton(f13, text="YES", padx=20, variable=v13, value=1).grid(row=1, column=0, sticky=W)

    tk.Radiobutton(f13, text="NO ", padx=20, variable=v13, value=2).grid(row=2, column=0, sticky=W)
    f13.grid(row=2, column=3, pady=10, sticky=W)

    f14 = Frame(window_symptoms)
    tk.Label(f14,
             text="""Does the patient suffer from Breathlessness ?""", padx=20).grid(row=0, column=0)

    tk.Radiobutton(f14, text="YES", padx=20, variable=v14, value=1).grid(row=1, column=0, sticky=W)

    tk.Radiobutton(f14, text="NO ", padx=20, variable=v14, value=2).grid(row=2, column=0, sticky=W)
    f14.grid(row=3, column=3, pady=10, sticky=W)

    f15 = Frame(window_symptoms)
    tk.Label(f15,
             text="""Does the patient suffer from Cough ?""", padx=20).grid(row=0, column=0)

    tk.Radiobutton(f15, text="YES", padx=20, variable=v15, value=1).grid(row=1, column=0, sticky=W)

    tk.Radiobutton(f15, text="NO ", padx=20, variable=v15, value=2).grid(row=2, column=0, sticky=W)
    f15.grid(row=4, column=3, pady=10, sticky=W)


    f16 = Frame(window_symptoms)
    tk.Label(f16,
             text="""Does the patient suffer from  Gastrointestinal(GI) \nbleeding?""", padx=20).grid(row=0, column=0, sticky=W)

    tk.Radiobutton(f16, text="YES", padx=20, variable=v16, value=1).grid(row=1, column=0, sticky=W)

    tk.Radiobutton(f16, text="NO ", padx=20, variable=v16, value=2).grid(row=2, column=0, sticky=W)
    f16.grid(row=5, column=3, pady=10, sticky=W)

    f17 = Frame(window_symptoms)
    tk.Label(f17,
              text="""Is there Leg swelling?""", padx=20).grid(row=0, column=0, sticky=W)

    tk.Radiobutton(f17, text="YES", padx=20, variable=v17, value=1).grid(row=1, column=0, sticky=W)

    tk.Radiobutton(f17, text="NO ", padx=20, variable=v17, value=2).grid(row=2, column=0, sticky=W)
    f17.grid(row=6, column=3, pady=10, sticky=W)

    button_proceed = Button(window_symptoms, text="PROCEED", font="times 20", command=proceed)
    button_proceed.grid(row=1, column=4, rowspan=6)





    window_symptoms.mainloop()






open_window_get_symptoms()

