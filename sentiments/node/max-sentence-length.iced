#!/usr/bin/iced

_ = console.log 

if process.argv.length != 3
    _ "Usage:\n\t#{__filename.split("/")[-1..]} intput"
    process.exit 0

inp_name = process.argv[2]

fs = require "fs"
readline = require "readline"

rl = readline.createInterface
    input: fs.createReadStream inp_name
maxlen = 0
minlen = 1000
rl.on "line", (l)->
    len = l.split("\t").length
    maxlen = len if len > maxlen
    minlen = len if len < minlen

rl.on "close", ()->
    _ "max sentence length is #{maxlen-1}"
    _ "min sentence length is #{minlen-1}"