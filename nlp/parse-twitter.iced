#!/usr/bin/iced

fs  = require "fs"
csv = require "csv"

console.error process.argv
file = process.argv[2]
unless file
    console.error "Usage:\n\t#{__filename} input"
    process.exit -1
    
console.error "Parse file #{file}"

data = fs.readFileSync(file).toString("utf8")

await csv.parse data, {delimiter: ";"}, defer err, rows

for row in rows
    tweet = row[3].replace /\r\n|\r|\n|\n\r|\t/g, " "
    console.log "#{tweet}"
    
