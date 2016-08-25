#!/usr/bin/coffee

fs = require "fs"

input      = "data/input.txt"

sart_token    = "sart_token"
end_token     = "end_token"
unknown_token = "unknown_token"

vs = 20 # vocabulary size
hs = 10  # hidden layer size

###

http://www.wildml.com/2015/09/recurrent-neural-networks-tutorial-part-2-implementing-a-language-model-rnn-with-python-numpy-and-theano/

Recuren Neural Network (RNN)
  
 X = y   y         y
     ↑   ↑         ↑
 H = h → h → ... → h 
     ↑   ↑         ↑
 Y = x   x         x

U = x->h
V = h->y
W = h->h

hi = tanh (U * xi + W * hi-1)
yi = softmax(W * hi)

vectors:
X = [vs]
Y = [vs] 
Z = [hs]

matrices:
U = [hs x vs]
V = [vs x hs]
W = [hs x hs]

###

# start random filling for matrices
rndsq =(s)-> ()->
    (Math.random()-0.5)*2.0/Math.sqrt(s)

softmax = (x)->
    math.div(
        math.exp(x),
        math.sum(math.exp(x))
    )

filled = (h, w, f)->
    [0...h].map ()->[0...w].map ()-> f()

zeros = (h, w)->
    [0...h].map ()->[0...w].map ()-> 0

# a[aw:ah] x b[bw:bh] = [aw:bh] 
#      ah<====>bw
mult = (a, b)->
    # with of a must be equal height of b
    return null unless a[0].length is b.length
    a.map (ar)->
        for j in [0...b[0].length]
            ar.reduce ((v, w, k)-> v + w*b[k][j]), 0

size = (a)-> [a.length, a[0].length]

class RNN

    constructor: (@vs, @hs)->

        @U = filled @hs, @vs, rndsq @vs
        @V = filled @vs, @hs, rndsq @hs
        @W = filled @hs, @hs, rndsq @hs

        console.log "U: [#{size @U}]"
        console.log "V: [#{size @V}]"
        console.log "W: [#{size @W}]"

    forward_propagation: (x)->

        # x = [vs:n]
        # y = [vs:n]
        # Ux = U[hs:vs] * x[vs:n] = [hs:n]
        # Wh = W[hs:hs] * h[hs:n] = [hs:n]
        # Vh = V[vs:hs] * h[hs:n] = [vs:n]
        # h = tanh(Ux+Wh) [hs:n]
        # y = softmax(Vh) [vs:n] 

        n = x.length
        h = zeros @hs, n+1
        y = zeros @vs, n
        
        for i in [0...n]
            # get column from U
            Ux = @U.map((r)->r[x])
            # h = H._data[i-1..i-1][0]
            # console.log H,h
            #  h = m.dotMultiply(@W, h)
            # H[i] = m.tanh(m.sum(u, h))
            # Y[i] = softmax(m.multiply(@V, H[i]))
            return [y, h]

    predict: (x)->

        [h, y] = @forward_propagation(x)
        m.max y, 1

data = fs.readFileSync input

lines = data.toString().split "\n"
lines = lines.map (l)-> "#{sart_token} #{l} #{end_token}"

console.log "Loaded #{lines.length} lines"
tokenized_lines = []
words_stat = lines.reduce ((a,b)->
    words = b.split(/[^a-zA-Zа-яА-Я_]+/g).map (w)->
        w = w.toLowerCase()
        a[w]?=0
        a[w]++
        w
    tokenized_lines.push words
    a
), {} 


words = ([w, v] for w, v of words_stat)
words = words.sort((a,b)->b[1]-a[1])
vocab = words[...vs-1]
vocab.push [unknown_token, 0]
vocab = vocab.map (w)->w[0]
word_to_index = vocab.reduce ((a,b,i)->a[b] = i; a), {}

console.log "Using vocabulary size #{vs}"

#encode
train_x = []
train_y = []
tokenized_lines = tokenized_lines.map (line)->
    line = line.map (word)->
        wid = word_to_index[word]
        wid?= vs-1
    train_x.push line[..-2]
    train_y.push line[1..]
    line

console.log train_x[0]
console.log train_y[0]

# rnn = new RNN vs, hs
# [y, h] = rnn.forward_propagation train_x[0]
# console.log y, h

