#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# by zhangzhi @2013-11-16 08:13:20 
# Copyright 2013 NONE rights reserved.
import pandas
import pylab
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import sys

import numpy
import pickle
import pmf as PMF
import numpy as np
import math

def readInList(fn):
    ret = []
    with open(fn) as f:
        for line in f:
            line = line.strip().split("\t")
            line = [ int(x) for x in line ]
            ret.append(line) 
    return ret

def readTrain():
    fn = 'dataset/training.dat'
    return readInList(fn)

def readTest():
    fn = 'dataset/testing.dat'
    return readInList(fn) 

def invLogistic(v):
    """
    please no extremely  values like 0, 1
    invert func of   
        1 / (1 + exp{-x})
        1.0 / (1 + math.exp(-x)
    so x = :
        log( v / 1- v)
        np.log(v) - np.log(1 - v)
    """
    return np.log(v) - np.log(1 - v)

def transRawRate(r, low, top):
    "tran a raw value r into value in gaussian distribution"
    #low -= 1
    #top += 1
    #normalization
    midv = float(r - low) / (top - low)
    return midv
    #return invLogistic(midv)

def trans2RawRate(v, low, top):
    #low -= 1
    #top += 1
    midv = logistic(v)
    r = midv * (top - low) + low
    #if r > top-1:
    #    r = top - 1
    #elif r < low+1 :
    #    r = low + 1
    #else:
    #    pass
    return r

def logistic(v):
    return 1.0 / (1.0 + math.exp(-1.0 * v))

if __name__ == '__main__':
    low = 1
    top = 5
    latent = 30
    trainData = readTrain()
    trainData = [ (x[0], x[1], transRawRate(x[2], low, top)) for x in trainData ]
    testData = readTest()
    testOut = []

    pmf = PMF.ProbabilisticMatrixFactorization(trainData, latent)
    liks, lRates = pmf.update()
    plt.figure()
    plt.plot(liks)
    plt.xlabel("Iteration")
    plt.ylabel("Log Likelihood")
    plt.figure()
    plt.plot(lRates)
    plt.xlabel("Iteration")
    plt.ylabel("Learning Rate")
    plt.show()

    #predict #multiply
    print "predict"
    for i, j in testData:
        #transform it
        ret = trans2RawRate(pmf.predict(i, j), low, top) 
        testOut.append(ret)
        print ret
    
    with open('testOut.%s.txt'%(latent), 'w') as f:
        for each in testOut:
            f.write("%f\n" % each)
    

