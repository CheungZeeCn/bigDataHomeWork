#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# by zhangzhi @2013-11-12 20:33:44 
# Copyright 2013 NONE rights reserved.
import networkx as nx
import matplotlib.pyplot as plt
import readTxt as r
import page
import logging as l
l.basicConfig(level=l.DEBUG, \
        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
        datefmt='%a, %d %b %Y %H:%M:%S')


def getRank():
    edges = r.readEage('web-Google.txt')
    #print edges
    g = nx.DiGraph()
    l.debug("#begin to add edges")
    g.add_edges_from(edges, weight=1)
    l.debug("#begin to count")
    eigenvector = page.pagerank(g)
    return eigenvector

if __name__ == '__main__':
    ret = getRank()
    l.debug("sotring, len is %d"  % len(ret))
    ret = sorted(ret.items(), key=lambda d: d[1], reverse=True)
    for each in ret:
        print each

