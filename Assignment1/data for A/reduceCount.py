#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# by zhangzhi @2013-09-29 00:08:46 
# Copyright 2013 NONE rights reserved.

from operator import itemgetter
import sys
current_word = None
current_count = 0
word = None


if __name__ == '__main__':
    for line in sys.stdin:
        line = line.strip()
        word, count = line.split('\t', 1)
        try:
            count = int(count)
        except ValueError:
            continue
        if current_word == word:
            current_count += count
        else:
            if current_word:
                print '%s\t%s' % (current_word, current_count)
            current_count = count
            current_word = word
    if current_word == word:
        print '%s\t%s' % (current_word, current_count)




