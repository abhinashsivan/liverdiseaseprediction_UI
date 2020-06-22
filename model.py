from Tkinter import  *
import tkinter as tk
import pickle
import numpy as np
import pandas as pd

global screen1
global screen2

def get_prediction():

    f = open("cache.txt", "r")
    feature_list = f.read()
    f.close()
    feature_list = eval(feature_list)

    array = np.array(feature_list).reshape(18 * 1)
    array = np.mat(array)
    x = pd.DataFrame(array)

    with open('model/k.pkl', 'rb') as file:
        model = pickle.load(file)

    result = model.predict(x)

    print("final result")
    print(result[0])

    global screen2

    screen2.insert(INSERT, "The predicted disease is \n\n")
    screen2.insert(INSERT, "\t"+result[0])

    return

def show_feature():

    global screen1

    screen1.delete('1.0', END)

    f = open("cache.txt", "r")
    feature_list = f.read()
    f.close()

    text=feature_list.replace(" ", "       ")

    print (type(feature_list))

    screen1.insert(INSERT, "The features and their values are as below\n\n")
    screen1.insert(INSERT, "Age,Gender,Jaundice,Acitis,Hepatic Encephalopathy,Fever,Weakness,Drawsiness,Nausea,Hypertension,Abdominal Distension,Decreased urine o/p,Altered Sensorium,Abdominal pain,Breathlessness,Cough,GI bleed,Leg swelling(pedel oedema)")
    screen1.insert(INSERT,"\n\n"+text)

    return



def open_window_model():
    window_model = Toplevel()
    window_model.geometry("1100x840")
    window_model.title("LIVER DISEASE PREDICTION USING ML")
    window_model.config(bg="#ffffff")

    Heading = Label(window_model, text="LIVER DISEASE PREDICTION USING MACHINE LEARNING", font="Cooper 30", bg="#ffffff",
                    padx=10)
    Heading.pack(fill='x', pady=50)


    f1 = Frame(window_model, bg="#ffffff")

    button_show_feature = Button(f1, text="SHOW FEATURE", width=20, font="times 20", padx=40, pady=20,
                           command=show_feature)
    button_show_feature.pack()

    global  screen1
    screen1 = Text(f1, height=10, bg="#ccccff")
    screen1.pack(fill="x")

    f1.pack(fill="x")

    f2 = Frame(window_model, bg="#ffffff")

    button_get_prediction = Button(f2, text="PREDICT", width=20, font="times 20", padx=40, pady=20,
                                 command=get_prediction)
    button_get_prediction.pack()

    global screen2
    screen2 = Text(f2, height=10, bg="#ccccff")
    screen2.pack(fill="x")
    screen2.configure(font=("Courier", 18,"bold", "italic"))

    f2.pack(fill="x")

    button_back = Button(window_model, text="BACK", width=20, font="times 20", padx=40, pady=20,
                                   command=lambda : window_model.destroy())
    button_back.pack(side="right")
    window_model.mainloop()

    return