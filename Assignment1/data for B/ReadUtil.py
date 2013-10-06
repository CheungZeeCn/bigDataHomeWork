#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# by zhangzhi @2013-10-06 11:43:07 
# Copyright 2013 NONE rights reserved.

import sys


def readShinglingData(fileLoc, d=','):
    """read shinglings in file
        it looks like "doc,word,times" in each line,
        if d is ','
    """
    sList = []
    with open(fileLoc) as f:
        for each in f:
            ret = each.strip().split(d)
            try:
                ret = [ int(x) for x in ret ]
            except Exception, e:
                print >> sys.stderr, e
                continue  
            sList.append(ret)   
    return sList

if __name__ == '__main__':
    print 'hello world'
    print readShinglingData("LSH_data.txt")

