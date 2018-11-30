#!/usr/bin/env python

import numpy as np
import sklearn
import matplotlib.pyplot as plt

logConcentration = [1.30, 0.30, -0.70, -1.70, -2.70, -3.70] 
avgCq = [8.718, 11.779, 15.414, 19.012, 22.247, 25.459] #read from file

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
slope = standardRegression.coef_
yIntercept = standardRegression.intercept_
print(slope) #output is currently -3.4291
print(yIntercept) #output is currently 13.033630000000002

#regressionLineY = [standardRegression.intercept_, ]
#regressionLineX = [0, ]
