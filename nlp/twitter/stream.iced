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



require "colors"
Twitter = require "twitter"

cfg = require "./config"

positive_emoji = /😁|😂|😃|😄|😅|😆|😉|😊|😋|😌|😍|😏|😘|😚|😜|😝|😸|😹|😺|😻|😼|😽|☺|♥|⭐|🎉|💋|💓|💕|💖|😀|😇|😈|😎|😗|😙|😛/g
negative_emoji = /😒|😓|😔|😖|😞|😠|😡|😢|😣|😤|😥|😨|😩|😪|😫|😭|😰|😱|😲|😳|😵|😷|😾|😿|🙀|💔|😟|😦|😧|😮|😯|😐|😑|😕/g
console.log cfg.twitter
twitter = new Twitter cfg.twitter

query = 
    language:"ru"
    track: 'и'
    # locations: "37.6,55.75"

await twitter.stream 'statuses/filter', query, defer stream
  
stream.on 'data', (event)->
    return unless event?.text
    t = event.text.replace /\n|\s{2,}/g, " "
    t = t.replace /@[^\s]+/g, "NIK"
    t = t.replace /http[^\s]+/g, "URL"
    t = t.replace /#[^\s]+/g, "HTG"
    t = t.replace /[0-9]+/g, "0"
    # console.log t.replace /RT|HTG|URL|NIK|0/g, "#".green

    caps = t.match(/[А-Я,\s]{4,}/g)?.join("")
    # console.log caps if caps

    excl = t.match(/!+/g)?.join("")
    # console.log excl if excl
    
    quest = t.match(/\?+/g)?.join("")
    # console.log quest if quest

    # joint spread
    spread =t.match(/((?:\s)|^)([а-яА-ЯЁё]\s){4,}[а-яА-ЯЁё]/g)
    if spread
        for s in spread
            r = s.replace(/\s/g,"")
            t=t.replace s, " #{r}" 

    smiles = []
    smiles.concat t.match(/[:;]{0,1}-{0,1}\)+/g)||[]
    smiles.concat t.match(/\:D/g)||[]
    # smiles.concat t.match(positive_emoji)||[]
    console.log t, smiles if smiles.length

stream.on 'error', (error)->
    console.log error
    process.exit 0 
