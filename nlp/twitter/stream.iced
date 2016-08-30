#!/usr/bin/iced

Twitter = require "twitter"

cfg = require "./config"

console.log cfg.twitter
twitter = new Twitter cfg.twitter

await twitter.stream 'statuses/filter', {track: 'javascript'}, defer stream
  
stream.on 'data', (event)->
    console.log event && event.text
 
stream.on 'error', (error)->
    console.log error
    process.exit 0 
