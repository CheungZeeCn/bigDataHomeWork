#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# by zhangzhi @2013-11-12 20:54:39 
# Copyright 2013 NONE rights reserved.

def readEage(fn, limit = None):
    ret = []
    c = 0
    with open(fn) as f:
        for line in f:
            if line[0] == '#':
                continue
            a, b = line.strip().split("\t")
            ret.append((int(a), int(b)))
            if limit:
                c += 1  
                if c == limit:
                    break
    return ret
            


if __name__ == '__main__':
    print 'hello world'

