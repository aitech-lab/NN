#!/usr/bin/python
# coding=utf-8

import io
import sys
import codecs
import re
import math

def tokenize(txt):
    w = re.split(r"(\s+|[\"\'%!?.,:;\)\(=\d]+)", txt)
    return filter(lambda a:len(a), w)  
    
def cleanup(txt):
    txt = re.sub(r"\n|^\s+", '' , txt)
    txt = re.sub(r"\s+"    , ' ', txt)
    return txt

def deurl(txt):
    return re.sub(r"http[^\s]+", "URL", txt)

def denick(txt):
    return re.sub(r"@[^\s]+", "NICK", txt)


def depunct(txt):
    k = 10.0
    n = 1.0
    
    # !!! ??? ... -> !3 ?3 .3 
    for s in re.findall(r"!{2,}|\?{2,}|\.{2,}", txt):
        l = len(s)
        p = int ( round( math.tanh(l*n/k) *k ) )
        c = s[0]
        txt = txt.replace(s, " "+c+str(p)+" ", 1)
    return txt
     
def desmile(txt):

    # k - activation power
    # n - power multiplier
    
    k = 10.0
    
    # :)
    n = 1.0
    sm = r"[:;=]-*\)+"
    for s in re.findall(sm, txt):
        l = len( re.sub(r"[^\)]+",'',s) )
        p = int ( round( math.tanh(l*n/k) *k ) )
        txt = txt.replace(s," )"+str(p)+" ", 1)
    
    # :3
    n = 1.0
    sm = r"[:;=]-*[3Зз]+"
    for s in re.findall(sm, txt):
        l = len( re.sub(r"[^\3Зз]+",'',s) )
        p = int ( round( math.tanh(l*n/k) *k ) )
        txt = txt.replace(s," )"+str(p)+" ", 1)
        
    # X)
    n = 1.0
    sm = r"[XxХх]-*\)+"
    for s in re.findall(sm, txt):
        l = len( re.sub(r"[^\)]+",'',s) )
        p = int ( round( math.tanh(l*n/k) *k ) )
        txt = txt.replace(s," )"+str(p)+" ", 1)

    # )))
    n = 1.0
    sm = r"\){2,}"
    for s in re.findall(sm, txt):
        l = len(s)
        p = int ( round( math.tanh(l*n/k) *k ) )
        txt = txt.replace(s," )"+str(p)+" ", 1)
    
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
        txt = txt.replace(s," )"+str(p)+" ", 1)

    # :( =/
    n = 1.0
    sm = r"[:;=]-*[\(/]+"
    for s in re.findall(sm, txt):
        l = len( re.sub(r"[^\(/]+",'',s) )
        p = int ( round( math.tanh(l*n/k) *k ) )
        txt = txt.replace(s," ("+str(p)+" ", 1)
 
    # X(
    n = 1.5
    sm = r"[xXхХ]-*\(+"
    for s in re.findall(sm, txt):
        l = len( re.sub(r"[^\(]+",'',s) )
        p = int ( round( math.tanh(l*n/k) *k ) )
        txt = txt.replace(s," ("+str(p)+" ", 1)
    
    # ((
    n = 1.0
    sm = r"\({2,}"
    for s in re.findall(sm, txt):
        l = len(s)
        p = int ( round( math.tanh(l*n/k) *k ) )
        txt = txt.replace(s," ("+str(p)+" ", 1)
    
    # :D
    n = 2.0
    sm = r"[:;=]-*D+"
    for s in re.findall(sm, txt):
        l = len( re.sub(r"[^D]+",'', s) )
        p = int ( round( math.tanh(l*n/k) *k ) )
        txt = txt.replace(s," )"+str(p)+" ", 1)
    
    # :C
    n = 2.0
    sm = u"[:]-*[CСcс]+"
    for s in re.findall(sm, txt):
        l = len( re.sub(u"[^CСсc]+",'', s) )
        p = int ( round( math.tanh(l*n/k) *k ) )
        txt = txt.replace( s," ("+str(p)+" ", 1)
    
    # ^_^
    n = 1.0
    sm = r"\^_*\^"
    for s in re.findall(sm, txt):
        l = len( re.sub(r"[^_]+",'', s) )
        p = int ( round( math.tanh(l*n/k) *k ) )
        txt = txt.replace(s," )"+str(p)+" ", 1)
    
    # T_T 
    n = 2.0
    sm = u"[TТ]_+[TТ]"
    for s in re.findall(sm, txt):
        l = len( re.sub(r"[^_]+",'', s) )
        p = int ( round( math.tanh(l*n/k) *k ) )
        txt = txt.replace(s," ("+str(p)+" ", 1)
    
    # *_*
    n = 1.5
    sm = r"\*_+\*"
    for s in re.findall(sm, txt):
        l = s.count("_")
        p = int ( round( math.tanh(l*n/k) *k ) )
        txt = txt.replace(s," )"+str(p)+" ", 1)

    # >_<
    n = 1.5
    sm = r"&gt;_+&lt;"
    for s in re.findall(sm, txt):
        l = s.count("_")
        p = int ( round( math.tanh(l*n/k) *k ) )
        txt = txt.replace(s," )"+str(p)+" ", 1)
    
    # o_o
    n = 1.0
    sm = u"[OoОо0]_+[OoОо0]"
    for s in re.findall(sm, txt):
        l = len( re.sub(r"[^_]+",'', s) )
        p = int ( round( math.tanh(l*n/k) *k ) )
        txt = txt.replace(s," ("+str(p)+" ", 1)
    
    return txt

