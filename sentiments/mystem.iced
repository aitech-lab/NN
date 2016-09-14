#!/usr/bin/iced

spawn = require('child_process').spawn

mystem = spawn './mystem'

mystem.stdin.write "В лесу родилась ёлочка\n"

mystem.stdout.on 'data', (data)->
    console.log data.toString("utf-8")
    mystem.stdin.end()

mystem.stderr.on 'data', (data)->
    console.log data

mystem.on 'close', (code)->
    console.log code
