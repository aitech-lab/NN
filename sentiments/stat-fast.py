#!/usr/bin/python3
# coding=utf-8

import sys
import re
import pymorphy2
from slang import cleanup

import queue
import threading
import multiprocessing

if len(sys.argv)!=2:
    print("Usage:\n\t",__file__,"file.txt")
    sys.exit(0)

try:
    fd = open(sys.argv[1],'r')
except:
    print("Can't open file")
    sys.exit(0)

print("Loading file")
file = fd.read()
print("Loaded", len(file))
morph = pymorphy2.MorphAnalyzer()

stat  = {} # word-> count
norm  = {} # norm-> count
cache = {} # word-> norm

q = queue.Queue()
threads = []

def worker():                               
    print("worker start")
    k = 0
    while True:
        l = q.get()
        if k%100 == 0:
            print(q.qsize(), end=" ")
            k+=1
        if l is None:
            break
        try:
            (txt, tone) = cleanup(l)
        except:
            q.task_done()
            continue
            
        for t in txt.split(" "):
            # count word
            stat[t] = stat.get(t, 0)+1
            # get norm
            n = cache.get(t, None)
            if n == None:
                cache[t] = n = morph.parse(t)[0].normal_form
            norm[n] = norm.get(n,0)+1

        q.task_done()

cores = multiprocessing.cpu_count()
print("Lauch",cores,"threads")
for c in range(cores):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

lines = file.split("\n")
print("Put",len(lines),"to queue")
for l in file.split('\n'):
    if len(l)>0:
        q.put(l)
print("Wait for processing end")
q.join()

print("Stop workers")
# stop workers
for i in range(cores):
    q.put(None)
print("Wait workers end")
for t in threads:
    t.join()


def write(fn, obj):
    print("Write",fn)
    fd = open(fn, "w")
    for k in sorted(obj, key=obj.get, reverse=True):
        fd.write(k+"\t"+str(obj[k])+"\n")

write("stat.tsv", stat)
write("norm.tsv", norm)