def deemoji(txt):
    
    k = 10.0
    
    # 😉
    n = 1.0
    sm = u"[👍🎶❤😉😊😋😌😍😏😘😚😜😝😻😼😽☺♥⭐🎉💋💓💕💖😇😈😎😗😙😛]+"
    for s in re.findall(sm, txt):
        l = len(s)
        p = int ( round( math.tanh(l*n/k) *k ) )
        txt = txt.replace(s," )"+str(p)+" ", 1)
    
    # 😁
    n = 2.0
    sm = u"[😁😂😃😄😅😆😸😹😺😀]"
    for s in re.findall(sm, txt):
        l = len(s)
        p = int ( round( math.tanh(l*n/k) *k ) )
        txt = txt.replace(s," )"+str(p)+" ", 1)
    
    # 😔
    n =1.0
    sm = u"[😒😓😔😡😢😣😤😰😱😲😳😵😷😾😿💔😮😯😐😑😕]+"
    for s in re.findall(sm, txt):
        l = len(s)
        p = int ( round( math.tanh(l*n/k) *k ) )
        txt = txt.replace(s," ("+str(p)+" ", 1)
    
    # 😩
    n = 2.0   
    sm = u"[😞😠😥😨😩😪😫😭🙀😟😦😧😖]+"
    for s in re.findall(sm, txt):
        l = len(s)
        p = int ( round( math.tanh(l*n/k) *k ) )
        txt = txt.replace(s," ("+str(p)+" ", 1)

    return txt
    
def dedigit(txt):
    return re.sub(r"([-+]*[0-9]+[-:.,хx/]*)+", " DGT ", txt)

def dehash(txt):
    return txt.replace("#", " HSH ");

if __name__ == "__main__":
    
    # stdin = codecs.getreader("utf-8")(sys.stdin)
    stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
    for l in stdin:
    
        # l = cleanup(l)
        s = deurl(l)
        s = denick(s)
        s = dedigit(s)
        s = depunct(s)
        s = desmile(s)
        s = deemoji(s)
        
        # s = dehash(s)
        s = cleanup(s)
        
        w = tokenize(s)
        print("-"*40)
        print(l)
        print("|".join(w))
        
