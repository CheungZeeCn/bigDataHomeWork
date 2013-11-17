#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# by zhangzhi @2013-11-17 22:37:59 
# Copyright 2013 NONE rights reserved.
import util as U
import numpy as np
from sklearn import linear_model

def findMaxDi(data):
    maxDi = 0
    for rec in data:     
        for k in rec[1]:
            if k > maxDi:
                maxDi = k
    return maxDi

    
if __name__ == '__main__':
    trainList = U.readTrain('train')
    testList = U.readTest('test')
    di = max(findMaxDi(trainList), findMaxDi(testList)) + 1
    trainArray = [ U.dict2Array(each[1],di) for each in trainList ]
    trainOut = [ each[0] for each in trainList ]
    testArray = [ U.dict2Array(each[1],di) for each in testList ]

    clf = linear_model.SGDClassifier()
    clf.fit(trainArray, trainOut) 
    predict = clf.predict(testArray)
    for each in predict:
        print "%+d" %each


    

