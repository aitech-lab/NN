#!/usr/bin/iced

# last max score
# day-news-encoded.tsv
# 6.794968920066267

_  = console.log 
__ = console.error

if process.argv.length != 4
    _ "Usage:\n\t#{__filename.split("/")[-1..]} vocabulary.tsv text_to_encode.txt"
    process.exit 0

voc_file  = process.argv[2]
text_file = process.argv[3]

Voc = require "./vocabulary"
voc = new Voc voc_file, 10

fs = require "fs"

max_score = 0
scores = []
encoded_text = fs.readFileSync(text_file)
    .toString("utf-8")
    .split("\n")
    .map((l,i)->
        [text, score] = l.split("\t")
        score = Math.log10 parseInt score
        if score > 0
            max_score = Math.max max_score, score
        scores[i] = score

        return null unless text? and score?
        enc = voc.encode_line(text).filter (c)-> c>0
        "#{enc.join("\t")}")
    .filter((l)->l?.length>2)

__ max_score
for l,i in encoded_text
    _ "#{scores[i]/max_score}\t#{l}"