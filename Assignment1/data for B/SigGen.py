#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# by zhangzhi @2013-10-06 11:55:07 
# Copyright 2013 NONE rights reserved.
"""
This module is for generationg signature
    provided list:
        . minHashing
"""
import random
import copy
import sys

g_code2Shg = []
g_code2Doc = []
g_shg2Code = {}
g_doc2Code = {}

def genMatrix(docShinglingCount):
    """
    gen a matrix for multiset
    """
    global g_code2Shg, g_code2Doc, g_shg2Code, g_doc2Code

    docCnt = 0
    shgMax = {}
    shgCnt = 0
    totalShgCnt = 0
    m = None

    for doc, shg, count in docShinglingCount:
        #deal with coding
        if doc not in g_doc2Code:
            docCnt += 1     
            g_code2Doc.append(doc)
            g_doc2Code[doc] = docCnt -1
        if shg not in g_shg2Code:
            shgCnt += 1
            g_code2Shg.append(shg)
            g_shg2Code[shg] = shgCnt - 1 
        shgCode = g_shg2Code[shg]

        # deal with shgMax
        if shgCode not in shgMax:
            shgMax[shgCode] = count
        elif shgMax[shgCode] <= count:
            shgMax[shgCode] = count

#    print sorted(docSet)
#    for each in sorted(shgMax.keys()):
#        print each, shgMax[each]

    # so 
    totalShgCnt = sum(shgMax.values())

    #debug
    #print "docCnt",  docCnt
    #print "shgCnt",  shgCnt
    #print sorted(shgMax.keys())

    #we begin to gen matrix m

    #init m with docCnt  colume and shgCnt rows
    m = [ [0] * docCnt for each in range(shgCnt) ]

    for doc, shg, count in docShinglingCount:
        docCode = g_doc2Code[doc]
        shgCode = g_shg2Code[shg]
        try:
            m[shgCode][docCode] = count
        except Exception, e:
            print e
            print "shgCode, docCode:", shgCode, docCode
            sys.exit(-1) 
    #print "docCnt, shgCnt, docCnt*shgCnt"
    #print docCnt, shgCnt, docCnt*shgCnt
    #sys.exit(-1) 

    return m, shgMax, docCnt, shgCnt, totalShgCnt

def genRandomMatrix(totalShgCnt, nHash):
    pai = [] 
    seed = []
    for j in range(totalShgCnt):
        seed.append(j)

    for i in range(nHash):
        random.shuffle(seed)
        pai.append(copy.deepcopy(seed))
         
    return pai

def minHashSig(m, shgMax, docCnt, shgCnt, totalShgCnt, nHash):
    """
    @param:
        m, it is the matrix for shigling(maybe)
        we will gen sig for each column of matrix.
        shgMax,
        docCnt, 
        shgCnt, 
        totalShgCnt,

        nHash, the width of sig
        value of the matrix can be more than one
    """
    #init, 
    sigM = [] # nHash Rows,   totalShgCnt Columns, 
    for i in range(nHash):
        sigM.append([]) 
        for j in range(docCnt):
            sigM[i].append(totalShgCnt)

    #gen a random matrix
    pai = genRandomMatrix(totalShgCnt, nHash)

    #show time of 4 times circulation
    thisBegin = 0
    for iShg in range(shgCnt):
        step = shgMax[iShg]
        for jDoc in range(docCnt):
            repeat = m[iShg][jDoc]
            if repeat == 0:
                continue
            for kHash in range(nHash):
                #gen min value of pai which is specificed by: (shg, pai, doc, hash)
                minVal = min(pai[kHash][thisBegin:thisBegin+repeat])
                if minVal < sigM[kHash][jDoc]:
                    sigM[kHash][jDoc] = minVal
        thisBegin += step
        #debug
        #print '++++' * 4
        #print "sigM in itering iShg:", iShg
        #print '++++' * 4
        #print sigM
    #done
    return sigM, pai

def genSigM(docShinglingCount, nHash):
    global g_code2Doc
    m, shgMax, docCnt, shgCnt, totalShgCnt = genMatrix(docShinglingCount)
    sigM, pai = minHashSig(m, shgMax, docCnt, shgCnt, totalShgCnt, nHash)
    return sigM, g_code2Doc
        
if __name__ == '__main__':
    import ReadUtil
    print 'hello world'
    ret = ReadUtil.readShinglingData('LSH_data.txt')
    print "now count it"
    print genSigM(ret, 10)


