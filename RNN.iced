# recomended random filler for neural matrices 
# -1/sqrt(n) ... 1/sqrt(n), where n - size of previous layer
rndsq = (s)-> ()-> (Math.random()-0.5)*2/Math.sqrt(s)

# generate matrix filled with f()
matf = (h, w, f)-> [0...h].map -> [0...w].map -> f()

# generate matrixe filed with 0
zeros = (h, w)-> [0...h].map -> [0...w].map -> 0

# dot multiply of 2 matrices
dot = (a, b)->
    # a width must be equal b height
    return null unless a[0].length is b.length 
    a.map (r)->
        [0...b[0].length].map (i)->
            r.reduce ((u, v, j)->u + v*b[j][i]), 0

# sum of 2 matrices
sum = (a, b)->
    a.map (r, i)->
        r.map (v, j)-> v+b[i][j]

# get tanh
tanh = (a)-> a.map (r)-> r.map (v)-> Math.tanh(v)

# map f to all elements
map = (a, f)-> a.map (r)-> r.map f

# softmax = e ^ x / sum(e ^ x)
# http://stackoverflow.com/questions/34968722/softmax-function-python
softmax = (a)->
    # sum e^x
    s = a.reduce ((v1,v2)-> v1+v2.reduce ((w1,w2)-> w1+Math.exp(w2)), 0), 0
    # map x/sum
    map a, (v)->Math.exp(v)/s

# get col of matrice
col = (a, c)-> a.map (r)->r[c..c]

# return column with max row values
maxcol = (a)-> a.map (r)->[r.indexOf Math.max(r...)]

# get size of matrix
size = (a)-> [a?.length, a[0]?.length]

# a = [[1,2,3],[4,5,6],[7,8,9]]
# console.log col(a,-1), col(a,1) 
# console.log softmax [[3.0,1.0,0.2]] => [ 0.8360188   0.11314284  0.05083836]

###

RNN structure

output    y     y
        V ↑     ↑
hidden  W h→ … →h
        U ↑     ↑
input     x     x

Y [vs : n  ]
V↑[vs : hs ]
H [hs : n+1]→W[hs : hs]
U↑[hs : vs ]
X [vs : n  ]

h[i] = tanh( U*x[i] + W*h[i-1] )
y[i] = softmax( V*h[i] )

###


class RNN


    # @vs - vocabulary size
    # @hs - hidden layer size
    constructor: (@vs, @hs)->

        @U = matf @vs, @hs, rndsq @vs 
        @V = matf @hs, @vs, rndsq @hs
        @W = matf @hs, @hs, rndsq @hs
    
    # X - sentence vector, contains vocabulary ids
    forward_propagation: (x)=>
        
        # sentence size, number of timesteps
        n = x.length
        h = zeros n+1, @hs
        y = zeros n  , @vs

        # iterate throught columns
        for id, i in x
            Ux = @U[id..id]
            Wh = dot h[i-1..i-1], @W
            h[i] = tanh(sum(Ux, Wh))[0]
            y[i] = softmax(dot(h[i..i], @V))[0]
        
        [y, h]

    predict: (x)=>
        [y, h] = @forward_propagation x
        maxcol y

    calculate_total_loss: (x, y)=>
        L = 0
        y.map (r, i)=>
            [yp, h] = @forward_propagation x[i]
            correct_prediction = r.map (id, j)-> yp[j][id]
            L+= -1 * correct_prediction.reduce ((u,v)->u+Math.log(v)),0
        L
    calculate_loss: (x, y)=>
        N = y.reduce ((v, w)-> v+w.length), 0  
        @calculate_total_loss(x,y)/N

module.exports = RNN