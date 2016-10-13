#!/usr/bin/iced

_ = console.log 

if process.argv.length != 3
    _ "Usage:\n\t#{__filename.split("/")[-1..]} input"
    process.exit 0

inp_name = process.argv[2]

fs = require "fs"
readline = require "readline"

rl = readline.createInterface
    input: fs.createReadStream inp_name

cleanup = require "./cleanup"
words = {}

rl.on "line", (l)->
    
    [text, score] = l.split "\t"
    text = cleanup text
    
    w = text.split " "
    w.map (a)->
        s = a.toLowerCase() 
        words[s] = words[s]+1 | 1
    # _ text, score

rl.on "close", ()->
    for n, v of words
        _ "#{n}\t#{v}"