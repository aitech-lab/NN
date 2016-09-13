#!/usr/bin/python3
# coding=utf-8

import sys
import re
import pymorphy2
from slang import cleanup

if len(sys.argv)!=2:
    print("Usage:\n\t",__file__,"file.txt")
    sys.exit(0)

try:
    file = open(sys.argv[1],'r')
except:
    print("Can't open file")
    sys.exit(0)

print("Loading file")

norm  = {} # norm-> count

morph = pymorphy2.MorphAnalyzer()

for l in file:
    f, w = l.split('\t')
    n = morph.parse(w)[0].normal_form
    norm[n] = norm.get(n,0) + int(f)

def write(fn, obj):
    print("Write",fn)
    fd = open(fn, "w")
    for k in sorted(obj, key=obj.get, reverse=True):
        fd.write(str(obj[k])+"\t"+k+"\n")

write("norm.tsv", stat)
# write("norm.tsv", norm)