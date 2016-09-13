#!/usr/local/bin/python3
# coding=utf-8

import re
from slang import cleanup

stat = {}
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
            t = t.lower()
            stat[t] = stat.get(t,0)+1
            
for word in sorted(stat, key=stat.get, reverse=True):
    print(word+"\t"+str(stat[word]))
