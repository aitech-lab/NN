#!/usr/bin/iced

rl = require('readline');
rl = rl.createInterface 
  input: process.stdin,
  # output: process.stdout

words = {}
k=0
on_line = (l)->
    console.error k unless (++k)%10000
    l = l.replace /[^а-яА-ЯёЁ]+/g, " " 
    l = l.replace /\s{2,}/g," "
    w = l.split /\s+/g
    w = w.map (a)->a.toLowerCase()
    w.map (a,i)-> words[a]++||words[a]=1 

on_close= ()->
   list = ([w,v] for w, v of words).sort (a,b)->b[1]-a[1]
   for w in list
       console.log "#{w[1]}\t#{w[0]}"
       # console.log "#{w[0]}"
       
rl.on "line", on_line
rl.on "close", on_close

