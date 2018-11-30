#!/usr/bin/env python

import numpy as np
import sklearn
import matplotlib.pyplot as plt

logConcentration = [1.30, 0.30, -0.70, -1.70, -2.70, -3.70] 
avgCq = [20.671, 18.032, 12.742, 12.463, 14.97, 13.12] 

from sklearn.linear_model import LinearRegression
#X = logConcentration
#Y = avgCq

X = np.asarray(logConcentration[0:5]).reshape(-1,1)
Y = avgCq[0:5]
standardRegression = LinearRegression()

''''plt.scatter(X, Y)
plt.title("log vs means")
plt.xlabel("log concentration")
plt.ylabel("Ct mean")
plt.show()'''

standardRegression.fit(X, Y)
#standardRegression.fit((X, Y), (X, Y), sample_weight=None)
print(standardRegression.coef_) #output is currently 1.6971
print(standardRegression.intercept_) #output is currently 16.96357
