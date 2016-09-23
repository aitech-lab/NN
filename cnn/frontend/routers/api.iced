
cfg = require "../config"

express = require "express"
darknet = require "../darknet"

router = express.Router()

fs      = require "fs"
multer  = require 'multer'
storage = multer.memoryStorage()
upload  = multer dest: "./uploads/"

router.post "/upload", upload.single("photo"), (req, res)->

    f = req.file
    return res.send "err" unless f

    ext = f.originalname.split('.')[-1..]
    hash_ext = "#{f.path}.#{ext}"
    fs.renameSync f.path, hash_ext
    res.send "ok"

    darknet.add_image hash_ext

module.exports = router
