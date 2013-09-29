#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# by zhangzhi @2013-09-28 16:59:38 
# Copyright 2013 NONE rights reserved.

import sys
import re

reEmpty = re.compile(r'\s+')
rePunc = re.compile(r'^\W+|\W+$')
g_stopWordSet = set()

def getWordsFromLine(aLine):
    """get word list from a line"""
    retList = []
    if line == '':
        return []
    for word in reEmpty.split(aLine.strip().lower()):
        word = rePunc.sub('', word)
        if word != '' and not isStopWord(word):
            retList.append(word)

    return retList

def isStopWord(word):
    if word in g_stopWordSet:
        return True
    else:
        return False

def initStopWordList():
    "set up"
    global g_stopWordSet

    if len(sys.argv) > 1:
        for each in sys.argv[1:]:
            with open(each) as f:         
                g_stopWordSet |= set([ word.strip() for word in f ])
    return True     

if __name__ == '__main__':
    initStopWordList()
    for line in sys.stdin:
        #print "line:[", line.strip(), ']'
        line = line.strip()
        if line == '':
            continue
        for word in getWordsFromLine(line):
            print "%s\t1" % (word)
