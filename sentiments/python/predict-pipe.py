#!./env/bin/python3
# codding=utf-8

import sys
# sys.path.append('/home/user/python-libs')

import io

if len(sys.argv) != 2:
    print("Usage:\n\tpredict.py model.h5")
    sys.exit(0)
    
from keras.models import load_model
from keras.preprocessing import sequence
import numpy as np

from slang import cleanup
import vocabulary as voc
voc.init()

model = load_model(sys.argv[1])

stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
sys.stdout.write("Ready for input:\n")
for l in stdin:
    enc = voc.encode(l)
    x = np.array([enc[1][0:40]])
    x = sequence.pad_sequences(x, maxlen=40)
    p = model.predict_proba(x, verbose=0)
    sys.stdout.write(
        "{:3.2}\t{:3.2}\t{}\t{}\n".format(
        0.5+enc[0]/20.0, 
        p[0][0], voc.decode(enc[1]), l)
    )
