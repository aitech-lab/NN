#!./env/bin/python3
# codding=utf-8

from keras.models import load_model
from keras.preprocessing import sequence
import numpy as np
import vocabulary as voc
voc.init()

model = load_model("out/final.h5")
tweets = [t for t in open("test-tweets.txt")]
x = np.array([voc.encode(t) for t in tweets])
x = sequence.pad_sequences(x, maxlen=100)

results = model.predict_proba(x)
for i, v in enumerate(results):
    print(v[0],"\t", tweets[i])
