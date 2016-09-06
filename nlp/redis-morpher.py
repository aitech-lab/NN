#!./env/bin/python
# coding=utf-8

import sys
import redis
import codecs
import pymorphy2
import json

input = "morph"
output = "morphed"

morph = pymorphy2.MorphAnalyzer()

rdb = redis.StrictRedis(host='localhost', port=5678, db=0)
while True:
     line = rdb.brpop(input, 5)
     
     if line == None:
         sys.stdout.write('.')
         sys.stdout.flush()
         continue
     
     print("")
     print("-"*10)
     words = line[1].decode("utf-8").split(" ")
     result =[] 
     for w in words:
         m = morph.parse(w)             
         r = [
             m[0].word,
             m[0].normal_form,
             ",".join(m[0].tag.grammemes),
             m[0].score
         ]
         result.append(r)
     print(str(result))
     rdb.rpush( output, str(result) )
