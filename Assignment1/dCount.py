#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# by zhangzhi @2013-10-11 22:06:40 
# Copyright 2013 NONE rights reserved.
import math

def count(aList, d=2):
    N = 0  
    SUM = [0] * d
    SUMSQ = [0] * d
    for each in aList:
        N += 1    
        for i in range(d):
            SUM[i] += each[i]
            SUMSQ[i] += each[i] ** 2
    return N, SUM, SUMSQ

def countVD(N, SUM, SUMSQ):
    VD = []
    N *= 1.0
    for i in range(len(SUM)):
        Vi = SUMSQ[i]/N - (SUM[i]/N)**2   
        Di = math.sqrt(Vi)
        VD.append((Vi, Di))
    return VD

if __name__ == '__main__':
    a = ([(4, 10), (7, 10), (4, 8), (6, 8)], \
            [(3, 4), (2, 2), (5, 2)], \
            [(9, 3), (10, 5), (12, 6), (11, 4), (12, 3)], \
            )
    for each in a:
        print "======="
        ret = count(each)
        print ret
        print countVD(ret[0], ret[1], ret[2])

