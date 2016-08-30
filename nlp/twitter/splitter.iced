#!/usr/bin/iced

rl = require('readline');

rl = rl.createInterface 
  input: process.stdin,
  # output: process.stdout

on_line = (l)->
    l = l.replace /http:[^\s]+/g, ""
    l = l.replace /@[^\s]+/g    , ""

    l = l.replace /\s{2,}/g," "
    l = l.replace /^\s/g,""

    console.log l

rl.on "line", on_line