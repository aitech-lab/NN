#!/usr/bin/iced

Twitter = require "twitter"
cfg = require "./config"

twitter = new Twitter cfg.twitter
query = 
    track: 'и,я,он,мне'

await twitter.stream 'statuses/filter', query, defer stream

cb = null 
stream.on 'data', (event)->
    return unless event?.text
    cb event.text

stream.on 'error', (error)->
    console.log error
    # process.exit 0 

module.exports = 
    set_callback: (c)-> cb = c