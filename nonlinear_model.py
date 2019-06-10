# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 23:21:50 2019

@author: Dmitry
"""

import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import scipy.integrate as integrate
import matplotlib.pyplot as plt

def func(x, a, b, c, d):
    """
        Модель с параметрами a, b, c, d, которую необходимо подогнать под данные
    """
    return np.dot(a, x) + b*np.sin(c*x) + d

data = pd.read_csv("data_nonlinear.csv", delimiter=',', header=None)

x = np.array(data[0])
y = np.array(data[1])

np.random.seed(1729)

popt, pcov = curve_fit(func, x, y)

print(popt)

plt.figure()

plt.plot(x, func(x, *popt), 'r-',
         label='fit: a=%5.3f, b=%5.3f, c=%5.3f, d=%5.3f' % tuple(popt))

plt.plot(x, func(x, 1, 10, 1, 0))

plt.show()

print("Result of residual integration")
diff = integrate.quad(lambda x: np.abs(func(x, *popt) - func(x, 1, 10, 1, 0)), 
                      -10*np.pi, 10*np.pi)

print(diff)

y_res = np.abs(func(x, *popt) - func(x, 1, 10, 1, 0))

plt.figure()

plt.title("Residuals plot")

plt.plot(x, y_res)

plt.show()