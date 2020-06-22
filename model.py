import pickle
import numpy as np
import pandas as pd
from array import *

def open_window_model():

    f = open("filename.txt", "r")
    feature_list = f.read()
    f.close()
    feature_list = eval(feature_list)

    array = np.array(feature_list).reshape(18 * 1)
    array = np.mat(array)
    x = pd.DataFrame(array)

    with open('model/k.pkl', 'rb') as file:
        model = pickle.load(file)

    re = model.predict(x)

    print("final result")
    print(re[0])





    return