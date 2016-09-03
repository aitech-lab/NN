#!./env/bin/python3
# codding=utf-8

from keras.models import load_model
from keras.preprocessing import sequence
import numpy as np
import vocabulary as voc
voc.init()

model = load_model("output.h5")

x = np.array([voc.encode(u"Полная херня :("), voc.encode(u"Идите все в жопу уроды! Я вас ненавижу!")])
x = sequence.pad_sequences(x, maxlen=100)

print(x)
result = model.predict_proba(x)

print(result)
