#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# by zhangzhi @2013-11-13 23:31:35 
# Copyright 2013 NONE rights reserved.
import util
import pca
import numpy as np
import sys

if __name__ == '__main__':
    for i in range(3):
        X = util.load_data(i, 5000)
        mean = np.mean(X, 0)

        evecs, evals = pca.pcaSvd(X)
        
        #test =  [ float(each) for each in evecs[0] ] 
        for j in range(20):
            if j == 0:
                #util.display(mean)
                pass
            util.display(evecs[j])

