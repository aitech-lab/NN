#!/usr/bin/iced

_ = console.log 

if process.argv.length != 4
    _ "Usage:\n\t#{__filename.split("/")[-1..]} vocabulary.tsv text_to_encode.txt"
    process.exit 0

voc_file  = process.argv[2]
text_file = process.argv[3]

Voc = require "./vocabulary"
voc = new Voc voc_file, 10

fs = require "fs"

encoded_text = fs.readFileSync(text_file)
    .toString("utf-8")
    .split("\n")
    .map((l)->
        [text, score] = l.split("\t")
        return null unless text? and score?
        enc = voc.encode_line(text).filter (c)-> c>0
        "#{score}\t#{enc.join("\t")}")

# _ voc.size()
for l in encoded_text
    _ l