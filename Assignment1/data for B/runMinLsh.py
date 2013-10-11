#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# by zhangzhi @2013-10-11 23:45:57 
# Copyright 2013 NONE rights reserved.
import LSH
import SigGen

if __name__ == '__main__':
    sigMFileName = 'SIG_M.pickle'
    'load file'
    g_code2Shg, g_code2Doc, g_shg2Code, g_doc2Code, sigM = SigGen.loadSigM(sigMFileName)
    print sigM
    ret = LSH.sigMTopN(sigM, 50, 2, g_doc2Code[1], 100)
    print ret
