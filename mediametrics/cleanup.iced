re1 = /\|.*}|&.*?;|[\[\]\(\)\{\}.,:;!?\/\\«»0-9]|\\s/g
re2 = /[^а-яА-Яa-zA-Z0-9 \-]+/g
dash = /\s[-\u2012\u2013\u2014\u2015]|[-\u2012\u2013\u2014\u2015]\s|^[-\u2012\u2013\u2014\u2015]|[-\u2012\u2013\u2014\u2015]$/g
spaces = /\s{2,}/g

module.exports = (text)->
    text.replace(re1   , "")
        .replace(re2   , "")
        .replace(dash  , "")
        .replace(spaces, "")
        .trim().toLowerCase()