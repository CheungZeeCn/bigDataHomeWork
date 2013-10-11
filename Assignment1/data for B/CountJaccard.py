#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# by zhangzhi @2013-10-07 11:20:02 
# Copyright 2013 NONE rights reserved.

import collections as C

def countJaccardM(docShgCntList):
    """
    we read the list in docShgCntList,
    each one of docShgCntList is a list like
    [doc, shg, count]
    than we count the jaccard for each two doc
    """
    shgCounter = {}
    jaccardM = {}
    for doc, shg, count in docShgCntList:
        #print "+" * 20
        #print "doc, shg, count"
        #print doc, shg, count
        if doc not in shgCounter:
            shgCounter[doc] = C.Counter()
        shgCounter[doc][shg] = count
        #print shgCounter
    #count every jaccard
    for eachDoc1 in shgCounter:
        if eachDoc1 not in jaccardM:
            jaccardM[eachDoc1] = {}
        for eachDoc2 in shgCounter:
            if eachDoc1 == eachDoc2:
                jaccardM[eachDoc1][eachDoc2] = 1
            elif (eachDoc2 in jaccardM) and \
                (eachDoc1 in jaccardM[eachDoc2]):
                jaccardM[eachDoc1][eachDoc2] = \
                    jaccardM[eachDoc2][eachDoc1]        
            else:
                #count jaccard
                a = shgCounter[eachDoc1]
                b = shgCounter[eachDoc2]
                j = float(sum((a & b).values())) / sum((a | b).values())
                jaccardM[eachDoc1][eachDoc2] = j
    return jaccardM

def jaccardTopN(jaccardM, doc, N=10):
    dictOfTheDoc = jaccardM[doc]                 
    print dictOfTheDoc
    retList = sorted(dictOfTheDoc.items(), key=lambda d:d[1], reverse=True)
    retList = retList[:N+1]
    return [ i[0] for i in retList ][1:]

if __name__ == '__main__':
    #print 'hello world'
    import ReadUtil
    ret = ReadUtil.readShinglingData('LSH_data_min.txt')
    print ret
    jM = countJaccardM(ret)
    print jM
    print jaccardTopN(jM, 0, 1)




