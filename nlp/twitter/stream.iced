#!/usr/bin/iced

###
    streaming api only works with proper local time
    correct it with 'ntpd -qg'

    https://dev.twitter.com/streaming/overview/request-parameters
    https://dev.twitter.com/overview/api/response-codes
###

###

Phenomens:
    emoticons
        simple
        japanese
        repeated
        unicode
    characters

    repeated punctuation
    sparsed characters
###

Twitter = require "twitter"
cfg = require "./config"

require "colors" 
emoji = /([\uE000-\uF8FF]|\uD83C[\uDF00-\uDFFF]|\uD83D[\uDC00-\uDDFF]|\uD83D[\uDE00-\uDE4E]|[\u2700-\u27BF]|\ud83c[\udf00-\udfff]|\ud83d[\udc00-\uddfe])/g
emoji_sentiments = require "./emoji_sentiments"

# console.log cfg.twitter

twitter = new Twitter cfg.twitter

query = 
    track: 'и,я,он,мне'
    # locations: "37.6,55.75"

await twitter.stream 'statuses/filter', query, defer stream

k = 10.0
norm = (l, n)->
    Math.round(Math.tanh(l*n/k)*k)

desmile = (t)->
    
    # :) 
    m = t.match(/[:;=xXхХ]+-*[\)]+/g)||[]
    for s in m
        l = s.replace(/[^\)]+/g,'').length
        p = norm l, 1.0
        t = t.replace s, " #{p}) "
    
    # :3
    m = t.match(/[:]+-*[3зЗ]+/g)||[]
    for s in m
        l = s.replace(/[^Зз3]+/g,'').length
        p = norm l, 1.0
        t = t.replace s, " #{p}) "
    
    # :( :/ :\
    m = t.match(/[:;=xXхХ]+-*[\(\\\/]+/g)||[]
    for s in m
        l = s.replace(/[^\(\\\/]+/g,'').length
        p = norm l, 1.0
        t = t.replace s, " #{p}( "

    # :D :*
    m = t.match(/[:;=xXхХ]+-*[D\*]+/g)||[]
    for s in m 
        l = s.replace(/[^D\*]+/g,'').length
        p = norm l, 2.0
        t = t.replace s, " #{p}) "
    t

unknown_emoji = {}

# assumes point > 0xffff
# http://crocodillon.com/blog/parsing-emoji-unicode-in-javascript
emoji_regex = (point)->
    if point > 0xFFFF
        offset = point - 0x10000
        lead = 0xd800 + (offset >> 10)
        trail = 0xdc00 + (offset & 0x3ff)
        new RegExp "\\u#{lead.toString(16)}\\u#{trail.toString(16)}"
    else
        new RegExp "\\u#{point}"

deemoji = (t)->
    m = t.match(emoji)||[]
    console.log "#{t} => [#{m.join("")}]" if m.length
    for s in m 
        # console.log s.codePointAt(0).toString(16), s
        code = s.codePointAt(0)
        sent = emoji_sentiments[code]
        if true #sent
            # p = Math.round 3.0*sent[3]
            r = emoji_regex code
            t = t.replace r, "#".red
            # t = t.replace(r, ")".repeat( p)) if p>0    
            # t = t.replace(r, "(".repeat(-p)) if p<0    
    console.log t if m.length
    
    m = t.match(emoji)||[]
    for s in m 
        # console.log t
        hex = s.codePointAt(0).toString(16)
        unless unknown_emoji[hex]
            console.log "    0x#{hex}: [ 0.0  , 0.0  , 0.0  , 0.0  ] # #{s}"
            unknown_emoji[hex] = 1
    t

tokenize = (t)->
    t = t.replace /\n/g, ' '
    # console.log "\n#{t}"
    
    t = t.replace /http[^\s]+/g, 'url'
    t = t.replace /@[a-zA-Z_\d]+/g, '@'
    t = t.replace /([\-+]*\d+[\s\/.-:]*)+/g, " # "

    t = deemoji t
    t = desmile t

    t = t.replace /\s{2,}/g, ' '
    t = t.replace /^\s/g, ''

    # t = t.split /\s/g
    # console.log t

stream.on 'data', (event)->
    return unless event?.text

    tweet = event.text
    tokenize tweet

stream.on 'error', (error)->
    console.log error
    process.exit 0 
