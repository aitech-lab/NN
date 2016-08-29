#!/bin/python

import sys
import re

import pymorphy2

# load file

try:
    h = open(str(sys.argv[1]))
    lines = h.readlines()
except IndexError:
    print("Usage:")
    print(__file__, "input.txt")
    sys.exit(0)
except:
    print(sys.exc_info[0])
    raise

# init morpher
morph = pymorphy2.MorphAnalyzer()

# parse
vocab = {}
for l in lines:
    words = re.split(u"[^а-яА-Яa-zA-Z]+", l)
    for w in words:
        m = morph.parse(w)
        # print(m)
        n = m[0].normal_form
        t = m[0].tag
        vocab[n] = vocab.get(n,0) + 1
        # print(w + " -> " + n, t)
print(vocab)
