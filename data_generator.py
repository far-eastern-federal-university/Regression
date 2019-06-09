# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 10:59:33 2019

@author: dv.zhilenkov
"""

def spoiler(f, x, params, mess):
    res = x + np.random.normal(loc=params[0], scale=params[1], size=(len(x), )) + 5*np.array(f(x))
    return res

import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt

if __name__ == "__main__":
    np.random.seed(124)
    x = np.linspace(-10*np.pi, 10*np.pi, 20)
    params = [0, 3]
    mn = 0.4
    mess = [0.6 - (np.random.rand()*mn - mn/2) for i in range(len(x))]
    mess = np.array(mess)
    
#    print(mess*x)
    y = spoiler(np.sin, x, params, mess)
    
    plt.figure()
    plt.title("spoiled sin")
    plt.plot(x, y)
    plt.show()
    
    data = np.array([x, y])
    data = data.transpose()
    
    with open("data_nonlinear.csv", mode='w') as dat:
        dat_w = csv.writer(dat, delimiter=',')
        
        for r in data:
            dat_w.writerow(r)
            
            
    data = pd.read_csv("data_nonlinear.csv", delimiter=',')
    
    print(data)