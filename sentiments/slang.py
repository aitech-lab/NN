#!/usr/local/bin/python3
# coding=utf-8

import re
from smile import resmile
from math import tanh

class C:
    HEADER       = '\033[95m'
    OKBLUE   = B = '\033[94m'
    OKGREEN  = G = '\033[92m'
    WARNING      = '\033[93m'
    FAIL     = R = '\033[91m'
    ENDC     = E = '\033[0m'
    BOLD         = '\033[1m'
    UNDERLINE    = '\033[4m'

def cleanup(l):

    txt, tone = resmile(l)
    
    # new lines
    txt = re.sub(r'\n', u' ', txt)
    # urls, nicks, spaces
    txt = re.sub(r'http[^\s]+|@[^\s]|^\s+|\s+$', r'', txt)
    
    # count !!!111
    excl=0
    for m in re.findall(r'![!1]*', txt):
        excl+=len(m)
    txt = re.sub(r'![!1]*', '', txt)
    
    # repitetive Mooooore, 
    txt = re.sub(r'([а-яА-ЯёЁ])(\1{2,})', r'\1', txt)
    
    # xaxaxa count
    xa = 0
    for m in re.findall(r'[AXaxАХах]{4,}', txt):
       xa+=len(m)
    txt = re.sub(r'[AXaxАХах]{4,}', '', txt)
    tone += xa

    txt = re.sub(r'([а-яА-ЯёЁс]{2,3})(\1{2,})', C.R+r'\1'+C.E, txt)
    
    # final cleanup
    txt = re.sub(r'[^а-яА-ЯёЁ]+'  , ' ', txt)
    txt = re.sub(r'\s-|-\s|^-|-$' , ' ', txt)
    txt = re.sub(r'^\s+|\s+$'     , '' , txt)
    txt = re.sub(r'\s{2,}'        , ' ', txt)

    tone = tone*(excl/2.0+1)
    tone = 10*tanh(tone/10)
    
    return (txt, tone)        


if __name__ == "__main__":
    
    import io
    import sys
                                
    stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
    for l in stdin:
        (txt, tone) = cleanup(l)
        print('\t', re.sub(r'\n','', l))
        if tone > 0: print(C.G, end='')
        if tone < 0: print(C.R, end='')
        print(round(tone), '\t', txt, C.E if tone!=0 else '')

