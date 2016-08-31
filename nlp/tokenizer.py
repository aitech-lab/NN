#!/usr/bin/python
# coding=utf-8

import sys
import pymorphy2
import codecs
import re
import math

stdin = codecs.getreader("utf-8")(sys.stdin)
morph = pymorphy2.MorphAnalyzer()

def tokenize(str):
    w = re.split(r"(\s+|[\"\'%!?.,:;\)\(=]+)", str)
    return filter(lambda a:len(a),w)  
    
def cleanup(str):
    str = re.sub("\n|^\s+", '',str)
    str = re.sub("\s+", ' ', str)
    return str

def deurl(str):
    return re.sub(r"http[^\s]+", "URL", str)

def denick(str):
    return re.sub(r"@[^\s]+", "NICK", str)

def resmile(txt):

    # k - activation power
    # n - power multiplier
    
    k = 10.0
    
    # :)
    n = 1.0
    sm = r"[:;=]-*\)+"
    for s in re.findall(sm, txt):
        l = len( re.sub(r"[^\)]+",'',s) )
        p = int ( round( math.tanh(l*n/k) *k ) )
        txt = txt.replace(s," SP"+str(p)+" ", 1)
    
    # :3
    n = 1.0
    sm = r"[:;=]-*[3Зз]+"
    for s in re.findall(sm, txt):
        l = len( re.sub(r"[^\3Зз]+",'',s) )
        p = int ( round( math.tanh(l*n/k) *k ) )
        txt = txt.replace(s," SP"+str(p)+" ", 1)
        
    # X)
    n = 1.0
    sm = r"[XxХх]-*\)+"
    for s in re.findall(sm, txt):
        l = len( re.sub(r"[^\)]+",'',s) )
        p = int ( round( math.tanh(l*n/k) *k ) )
        txt = txt.replace(s," SP"+str(p)+" ", 1)

    # )))
    n = 1.0
    sm = r"\){2,}"
    for s in re.findall(sm, txt):
        l = len(s)
        p = int ( round( math.tanh(l*n/k) *k ) )
        txt = txt.replace(s," SP"+str(p)+" ", 1)
    
    # :*
    n = 1.5
    sm = r"[:;]-*\*+"
    for s in re.findall(sm, txt):
        l = len( re.sub(r"[^\*]+",'',s) )
        p = int ( round( math.tanh(l*n/k) *k ) )
        txt = txt.replace(s," SP"+str(p)+" ", 1)
    
    # <3
    n = 1.5
    sm = r"&lt\;[3З]+"
    for s in re.findall(sm, txt):
        l = len( re.sub(r"&lt;",'',s) )
        p = int ( round( math.tanh(l*n/k) *k ) )
        txt = txt.replace(s," SP"+str(p)+" ", 1)

    # :(
    n = 1.0
    sm = r"[:;=]-*\(+"
    for s in re.findall(sm, txt):
        l = len( re.sub(r"[^\(]+",'',s) )
        p = int ( round( math.tanh(l*n/k) *k ) )
        txt = txt.replace(s," SN"+str(p)+" ", 1)
 
    # X(
    n = 1.5
    sm = r"[xXхХ]-*\(+"
    for s in re.findall(sm, txt):
        l = len( re.sub(r"[^\(]+",'',s) )
        p = int ( round( math.tanh(l*n/k) *k ) )
        txt = txt.replace(s," SN"+str(p)+" ", 1)
    
    # ((
    n = 1.0
    sm = r"\({2,}"
    for s in re.findall(sm, txt):
        l = len(s)
        p = int ( round( math.tanh(l*n/k) *k ) )
        txt = txt.replace(s," SN"+str(p)+" ", 1)
    
    # :D
    n = 2.0
    sm = r"[:;=]-*D+"
    for s in re.findall(sm, txt):
        l = len( re.sub(r"[^D]+",'', s) )
        p = int ( round( math.tanh(l*n/k) *k ) )
        txt = txt.replace(s," SP"+str(p)+" ", 1)
    
    # :C
    n = 2.0
    sm = u"[:]-*[CСcс]+"
    for s in re.findall(sm, txt):
        l = len( re.sub(u"[^CСсc]+",'', s) )
        p = int ( round( math.tanh(l*n/k) *k ) )
        txt = txt.replace( s," SN"+str(p)+" ", 1)
    
    # ^_^
    n = 1.0
    sm = r"\^_*\^"
    for s in re.findall(sm, txt):
        l = len( re.sub(r"[^_]+",'', s) )
        p = int ( round( math.tanh(l*n/k) *k ) )
        txt = txt.replace(s," SP"+str(p)+" ", 1)
    
    # T_T 
    n = 2.0
    sm = u"[TТ]_*[TТ]"
    for s in re.findall(sm, txt):
        l = len( re.sub(r"[^_]+",'', s) )
        p = int ( round( math.tanh(l*n/k) *k ) )
        txt = txt.replace(s," SN"+str(p)+" ", 1)
    
    # *_*
    n = 1.5
    sm = r"\*_*\*"
    for s in re.findall(sm, txt):
        l = s.count("_")
        p = int ( round( math.tanh(l*n/k) *k ) )
        txt = txt.replace(s," SP"+str(p)+" ", 1)

    # >_<
    n = 1.5
    sm = r"&gt;_*&lt;"
    for s in re.findall(sm, txt):
        l = s.count("_")
        p = int ( round( math.tanh(l*n/k) *k ) )
        txt = txt.replace(s," SP"+str(p)+" ", 1)
    
    # o_o
    n = 0.5
    sm = u"[OoОо0]_*[OoОо0]"
    for s in re.findall(sm, txt):
        l = len( re.sub(r"[^_]+",'', s) )
        p = int ( round( math.tanh(l*n/k) *k ) )
        txt = txt.replace(s," SN"+str(p)+" ", 1)
    
    
    # single, not paired ( )
    if txt.count("(") != txt.count(")"):
        txt = txt.replace("(", " SN1 ").replace(")", " SP1 ")
        
    return txt

def dedigit(txt):
    return re.sub(r"([-+]*[0-9]+[-:.,хx/]*)+", " DGT ", txt)

def dehash(txt):
    return txt.replace("#", " HSH ");

for l in stdin:
    print("-"*10)

    l = cleanup(l)
    
    s = deurl(l)
    s = denick(s)
    s = dedigit(s)
    s = resmile(s)
    # s = dehash(s)
    s = cleanup(s)
    
    w = tokenize(s)
    
    print(l)
    print(s)
    print("|".join(w).encode("utf-8"))
    
    #p = morph.parse(l)
    #print(p[0].normal_form.encode("utf-8"))
    
