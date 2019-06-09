# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 10:59:33 2019

@author: dv.zhilenkov
"""

import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import itertools as it

def trend(x, a, b):
    return np.dot(a, x) + b

def sintrend(x, a, b, c, d):
    return np.dot(a, x) + b*np.sin(c*x) + d

def spoiler(f, params):
    return np.random.normal(loc=params[0], scale=params[1], size=f.shape) + f

def plot_and_write(x, y, plotname, filename):
    plt.figure()
    plt.title(plotname)
    plt.plot(x, y)
    plt.show()
    
    data = np.array([x, y])
    data = data.transpose()
    
    with open(filename, mode='w', newline='') as dat:
        dat_w = csv.writer(dat, delimiter=',')
        
        for r in data:
            dat_w.writerow(r)

if __name__ == "__main__":
    np.random.seed(242)
    x = np.linspace(-10*np.pi, 10*np.pi, 200)
    params = [0, 3]
        
    y = spoiler(sintrend(x, 1, 10, 1, 0), params)
    
    filename = "data_nonlinear.csv"
    plotname = "spoiled sin"
    
    plot_and_write(x, y, plotname, filename)
            
    data = pd.read_csv("data_nonlinear.csv", delimiter=',', header=None)
    data.plot.scatter(x=0, y=1)
    
    params = [0, 6]
    
    y = spoiler(trend(x, 1, 0), params)
    
    filename = "data_linear.csv"
    plotname = "spoiled linear function"
    
    plot_and_write(x, y, plotname, filename)
    
    data = pd.read_csv(filename, delimiter=',', header=None)
    data.plot.scatter(x=0, y=1)
    
    x = np.linspace(-10*np.pi, 10*np.pi, 10)
    
    y = [i for i in x]
    
    data3d = []
    
    for i in it.product(x, y):
        data3d.append([i[0], i[1], spoiler(trend([i[0], i[1]], [1, -1], 0), params)])
    
    filename = "data3d_linear.csv"
    plotname = "spoiled linear 3d function"
    
    with open(filename, mode='w', newline='') as dat:
        dat_w = csv.writer(dat, delimiter=',')
        
        for r in data3d:
            dat_w.writerow(r) 
    
    data3d = np.array(data3d)
    
    data3d = data3d.transpose()
   
    fig = plt.figure()
    
    ax = fig.add_subplot(111, projection='3d')
    
    ax.scatter(data3d[0], data3d[1], data3d[2], zdir='x')
    
   