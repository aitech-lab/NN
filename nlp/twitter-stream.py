#!./env/bin/python
# coding=utf-8

from TwitterAPI import TwitterAPI
from config import twitter as cfg
import hashlib
import redis

import tokenizer as tk

rdb = redis.StrictRedis(host='localhost', port=5678, db=0)

api = TwitterAPI(
    cfg['consumer_key'       ], 
    cfg['consumer_secret'    ], 
    cfg['access_token_key'   ], 
    cfg['access_token_secret'])

# query = {'location': '37.363697,55.512489,37.870326,55.969110'}
query = {'track': u"и,не,я,в,а,на,с,у,как,ты,меня,так,мне,все,но,ну,по,то,за,да,вот,уже,сегодня,тебя,же,бы,ещё,мы,к"}
stream = api.request('statuses/filter', query)
def md5(t):
    return hashlib.md5(t.encode('utf-8')).hexdigest()

def save_tweet(t):
    
    m = md5(t)
    has = rdb.sismember("filter", m)
    if has == 1:
        print("// REPEAT //")
        return
 
    
    t = tk.deurl(t)
    t = tk.denick(t)
    t = tk.dedigit(t)
    t = tk.desmile(t)
    t = tk.deemoji(t)
    t = tk.depunct(t)
    t = tk.cleanup(t)
    l = tk.tokenize(t)

    rdb.rpush('tweets', t)
    rdb.sadd('filter', m)
    
    f = filter(lambda a: a != ' ', l)
    rdb.lpush("morph", " ".join(list(f)))
    
    for w in l:
       rdb.zincrby('word_stat', w, 1)
       
    print(t)
     
for tweet in stream:
    if 'text' in tweet:
        save_tweet(tweet['text'])        
