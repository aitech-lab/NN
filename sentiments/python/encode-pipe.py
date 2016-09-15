#!/usr/bin/python3
# coding=utf-8

import re
import vocabulary
import io
import sys

stat = {}

vocabulary.init()
                                
stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
k = 0
for l in stdin:

    (tone, codes) = vocabulary.encode(l)
    if(abs(tone)>0.2) and len(codes)>0:
        print('{:3.1f}'.format(tone), end="\t")
        print("\t".join(str(c) for c in codes))

    k+=1
    if k%1000 is 0:
        sys.stderr.write(str(k))
        sys.stderr.write("\n")