#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re
import csv

import pymorphy2

# load file

try:
    f = open(sys.argv[1], encoding="utf-8", newline="\n")
    rows = csv.reader(f, delimiter=";", quotechar='"')
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
for r in rows:
    tweet =  r[3]
    words = re.split(u"[^а-яА-Я]+|[а-яА-Я]{10,}", tweet)
    for w in words:
        m = morph.parse(w)
        # print(m)
        n = m[0].normal_form
        t = m[0].tag
        vocab[n] = vocab.get(n,0) + 1
        # print(w + " -> " + n, t)
for w in sorted(vocab, key=vocab.get, reverse=True):
    print(w, vocab[w])
