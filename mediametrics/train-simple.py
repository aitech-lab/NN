#!./env/bin/python3
# coding=utf-8

import sys

if len(sys.argv) != 2:
    print("Usage:\n\t./train.py train_data")
    print("Data format:\n\tY0 [tab] X0 [tab] X1 [tab] ... Xn")
    sys.exit(0)

import numpy as np

from keras.preprocessing     import sequence
from keras.utils             import np_utils
from keras.models            import Sequential
from keras.layers.core       import Dense, Dropout, Activation
from keras.layers.embeddings import Embedding
from keras.layers.recurrent  import LSTM
from keras.callbacks         import ModelCheckpoint

print("Params:")
print(sys.argv)

samples_max  = 200000
# vocabulary size
max_features = 60500
# words in sequence
maxlen       = 25
# samples for descent
batch_size   = 32

train = sys.argv[1]

def load_data(file): 
    x_data = []
    y_data = []
    
    samples_cnt = 0

    for l in open(file, "r"):
        d = l.split("\t")
        
        y = float(d[0])

        x = [int(x) for x in d[1:]]
        
        x_data.append(x)
        y_data.append(y)

        samples_cnt+=1
        if samples_cnt>=samples_max:
            break

    x_data = np.array(x_data)
    y_data = np.array(y_data)
    return (x_data, y_data)

x_train, y_train = load_data(sys.argv[1])

print("Loading {} train cases from '{}' complete".format(len(x_train), sys.argv[1]))

print('Pad sequences (samples x time)')
x_train = sequence.pad_sequences(x_train, maxlen=maxlen)

print("x_train shape:", x_train.shape)
print("y_train shape:", y_train.shape)

model = Sequential()
model.add(Embedding(max_features, 128, input_length=maxlen))
model.add(LSTM(128, return_sequences=True))
model.add(LSTM(128))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

              
checkpointer = ModelCheckpoint(filepath="out/checkpoint.{epoch:02d}.h5", verbose=1)
model.fit(
    x_train, y_train,
    validation_split=0.1,
    # validation_data=(x_test, y_test), 
    batch_size=batch_size, 
    nb_epoch=100,
    verbose=1,
    shuffle=True,
    callbacks=[checkpointer]
)

print("Save model")
model.save("out/final.h5")
