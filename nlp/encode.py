#!./env/bin/python3
# coding=utf-8

import sys

if len(sys.argv) != 3:
    print("Usage:\n\t./encode.py ../data/tweets/positive.txt ../data/tweets/negative.txt")
    sys.exit(0)

import vocabulary as voc
voc.init()

import numpy as np

print("Params:")
print(sys.argv)

positive = sys.argv[1]
negative = sys.argv[2]

out = open("train_data.txt", "w")

for l in open(positive, "r"):
    e = "\t".join(str(c) for c in voc.encode(l))
    out.write("1\t%s\n" % e)
     
for l in open(negative, "r"):
    e = "\t".join(str(c) for c in voc.encode(l))
    out.write("0\t%s\n" % e)

out.close()

    
