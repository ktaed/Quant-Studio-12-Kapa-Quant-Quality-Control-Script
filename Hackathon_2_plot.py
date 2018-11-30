#!/usr/bin/env python

import numpy as np
import sklearn
import matplotlib.pyplot as plt

logConcentration = [1.30, 0.30, -0.70, -1.70, -2.70, -3.70] #stays constant/unchanged
avgCq = [8.718, 11.779, 15.414, 19.012, 22.247, 25.459] #read from file

from sklearn.linear_model import LinearRegression
#X = logConcentration
#Y = avgCq

X = np.asarray(logConcentration[0:5]).reshape(-1,1) #x values (remain constant/unchanged)
Y = avgCq[0:5] #y values (will change)
standardRegression = LinearRegression()

standardRegression.fit(X, Y)
#standardRegression.fit((X, Y), (X, Y), sample_weight=None)
slope = standardRegression.coef_
yInt = standardRegression.intercept_
print(slope) #output is currently -3.4291
print(yInt) #output is currently 13.033630000000002

regressionLineY = [yInt, slope+yInt, slope*2+yInt, slope*3+yInt, slope*-1+yInt, slope*-2+yInt, slope*-3+yInt]
regressionLineX = [0, 1, 2, 3, -1, -2, -3]

plt.scatter(X, Y)
plt.plot(regressionLineX, regressionLineY) #regression line WIP
plt.text(-3, 10, "y = %sx+%s" %(slope, yInt)) #prints line equation
plt.title("log vs means")
plt.xlabel("log concentration")
plt.ylabel("Ct mean")
plt.show()
