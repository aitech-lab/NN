#!/usr/bin/iced

fs = require "fs"

RNN = require "./RNN"

# vocabulary size
vs = 100
hs = 100

data = fs.readFileSync("data/input.txt").toString("utf8")
lines = data.split("\n").map (l)-> "BGN #{l} END"
words = lines.map (l)-> l.split /[^a-zA-Z]+/g
stat = {} 
words.map (l)-> l.map (w)-> stat[w]?=0; stat[w]++ 
stat = ([n,v] for n,v of stat).sort((a, b)-> b[1] - a[1])[0...vs-1]
stat.push ["UNK",0]
word_id = stat.reduce ((a,b,i)->a[b[0]]=i;a),{}

tarin_words = words.map (l)->
    l.map (w)->
        id = word_id[w]
        id?= word_id["UNK"]
        id
X = tarin_words.map (l)->l[0..-2]
Y = tarin_words.map (l)->l[1..-1]

rnn = new RNN vs, hs

rnn.calculate_loss X,Y