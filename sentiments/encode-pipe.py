#!/usr/bin/python3
# coding=utf-8

import re
import vocabulary
import io
import sys

stat = {}

vocabulary.init()
                                
stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
for l in stdin:
    (tone, codes) = vocabulary.encode(l)
    print(tone, end="\t")
    print("\t".join(str(c) for c in codes))
