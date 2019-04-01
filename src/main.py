
# ==> import to the virtual environment that will run this code:
# - keras
# - keyboard
# - v20
# - matplotlib
# - datetime

from keras.models import load_model

from threading import Thread
from dateutil import parser
from scipy.signal import savgol_filter
from PyQt5 import QtCore, QtGui, QtWidgets

from oanda import getAPI, getLatestPrice
from gui import UiMainWindow
from trade import feed

# import pyqtgraph as pg
import numpy as np
import datetime, time
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


# for direction indicator
TREND_UP = 'g'
TREND_DOWN = 'r'
STOP_LOSS = 5

# pyrcc5 -o res_rc.py assets/res.qrc
# pyuic5 -x application.ui -o gui.py

class ForexFeed(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = UiMainWindow()
        self.ui.setupUi(self)
        
        self.path = QtGui.QPainterPath()
        
        self.latest = None
        # self.pen = QtGui.QPen(QtCore.Qt.red)
        self.data = []
        self.tick = []

        # self.ui.historyChart.AxisItem.tickStrings()
        self.ui.historyChart.setXRange(0, 25)
        
        self.lookback = 7
        self.modeltype = 'lstm'
        self.model = load_model("../model/%s/model-%s.hdf5" % (self.modeltype, self.modeltype))

        self.thread = Thread(target=self.livefeed, args=())
        self.thread.daemon = True
        self.thread.start()
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(5 * 1000)
        try:
            self.timer.timeout.connect(self.apply)
        except ValueError:
            print("Issue from livefeed instruction", ValueError)

        os.system("cls")
        print("Started at {} Please wait ...".format(datetime.datetime.utcnow()))


    def start(self):
        self.timer.start()


    def stop(self):
        self.timer.stop()


    # @QtCore.pyqtSlot()
    def apply(self):
        try:
            self.data.append([self.bid, self.ask])
            
            print("No : {}, Current status : ({}, {})".format(len(self.data), self.bid, self.ask))
            
            # display live data

            livedata = [col[0] for col in self.data]
            self.ui.historyChart.plot(livedata, pen='g')

            if len(self.data) > self.lookback:
                Yp = self.singlepredict(self.model, livedata, self.lookback, self.modeltype)

                # blue - prediction curve
                tlen = len(Yp[:, 0])

                Xt = np.array(range(tlen)) + self.lookback + 1
                self.ui.historyChart.plot(Xt, Yp[:, 0], pen='b')

                
                
                # apply savgol filter
                if len(Yp) > 15:
                    Yf = savgol_filter(Yp, window_length=15, polyorder=5, axis=0)
            
                    # graph visualization and create new indicator
                    threshold = 0.5 * 1e-4
                    direction = [TREND_UP]      # temporary
                    arraylen = len(Yf)

                    for i in range(1, arraylen):
                        diff = Yf[i] - Yf[i-1]
                        
                        if diff > threshold:
                            direction.append(TREND_UP)
                        elif diff < -threshold:
                            direction.append(TREND_DOWN)
                        else:
                            last = len(direction) - 1
                            previous = direction[last]
                            direction.append(previous)

                    direction[0] = direction[1]
                    X = np.array(range(arraylen))
                    self.ui.historyChart.setData(X, Yf, pen=direction)
                    # feed(self.bid, self.ask, self.datestamp, direction)
                
        except ValueError:
            print(ValueError)


    def singlepredict(self, model, bid, lookback, modeltype):
        Xr = []
        length = len(bid)

        if length > lookback:
            for st in range(length - lookback):
                end = st + lookback
                Xr.append(bid[st:end])

            # convert to numpy array
            Xr = np.array(Xr)
            samples = Xr.shape[0]
            timesteps = Xr.shape[1]

            if modeltype == 'cnn' or modeltype == 'lstm':
                Xr = Xr.reshape((samples, timesteps, 1))
                # Xr = Xr.reshape((samples, 1, timesteps))

            # return prediction result
            Yp = model.predict(Xr, verbose=0)
            return Yp


    def livefeed(self):
        api = getAPI()
        symbol = "EUR_USD"
        
        #attempt to solve connection issue.
        try:
            while True:
                time.sleep(1)
                
                status, bid, ask, self.latest = getLatestPrice(api, symbol, self.latest)

                if status != "notready":
                    if status == "tradeable":
                        rowPosition = self.ui.tableFeed.rowCount()
                        if rowPosition == 0:
                            self.ui.tableFeed.insertRow(rowPosition)

                        latest = parser.parse(self.latest)
                        self.ui.tableFeed.setItem(0, 0, QtWidgets.QTableWidgetItem(symbol))

                        ####  ==> information about Bid, Ask, Spread, Time <==  #####
                        self.ui.tableFeed.setItem(0, 2, QtWidgets.QTableWidgetItem("%f" % (bid)))
                        self.ui.tableFeed.setItem(0, 3, QtWidgets.QTableWidgetItem("%f" % (ask)))
                        self.ui.tableFeed.setItem(0, 4, QtWidgets.QTableWidgetItem("%.5f" % (ask - bid)))
                        self.ui.tableFeed.setItem(0, 1, QtWidgets.QTableWidgetItem("%04d/%02d/%02d %02d:%02d:%02d" % (latest.year, latest.month, latest.day, latest.hour, latest.minute, latest.second)))
                        ####  ==> information about Bid, Ask, Spread, Time <==  #####
                        
                        #check exports
                        print(bid, ask, (ask-bid))

                        self.tick.append("%02d:%02d:%02d" % (latest.hour, latest.minute, latest.second))
                        self.bid, self.ask = bid, ask
                        self.datestamp = "%04d/%02d/%02d %02d:%02d:%02d" % (latest.year, latest.month, latest.day, latest.hour, latest.minute, latest.second)
                        
                    self.statusBar().showMessage("Market Status | {}".format(status))
                    # self.ui.tableFeed.setFocus()
                    # self.ui.tableFeed.clearFocus()
        except ValueError:
                    print("Possible connection issue from Caio", ValueError)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = ForexFeed()
    window.show()
    window.start()

    sys.exit(app.exec_())