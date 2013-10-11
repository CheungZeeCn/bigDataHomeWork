#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# by zhangzhi @2013-10-10 21:51:16 
# Copyright 2013 NONE rights reserved.
"""
module of DGIM
"""
import math

def readData(fileName):
    dataStream = []
    with open(fileName) as f:
        ret = f.readlines()
    for each in ret:
        tabSpl = each.strip().split("\t")
        dataStream += [ int(x) for x in tabSpl ]
    return dataStream

class DGIM(object):
    def __init__(self, N, r=2):
        self.N = N      
        self.r = r     
        self.winList = [] # 0=>timestamp 1=>size
        self.ts = None

    def _maintain_(self, ):
        i = 0
        while i != -1:
            i = self._merger_(i)    

    def _combine_(self, i):
        "combine two adjacent unit in winList"
        for index in range(i, i+1):
            self.winList[i][1] *= 2    
        self.winList.pop(i+1)
        return i

    def _merger_(self, i):
        r = self.r

        if len(self.winList) >= i+r+1 and self.winList[i][1] == self.winList[i+r][1]:
            return self._combine_(i+r-1)
        else:
            #we stop here because there is no need to combine units anymore
            return -1

    def _cutTail_(self, ):
        if len(self.winList) == 0:
            return False
        if self.ts - self.winList[-1][0] >= self.N:
            self.winList.pop()
            return True
        else:
            return False

    def _updateTs(self, ts):
        self.ts = ts
        return self.ts

    def eat(self, data, ts):
        self._updateTs(ts)
        self._cutTail_()
        if data == 0:
            return 0
        else:
            self.winList.insert(0, [ts, 1])
            self._maintain_()

    def query(self, k):
        allOne = 0
        lastVal = 0
        for each in self.winList:
            if self.ts - each[0] < k:
                allOne += each[1]
                lastVal = each[1]
            else:
                break
        allOne -= lastVal/2
        return allOne

    def printWinList(self, ):
        print "==winList===[ts, value]========="
        for each in self.winList:
            print each, 
        print ""

if __name__ == '__main__':
#    import random
#    d = DGIM(20)
#    window = []
#    for s in range(22):
#        if random.random() >= 0.0:
#            window.insert(0, 1)
#            d.eat(1, s) 
#        else:
#            window.insert(0, 0)
#            d.eat(0, s) 
#        print "================ window,s ==============="
#        print window, "<%s>" % s
#        d.printWinList()
#
#    print "auery 10 in  win 20"
#    print d.query(10)
#
#
    data = readData('stream_data.txt')
    d = DGIM(1000)
    ts = 0
    for each in data:
        d.eat(each, ts)
        ts += 1

    d.printWinList()
    onesActually = sum(data[-1000:])
    print "1's in last 1000bits ~=", d.query(1000), "in fact = ", onesActually


