#!/usr/bin/iced

_ = console.log 

if process.argv.length != 3
    _ "Usage:\n\t#{__filename.split("/")[-1..]} data.tsv"
    process.exit 0

data_file  = process.argv[2]

fs = require "fs"
max = Math.max
max_length = fs.readFileSync(data_file)
    .toString("utf-8")
    .split("\n")
    .reduce ((a,b)->max(a, b.split("\t").length)), 0

console.log "max line length #{max_length}"