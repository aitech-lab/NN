#!./env/bin/python3
# coding=utf-8

import io
import sys
import codecs

import tokenizer as tk


class Counter(dict): 
    def __missing__(self, key): 
        return 0
        
words = Counter()

# stdin = codecs.getreader("utf-8")(sys.stdin)
stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')

for l in stdin:
    l = tk.deurl(l)
    l = tk.denick(l)
    l = tk.dedigit(l)
    l = tk.desmile(l)
    l = tk.deemoji(l)
    l = tk.cleanup(l)
    
    t = tk.tokenize(l)
    t = filter(lambda a: a != ' ', t)
    for w in t:
        words[w.lower()] += 1
        
for w in sorted(words.items(), key=lambda a: a[1], reverse=True):
    print(w[0]+"\t"+str(w[1]))
