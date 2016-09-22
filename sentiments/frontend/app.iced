#!/usr/bin/iced

express = require "express"
socket  = require "socket.io"
stylus  = require "stylus"
coffee  = require "coffee-middleware"
nib     = require "nib"
http    = require "http"
bp      = require "body-parser"


try cfg = require "./config"
catch err
    console.error "Copy config.txt to config.iced"
    process.exit 1

api  = require "./routers/api"

app = express()
srv = http.Server app
io  = socket srv

console.log "Listen #{cfg.port}"
srv.listen cfg.port

compile = (str, path)->
    stylus(str)
    .set("filename", path)
    .use(nib())

app.set "views"      , "#{__dirname}/views"
app.set "view engine", "jade"

# post request
app.use bp.json()
app.use bp.urlencoded extended: true 

app.use stylus.middleware
    src: "#{__dirname}/public"
    compile: compile

app.use coffee
    src: "#{__dirname}/public"
    compress: true

app.use "/api" , api

app.use express.static "#{__dirname}/public"

app.get "/", (req,res)->
    res.render "index",
        title: "index"
        req  : req
        cfg  : cfg

app.get "/aggr/:name", (req, res)->
    a = aggregators.get req.params.name
    return res.render "404" unless a

    res.render "aggregation",
        cfg: cfg
        aggr: a

console.log cfg

    
# SOCKETS
keras = require "./keras"
keras.setcb (data)->
    io.emit "text", data.toString("utf-8")

io.on "connection", (socket)->

    socket.on "text", (msg)->
        console.log "text: #{msg}"
        keras.predict msg


