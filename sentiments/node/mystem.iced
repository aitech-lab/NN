#!/usr/bin/iced

fs = require 'fs'

spawn = require('child_process').spawn

mystem = spawn './mystem', [
    "-l", 
    "--format", "json"
]

console.error "Loading tweets"
tweets = fs.readFileSync("./data/tweets-1k.csv").toString("utf-8")
tweets = tweets.split("\n")
console.error "Loaded #{tweets.length} tweets"


norm = []
writeNext = ()->
    console.log "write start"
    loop
        t = tweets.pop()
        break unless tweets.length
        r = mystem.stdin.write("#{t}\n")
    mystem.stdin.end()
    console.log "write end"

mystem.stdout.on 'data', (data)->
    data = data.toString("utf-8").replace /\r|\n/g, ""
    data = data.replace(/\]\[/g, "]][[").split "]["
    for d, i in data
        try
            json = JSON.parse(d)
            norm.push json if json.length
            # console.log json
        catch err
            console.log err
            console.log i
            for d in data
                console.log "----"
                console.log d
            # process.exit 0

# mystem.stderr.on 'data', (data)->
#     console.log data

mystem.on 'close', (code)->
    console.log code
    console.log norm
    console.log norm.length

writeNext()