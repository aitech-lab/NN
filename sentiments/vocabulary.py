#!./env/bin/python3
# coding=utf-8

import re
import pymorphy2
from slang import cleanup

cache   = {}
word2id = {}
id2word = []
morph = None

def init(file="data/frequency-norm-cleaned.tsv"):

    global morph
    global word2id 
    global id2word 
    
    morph = pymorphy2.MorphAnalyzer()
    
    word2id = {}
    id2word = []
   
    word2id["unknown"] = 0
    id2word.append("unknown")
    
    i = 1                     
    for l in  open(file, "r", encoding="utf-8"):
       l = l.replace("\n","")
       w = l.split("\t")[0]
       word2id[w] = i
       id2word.append(w)
       i += 1

def encode(sentence):
    try:
      s, tone = cleanup(sentence)
    except:
      return []
    s = s.lower()
    s = re.sub(r"[^а-яА-ЯёЁ]+", " ", s)
    s = re.sub(r"^\s+|\s+$","", s)
    words = re.split(r"\s+", s)
    codes =[]
    for i, w in enumerate(words):
        code = getid(w)
        if code > 0:
            codes.append(code)
    return tone, codes
    
def getid(word):
    global cache
    norm = cache.get(word, None)
    if norm is None:
        norm = morph.parse(word)[0].normal_form
    if norm in word2id:
        return word2id[norm]
    else:
        return 0
        
def getword(id):
    if id>=len(id2word) or id<0:
        id = 0
    return id2word[id]
