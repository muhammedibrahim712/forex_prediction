import time
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from keras.callbacks import ReduceLROnPlateau, ModelCheckpoint
from scipy.signal import savgol_filter
from os.path import splitext
from keras.models import load_model
from util import buildmodel, createdir
from preprocess import analyze
from trade import feed

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

# for direction indicator
TREND_UP = 'g'
TREND_DOWN = 'r'
STOP_LOSS = 5


def prepare(bid, quotecnt):
    # prepare dataset
    random.seed(54)
    length = len(bid)
    samplecnt = length - quotecnt
    stset = random.sample(range(length - quotecnt), samplecnt)

    # build train dataset
    X = []
    Y = []
    for st in stset:
        end = st + quotecnt
        X.append(bid[st:end])
        Y.append(bid[end])

    return np.array(X), np.array(Y)


def train(bid, lookback, modeltype, modelpath):
    # get train dataset
    X, Y = prepare(bid, lookback)

    # build the model
    print("[TRAIN] Training prediction model ...")

    start = time.time()
    samples = X.shape[0]
    timesteps = X.shape[1]

    if modeltype == 'cnn' or modeltype == 'lstm':
        X = X.reshape((samples, timesteps, 1))
    
    # build model
    nb_epochs = 20000
    createdir("../checkpoints")
    model = buildmodel(timesteps, 1, modeltype, modelpath)
    callbacks = [
		ReduceLROnPlateau(monitor='val_loss', factor=0.9, patience=10, min_lr=0.000001, verbose=1),
		ModelCheckpoint("../checkpoints/model.{epoch:04d}-{val_loss:.8f}.hdf5",
			monitor="val_loss",
			save_best_only=True,
			verbose=1,
			mode="auto")]

    history = model.fit(X, Y,
        verbose=1,
        epochs=nb_epochs,
        batch_size=128,
        shuffle=True,
        callbacks=callbacks,
        validation_split=0.20)

    createdir("../model/%s" % modeltype)
    model.save_weights("../model/%s/weight-%s.hdf5" % (modeltype, modeltype))
    model.save("../model/%s/model-%s.hdf5" % (modeltype, modeltype))

    end = time.time()
    print("[TRAIN] Done. Elapsed time is %.2f seconds" % (end - start))

    # show training log
    # plt.figure()
    # plt.plot(history.history["loss"], label="TRAIN")
    # plt.plot(history.history["val_loss"], label="TEST")
    # plt.legend()
    # plt.show()

    # return trained model
    return model


def predict(model, Xr):
    # prediction
    print("[PREDICT] Predict given dataset ...")

    start = time.time()
    Yp = model.predict(Xr, verbose=0)
    end = time.time()

    print("[PREDICT] Done. Elapsed time is %.2f seconds" % (end - start))

    # return prediction result
    return Yp


def mean(A, B):
    return (A + B) / 2


def main():
    os.system("cls")

    # read input csv dataset
    # filename = "EURUSD-201801-201809.csv"
    filename = "EURUSD-2018-09.csv"
    datestamp, bid, ask = analyze(filename, 5)
    body, _ = splitext(filename)
    mid = mean(np.array(bid), np.array(ask))

    # train stage
    lookback = 7
    modeltype = 'lstm'
    modelpath = "../model/%s/weight-%s.hdf5" % (modeltype, modeltype)
    # model = train(mid, lookback, modeltype, None)
    model = load_model("../model/%s/model-%s.hdf5" % (modeltype, modeltype))
    model.summary()

    # predict stage
    Yr, Yp = singlepredict(model, mid, lookback, modeltype)

    # plot output result (smoothed version)
    # Yr = savgol_filter(Yr, 151, 3, axis=0)
    # Yt = savgol_filter(Yp, 53, 3, axis=0)
    Yf = savgol_filter(Yp, 51, 5, axis=0)
    
    # graph visualization and create new indicator
    threshold = 0.5 * 1e-4
    direction = [TREND_UP]      # temporary
    arraylen = len(Yf)
    checkflag = False

    for i in range(1, arraylen):
        diff = Yf[i] - Yf[i-1]
        
        if diff > threshold:
            checkflag = False
            direction.append(TREND_UP)
        elif diff < -threshold:
            checkflag = False
            direction.append(TREND_DOWN)
        else:
            last = len(direction) - 1
            previous = direction[last]
            direction.append(previous)

    direction[0] = direction[1]
    feed(bid, ask, datestamp, direction)

    X = np.array(range(arraylen))

    # display two curve lines
    plt.figure()
    plt.plot(Yr, color="blue")
    plt.scatter(X, Yf, s=20, c=direction, marker='.')
    plt.xlabel("TIME")
    plt.ylabel("QUOTES")
    plt.title(body)
    plt.show()


def singlepredict(model, bid, lookback, modeltype):
    Xr = []
    Yr = []
    length = len(bid)

    for st in range(length - lookback):
        end = st + lookback
        Xr.append(bid[st:end])
        Yr.append(bid[end])

    # convert to numpy array
    Xr = np.array(Xr)
    Yr = np.array(Yr)
    
    samples = Xr.shape[0]
    timesteps = Xr.shape[1]

    if modeltype == 'cnn' or modeltype == 'lstm':
        # Xr = Xr.reshape((samples, timesteps, 1))
        Xr = Xr.reshape((samples, 1, timesteps))

    # return prediction result
    Yp = predict(model, Xr)
    return Yr, Yp[1:]


if __name__ == "__main__":
    main()