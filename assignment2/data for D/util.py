#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# by zhangzhi @2013-11-17 19:44:00 
# Copyright 2013 NONE rights reserved.
import re
import numpy as np

def readInList(fn):
    reEmpty = re.compile(r'\s+')
    ret = []
    with open(fn) as f:
        for line in f:
            line = reEmpty.split(line.strip())
            #line = [ int(x) for x in line ]
            ret.append(line)
    return ret

def readTrain(fn):
    ret = []
    data = readInList(fn)
    for each in data: 
        item = [ int(each[0]), {} ]
        for col in each[1:]:
            k, v = col.split(':')        
            item[1][int(k)] = int(v)
        ret.append(item)
    return ret

def readTest(fn):
    ret = []
    data = readInList(fn)
    for each in data: 
        item = [ 0, {} ]
        for col in each:
            k, v = col.split(':')        
            item[1][int(k)] = int(v)
        ret.append(item)
    return ret

def dict2Array(rec, di):
    x = np.zeros(di)
    for k in rec:
        x[k] = rec[k]
    return x

if __name__ == '__main__':
    print readTest('minTest')
    print readTrain('minTrain')

