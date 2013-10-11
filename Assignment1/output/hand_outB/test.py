#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# by zhangzhi @2013-10-06 14:32:52 
# Copyright 2013 NONE rights reserved.

import SigGen
import ReadUtil



if __name__ == '__main__':
    #print 'hello world'
    #ret = ReadUtil.readShinglingData('LSH_data_min.txt')
    #print "now count it"
    #m, shgMax, docCnt, shgCnt, totalShgCnt = SigGen.genMatrix(ret)
    #nHash = 2
    #print 'm:'
    #print m
    #print "shagMax"
    #print shgMax
    #print "docCnt, shgCnt, totalShgCnt"
    #print docCnt, shgCnt, totalShgCnt
    #print "=" * 20

    #sigM, pai = SigGen.minHashSig(m, shgMax, docCnt, shgCnt, totalShgCnt, nHash)
    #print "sigM"
    #print sigM 
    #print "pai"
    #print pai

    ret = ReadUtil.readShinglingData('LSH_data_min.txt')
    print "now count it"
    m, shgMax, docCnt, shgCnt, totalShgCnt = SigGen.genMatrix(ret)
    nHash = 2
    sigM, pai = SigGen.minHashSig(m, shgMax, docCnt, shgCnt, totalShgCnt, nHash)
