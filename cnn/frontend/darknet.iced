spawn = require('child_process').spawn

params = 
    encoding: "utf-8"
    env: process.env
    cwd: "../darknet"
    stdio:['pipe', 'pipe', 'pipe']

#  ./darknet yolo test cfg/yolo.cfg nets/yolo.weights data/dog.jpg
darknet = spawn '../darknet/darknet', ["yolo", "test", "cfg/yolo.cfg", "nets/yolo.weights"], params

# console.log process.env

cb = null
darknet.stdout.on 'data', (data)->
    console.log "stdout: #{data}"
    if data.indexOf("Enter Image") >= 0
        cb?(data)

darknet.stderr.on 'data', (data) ->
    console.log "stderr: #{data}"
    cb?(data)

darknet.on 'close', (code)->
    console.log "child process exited with code #{code}"
    cb?(code)
    process.exit -1

darknet.on 'error', (err)->
    console.error "ERROR"
    console.error err
    process.exit -1

add_image = (file)->darknet.stdin?.write "../frontend/#{file}\n"
setcb = (c)-> cb = c

module.exports = 
    add_image: add_image
    setcb  : setcb
