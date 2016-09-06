#!/usr/bin/iced

###
   
   Modern Language features extractor
   
   Features
     Repeated letters
     Sparsed text
     Smiles
       Regular
       Japanese
       Emoji
        
###

_ = console.log

parse_sentence = (s)->
tokenize = (s)->
    m = /[russian]+(-[russian]+)*|[a-zA-Z]+(-[a-zA-Z]+)*|!+|?+|\.+/g
    _ s.match m
