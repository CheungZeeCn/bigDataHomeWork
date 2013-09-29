#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# by zhangzhi @2013-09-29 00:08:46 
# Copyright 2013 NONE rights reserved.
"""
sort and find out the top N most words
"""
from operator import itemgetter
import sys

g_topN = 200
g_sortedDict = {}
g_sortedList = []
g_minCount = None


def deleteTheMin():
    global g_sortedDict, g_sortedList, g_minCount
    if len(g_sortedDict[g_minCount]) == 1:
        del g_sortedDict[g_minCount]
    else:
        g_sortedDict[g_minCount].pop()
    g_sortedList.pop()
    # not necessary
    #g_minCount = g_sortedList[-1]


def _addInDict(k, c):
    global g_sortedDict, g_sortedList, g_minCount
    if c in g_sortedDict: #already in Dict
        g_sortedDict[c].append(k)
        g_sortedList.append(c)
        g_sortedList.sort(reverse=True)
    else: # not in dict before
        g_sortedDict[c] = [k,]
        g_sortedList.append(c)
        g_sortedList.sort(reverse=True)
    g_minCount = g_sortedList[-1]

def addInDict(k, c):
    global g_sortedDict, g_sortedList, g_minCount
    if g_minCount == None: # init
        g_sortedDict[c] = [k,]
        g_sortedList = [c,]
        g_minCount = c
    elif len(g_sortedList) < g_topN: # add and sort
        _addInDict(k, c)
    else: # N item already
        if g_minCount >= c:
            pass
        else:
            deleteTheMin()    
            _addInDict(k, c)

def output():
    lastC = None
    for c in g_sortedList:
        if c == lastC:
            continue
        for k in g_sortedDict[c]:
            print "%s\t%s" % (k, c)
        lastC = c

if __name__ == '__main__':
    for line in sys.stdin:
        line = line.strip()
        #count, word = line.split("\t")
        word, count = line.split("\t")
        try:
            count = int(count)
        except ValueError:
            continue
        addInDict(word, count)       
    #ok
    output()




