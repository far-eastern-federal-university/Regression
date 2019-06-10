# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 21:55:28 2019

@author: Dmitry
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = pd.read_csv("data_linear.csv", delimiter=',', header=None)

x = np.array(data[0]).reshape(-1,1)
y = np.array(data[1])

model = LinearRegression()

model.fit(x, y)

print('coefficient of determination:', model.score(x, y))
print('coef:', model.coef_)
print('intercept', model.intercept_)

s = [3]*len(x)

plt.figure()

plt.title("Linear fitted model")

plt.scatter(x, y, c="red", s=s)

plt.plot(x, model.coef_*x + model.intercept_, linewidth=2)

plt.show()

#----------------------------------------------------------

data = pd.read_csv("data_nonlinear.csv", delimiter=',', header=None)

x = np.array(data[0]).reshape(-1,1)
y = np.array(data[1])

model = LinearRegression()

model.fit(x, y)

print('coefficient of determination:', model.score(x, y))
print('coef:', model.coef_)
print('intercept', model.intercept_)

s = [3]*len(x)

plt.figure()

plt.title("Nonlinear fitted model")

plt.scatter(x, y, c="red", s=s)

plt.plot(x, model.coef_*x + model.intercept_, linewidth=2)

plt.show()