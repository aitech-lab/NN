#!/usr/bin/iced

_ = console.log 

if process.argv.length != 5
    _ "Usage:\n\t#{__filename.split("/")[-1..]} intput postivie_out negative_out"
    process.exit 0

inp_name = process.argv[2]
pos_name = process.argv[3]
neg_name = process.argv[4]

fs = require "fs"
readline = require "readline"

pos = fs.createWriteStream pos_name
neg = fs.createWriteStream neg_name

rl = readline.createInterface
    input: fs.createReadStream inp_name

rl.on "line", (l)->
    score = parseFloat(l.split("\t", l)[0])
    _ score
    if score > 0.0
        pos.write "#{l}\n"
    else
        neg.write "#{l}\n"

rl.on "close", ()->
    pos.end()
    neg.end()