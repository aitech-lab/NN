#!/usr/bin/iced

rl = require('readline');

rl = rl.createInterface 
  input: process.stdin,
  # output: process.stdout

extract_smiles = (s)->
    p = n = 0

    # positive
    p += s.match(/\)/g).length
    p += (s.match(/:D/g).length + s.match(/D{2,}/g).join('').length)*2
    
    # negative
    n += s.match(/\(/g).length



on_line = (l)->
    l = l.replace /http:[^\s]+/g, "url"
    l = l.replace /@[^\s]+/g    , "usr"

    l = l.replace /\s{2,}/g," "
    l = l.replace /^\s/g,""

    console.log l

rl.on "line", on_line
