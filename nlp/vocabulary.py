#!./env/bin/python3
# coding=utf-8

import re
import pymorphy2

word2id = {}
id2word = []
morph = None

def init(file="positive-norm.txt"):

    global morph
    global word2id 
    global id2word 
    
    morph = pymorphy2.MorphAnalyzer()
    
    word2id = {}
    id2word = []
   
    word2id["unknown"] = 0
    id2word.append("unknown")
    
    i = 1                     
    for l in  open(file, "r"):
       l = l.replace("\n","")
       w = l.split("\t")
       s = int(w[1])
       w = w[0]
       
       if s>=2:
           word2id[w] = i
           id2word.append(w)
           i += 1

def encode(sentence):
    s = sentence
    s = re.sub(r"[^а-яА-ЯёЁ]+", " ", s)
    s = re.sub(r"^\s+|\s+$","", s)
    words = re.split(r"\s+", s)
    for i, w in enumerate(words):
        words[i] = getid(w)
    return words
    
def getid(word):
    norm = morph.parse(word)[0].normal_form
    if norm in word2id:
        return word2id[norm]
    else:
        return 0
        
def getword(id):
    if id>=len(id2word) or id<0:
        id = 0
    return id2word[id]

if __name__ == "__main__":
    init()
    enc = encode(u"В лесу родилась ёлочка, в лесу она росла")
    print(enc)
    # print(word2id)
    # print(id2word)
