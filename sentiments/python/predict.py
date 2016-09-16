#!./env/bin/python3
# codding=utf-8

from keras.models import load_model
from keras.preprocessing import sequence
import numpy as np

from slang import cleanup
import vocabulary as voc
voc.init()

if len(sys.argv) != 3:
    print("Usage:\n\tpredict.py model.h5 data.txt")

model = load_model(sys.argv[1])
tweets = [t for t in open(sys.argv[2], encoding="utf-8")]
x = np.array([voc.encode(t[0]) for t in tweets])
x = sequence.pad_sequences(x, maxlen=40)

results = model.predict_proba(x)
for i, v in enumerate(results):
    print(tweets[i][1], "\t", v[0], "\t", tweets[i][0])
