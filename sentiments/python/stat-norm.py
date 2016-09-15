#!/usr/local/bin/python3
# coding=utf-8

import re
import pymorphy2
from slang import cleanup

morph = pymorphy2.MorphAnalyzer()

stat = {}
norm = {}
if __name__ == "__main__":
    
    import io
    import sys
                                
    stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
    for l in stdin:
        
        try:
            (txt, tone) = cleanup(l)
        except:
            continue
            
        for t in txt.split(" "):
            n = norm.get(t, None)
            if n == None:
                norm[t] = n = morph.parse(t)[0].normal_form
            stat[n] = stat.get(n,0)+1
            
for word in sorted(stat, key=stat.get, reverse=True):
    if stat[word]<2 : continue
    print(word+"\t"+str(stat[word]))
