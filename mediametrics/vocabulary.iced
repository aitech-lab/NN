fs = require "fs"

cleanup = require "./cleanup"

class Vocabulary
    
    constructor: (@voc_file, @min_score = 100)->
        @voc_a = ["UNK"]
        @voc = {}
        
        fs.readFileSync(@voc_file)
            .toString("utf-8")
            .split("\n")
            .map (l)=>
                [l, score] = l.split("\t")
                score = parseInt score
                if l?.length and score >= @min_score
                    @voc_a.push l
    
        for w, i in @voc_a
            @voc[w] = i
    
    encode_line:(text)=>
        text = cleanup text
        words = text.split " "
        @encode_word w for w in words
    
    encode_word:(word)=> 
        return @voc[word] if @voc[word]?
        return 0

    decode_line: (line)=> @voc_a[wid] for wid in line

    size: ()=> @voc_a.length

module.exports = Vocabulary