import os
from keras import backend as K
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, LSTM
from keras.layers import BatchNormalization, LeakyReLU
from keras.regularizers import l2
from keras.layers.convolutional import Conv1D, MaxPooling1D


def rmse(y_true, y_pred):
    return K.sqrt(K.mean(K.square(y_pred - y_true))) 


def createdir(dir):
	try:
		os.mkdir(dir)
	except OSError:
		pass


def buildmodel(timestep, lookback, mtype='cnn', modelpath=None):
    # build neural network using Keras python machine learning library
    model = Sequential()
    model.add(BatchNormalization())

    if mtype == 'dnn':
        model.add(Dropout(0.2))
        model.add(Dense(512, input_dim=timestep, activity_regularizer=l2(0.01)))
        model.add(LeakyReLU()) 
        model.add(Dropout(0.3))
        model.add(Dense(256, activity_regularizer=l2(0.01)))
        model.add(LeakyReLU())
        model.add(Dropout(0.1))
        model.add(Dense(128, activity_regularizer=l2(0.01)))
        model.add(LeakyReLU())

    elif mtype == 'cnn':
        model.add(Conv1D(filters=64, kernel_size=2, activation='relu', input_shape=(timestep, lookback)))
        model.add(MaxPooling1D(pool_size=2))
        model.add(Conv1D(filters=64, kernel_size=2, activation='relu'))
        model.add(MaxPooling1D(pool_size=2))
        model.add(Flatten())
        model.add(Dropout(0.2))
        model.add(Dense(512, activation='relu'))
        model.add(Dropout(0.3))
        model.add(Dense(256, activation='relu'))
        model.add(Dropout(0.1))
        model.add(Dense(128, activation='relu'))

    elif mtype == 'lstm':
        model.add(Dropout(0.2))
        model.add(LSTM(512, activation='relu', return_sequences=True, input_shape=(timestep, lookback)))
        model.add(Dropout(0.3))
        model.add(LSTM(256, activation='relu', return_sequences=True))
        model.add(Dropout(0.1))
        model.add(LSTM(128, activation='relu'))
    
    # last output layer
    model.add(Dense(units=1, activation='linear'))

    # load model weights
    if modelpath != None:
        model.load_weights(modelpath)

    # compile the neural network model
    model.compile(loss='mse', optimizer='adam')

    # return neural network model
    return model