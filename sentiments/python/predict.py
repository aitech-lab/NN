#!./env/bin/python3
# codding=utf-8

import sys

if len(sys.argv) != 3:
    print("Usage:\n\tpredict.py model.h5 data.txt")
    sys.exit(0)
    
from keras.models import load_model
from keras.preprocessing import sequence
import numpy as np

from slang import cleanup
import vocabulary as voc
voc.init()

model = load_model(sys.argv[1])
tweets  = [t for t in open(sys.argv[2], encoding="utf-8")]
encoded = [voc.encode(t) for t in tweets]
x = np.array([e[1][0:40] for e in encoded])
x = sequence.pad_sequences(x, maxlen=40)

results = model.predict_proba(x)
for i, v in enumerate(results):
    print(
        "{:3.2}".format(0.5+encoded[i][0]/20.0)+"\t"
        voc.decode(ecoded[i][1]+"\t"
        "{:3.2}".format(v[0])+"\t"
        tweets[i], end="")
