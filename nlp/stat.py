#!./env/bin/python3
# coding=utf-8

import io
import sys
import re
import codecs
import pymorphy2

class Counter(dict): 
    def __missing__(self, key): 
        return 0
        
words = Counter()

morph = pymorphy2.MorphAnalyzer()

# stdin = codecs.getreader("utf-8")(sys.stdin)
stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')

for l in stdin:
    #l = tk.deurl(l)
    #l = tk.denick(l)
    #l = tk.dedigit(l)
    #l = tk.desmile(l)
    #l = tk.deemoji(l)
    #l = tk.cleanup(l)
    
    #t = tk.tokenize(l)
    l = re.sub(r"[^а-яА-ЯёЁ]+", " ", l)
    l = re.sub(r"^\s+|\s+$|\n", "", l)
    t = re.split(r"\s+", l)
    for w in t:
        norm = morph.parse(w)[0].normal_form
        words[norm] += 1
        
for w in sorted(words.items(), key=lambda a: a[1], reverse=True):
    print(w[0]+"\t"+str(w[1]))
