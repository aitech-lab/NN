#!/usr/bin/iced

fs  = require "fs"
csv = require "csv"
az  = require "az"

console.log process.argv
file = process.argv[2]
unless file
    console.error "Usage:\n\t#{__filename} input"
    process.exit -1
    
console.log "Parse file #{file}"

data = fs.readFileSync(file).toString("utf8")

await csv.parse data, {delimiter: ";"}, defer err, rows
await az.Morph.init 'node_modules/az/dicts', defer()
for row in rows
    tweet = row[3]
    words = tweet.split /[^а-яА-Я]+/
    for w in words
        console.log w
        console.log JSON.stringify az.Morph(w), null, 2
    
