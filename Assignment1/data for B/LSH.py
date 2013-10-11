#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# by zhangzhi @2013-10-07 00:00:14 
# Copyright 2013 NONE rights reserved.
"""
for locality sensitive hashing
typically,
    b for #bands
    r for #rows
    b * r shoule be nHash \
        which is the length of the signature
"""
import numpy as N

def findCandidatePairs(sigM, b, r):
    sigM = N.array(sigM, int) 
    nHash, docCnt = sigM.shape
    hBkt = countLshHashBucket(sigM, b, r, docCnt)
    # if two candidate is the same, the value would be b
    # in cPairDict
    cPairDict = {} 

    for iLine in hBkt:
        for hashPair in iLine:
            cPairs = list2Pairs(iLine[hashPair])
            for iPair in cPairs:
                a, b = iPair
                if a not in cPairDict:
                    cPairDict[a] = {}
                if b not in cPairDict[a]:
                    cPairDict[a][b] = 0
                if b not in cPairDict:
                    cPairDict[b] = {}
                if a not in cPairDict[b]:
                    cPairDict[b][a] = 0
                cPairDict[a][b] += 1
                cPairDict[b][a] += 1
    return cPairDict 
    
def list2Pairs(aList):
    l = len(aList)
    pairs = []
    for i in range(l):
        for j in range(l):
            if i <= j:
                break
            pairs.append((aList[j], aList[i]))
    return pairs
    
def countLshHashBucket(sigM, b, r, docCnt):
    # find pairs
    hBkt = [ {} for each in range(b) ]                  
    for iB in range(b):#count the little band into a bkt
        rowBegin = iB * r
        for iDoc in range(docCnt):
            hashValue = tuple(sigM[rowBegin:rowBegin+r, iDoc].tolist())
            if hashValue not in hBkt[iB]:
                hBkt[iB][hashValue] = []
            hBkt[iB][hashValue].append(iDoc)
    return hBkt

def sigMTopN(sigM, b, r, docCode, N=10):
    cPairDict = findCandidatePairs(sigM, 3, 2)
    #print cPairDict
    if docCode not in cPairDict:
        return []
    dictOfTheDoc =  cPairDict[docCode]
    retList = sorted(dictOfTheDoc.items(), key=lambda d:d[1], reverse=True)
    retList = retList[:N+1]
    return [ i[0] for i in retList ][1:]
     

if __name__ == '__main__':
    sigM = [[1,0, 1, 1],[1, 2, 1, 1], [0, 1, 0, 3], [2,3,2,0], [1,0,0,1], [1,2,2,4]]
    print sigMTopN(sigM, 3, 2, 2, 100)

