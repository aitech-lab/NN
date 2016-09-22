
cfg = require "../config"

express = require "express"

router = express.Router()

# router.get "/getall", (req, res)->
#     res.send aggregators.getall()


# router.post "/add", (req, res)->
#     aggregators.add req.body
#     res.send "ok"

module.exports = router
