#!/usr/bin/iced

fs = require 'fs'

spawn = require('child_process').spawn

mystem = spawn './mystem', [
    "-l", 
    # "--filter-gram","A"
    "--format", "json"
]

tweets = fs.readFileSync("./data/tweets-1k.csv").split("\n")

writeNext = ()->
    console.log "." while mystem.stdin.write(tweets.pop())

# mystem.stdin.on 'drain', writeNext
    
mystem.stdout.on 'data', (data)->
    data = data.toString("utf-8")
    console.log data
    json = JSON.parse(data)
    console.log json

# mystem.stderr.on 'data', (data)->
#     console.log data

mystem.on 'close', (code)->
    console.log code

writeNext()