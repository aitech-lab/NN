spawn = require('child_process').spawn

params = 
    encoding: "utf-8"
    env: process.env 
    cwd: "../python"
    stdio:['pipe', 'pipe', 'pipe']

keras = spawn '/home/peko/Projects/nn/sentiments/python/env/bin/python', ["-u", "predict-pipe.py", "out/final.h5"], params

# console.log process.env

cb = null
keras.stdout.on 'data', (data)->
    console.log "stdout: #{data}"
    cb?(data)

keras.stderr.on 'data', (data) ->
    console.log "stderr: #{data}"
    cb?(data)

keras.on 'close', (code)->
    console.log "child process exited with code #{code}"
    cb?(code)
    process.exit -1

keras.on 'error', (err)->
    console.error "ERROR"
    console.error err
    process.exit -1

predict = (text)->keras.stdin?.write "#{text}\n"
setcb = (c)-> cb = c

module.exports = 
    predict: predict
    setcb  : setcb