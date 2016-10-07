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

words = {}

re1 = /\|.*}|&.*?;|[\[\]\(\)\{\}.,:;!?\/\\«»0-9]|\\s/g
re2 = /[^а-яА-Яa-zA-Z0-9 \-]+/g
dash = /\s[-\u2012\u2013\u2014\u2015]|[-\u2012\u2013\u2014\u2015]\s|^[-\u2012\u2013\u2014\u2015]|[-\u2012\u2013\u2014\u2015]$/g
spaces = /\s{2,}/g

rl.on "line", (l)->
    [text, score] = l.split "\t"
    text = text
        .replace(re1   , "")
        .replace(re2   , "")
        .replace(dash  , "")
        .replace(spaces, "")
        .trim()
    
    w = text.split " "
    w.map (a)-> words[a] = words[a]+1 | 1
    # _ text, score

rl.on "close", ()->
    for n, v of words
        _ "#{n}\t#{v}"