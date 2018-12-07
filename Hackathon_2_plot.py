#!/usr/bin/env python

import numpy as np
from numpy import log10 as log
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def harry_plotter(Y):
    Y = np.array([float(i) for i in Y]).reshape(-1, 1)
    X = np.array(log([20, 2, .2, .02, .002,.0002])).reshape(-1, 1)
    # X = np.asarray(logConcentration[0:5]).reshape(-1,1) #x values (remain constant/unchanged)
    # Y = avgCq[0:5] #y values (will change)
    standardRegression = LinearRegression()

    standardRegression.fit(X, Y)
    #standardRegression.fit((X, Y), (X, Y), sample_weight=None)
    slope = standardRegression.coef_[0]
    yInt = standardRegression.intercept_[0]
    # print(slope) #output is currently -3.4291
    # print(yInt) #output is currently 13.033630000000002

    regressionLineY = [yInt, slope+yInt, slope*2+yInt, slope*3+yInt, slope*-1+yInt, slope*-2+yInt, slope*-3+yInt]

    # regressionLineX = [0, 1, 2, 3, -1, -2, -3]
    # print(standardRegression.predict(X))
    plt.scatter(X[:,0], Y[:,0], marker="+", s=48)
    plt.plot(X, standardRegression.predict(X), 'black', linewidth=0.5 ) #regression line WIP
    # print(
    #                ))
    # plt.plot(X[:,0], regressionLineY) #regression line WIP
    r2 = r2_score(Y, standardRegression.predict(X) )
    plt.text(-3, 8, "y = %sx+%s\nR^2 = %s" %(slope[0], yInt, r2)) #prints line equation
    plt.title("log vs means")
    plt.xlabel("log concentration")
    plt.ylabel("Ct mean")
    plt.show()
    return slope[0], yInt, r2

if __name__ == "__main__":
    logConcentration = [1.30, 0.30, -0.70, -1.70, -2.70, -3.70] #stays constant/unchanged
    avgCq = [8.718, 11.779, 15.414, 19.012, 22.247, 25.459] #read from file
    harry_plotter(logConcentration, avgCq)
