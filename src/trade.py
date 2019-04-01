import csv
import pandas as pd
from os.path import exists
from datetime import datetime
from util import createdir

# define default values

STANDARD_LOT = 100000
DEFAULT_BALANCE = 100000
DEFAULT_PERCENTAGE = 5
DEFAULT_COMMISSION = 1.4
DEFAULT_LOOKBACK = 10
DEFAULT_CUTOFF = 0.7
DEFAULT_SYMBOL = "EURUSD"

TYPE_INIT = "INIT"
TYPE_LONG = "LONG"
TYPE_SHORT = "SHORT"


def writeLog(beginPrice, endPrice, beginTime, endTime, tradeType, symbol=DEFAULT_SYMBOL, firstBalance=DEFAULT_BALANCE, percentage=DEFAULT_PERCENTAGE, commission=DEFAULT_COMMISSION):
    fieldnames = [
        "Balance",
        "Begin Time",
        "End Time",
        "Trade Type",
        "Perc Bal",
        "Symbol",
        "Begin Price",
        "End Price",
        "Commission",
        "Profit",
        "Lot"
    ]

    dirname = "../backtest/"
    createdir(dirname)
    # filename = dirname + datetime.now().strftime("%Y%m%d-%H%M%S") + ".csv"
    filename = dirname + "testchart.csv"
    balance = firstBalance
    lots = 1

    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        logLen = len(endPrice)
        pointer = 0
        positiveLogs = 0

        for i in range(logLen):
            # profit calculation
            # ($1.2188 – 1.2178) X 100,000 = $100
            if tradeType[i] == TYPE_LONG:
                profit = (endPrice[i] - beginPrice[i] - commission * 1e-4) * STANDARD_LOT * lots
            else:
                profit = (beginPrice[i] - endPrice[i] - commission * 1e-4) * STANDARD_LOT * lots

            # write to csv file
            writer.writerow({
                "Balance": balance,
                "Begin Time": beginTime[i],
                "End Time": endTime[i],
                "Trade Type": tradeType[i],
                "Symbol": symbol,
                "Begin Price": beginPrice[i],
                "End Price": endPrice[i],
                "Perc Bal": percentage,
                "Commission": commission,
                "Profit": profit,
                "Lot" : lots
            })

            # update next balance by profit
            # increase lots if we have confidence of trending up
            balance = balance + profit
            pointer = pointer + 1

            if profit > 0:
                positiveLogs = positiveLogs + 1
            
            if pointer >= DEFAULT_LOOKBACK and positiveLogs / DEFAULT_LOOKBACK >= DEFAULT_CUTOFF:
                lots = lots + 1
                positiveLogs = 0
                pointer = 0


def feed(bid, ask, datestamp, direction):
    tradeSignal = TYPE_INIT
    length = len(direction)

    # significant arrays definition
    beginPrice = []
    endPrice = []
    beginTime = []
    endTime = []
    tradeType = []
    
    for i in range(length):
        cur = direction[i]
        if tradeSignal == TYPE_INIT and cur == "g":
            # open initial trade as "LONG"
            openTrade(beginPrice, beginTime, tradeType, ask[i], datestamp[i], TYPE_LONG)
            tradeSignal = TYPE_LONG
            
        elif tradeSignal == TYPE_INIT and cur == "r":
            # open initial trade as "SHORT"
            openTrade(beginPrice, beginTime, tradeType, bid[i], datestamp[i], TYPE_SHORT)
            tradeSignal = TYPE_SHORT
            
        elif tradeSignal == TYPE_SHORT and cur == "g":
            # close trade and open new trade as "LONG"
            closeTrade(endPrice, endTime, ask[i], datestamp[i])
            openTrade(beginPrice, beginTime, tradeType, ask[i], datestamp[i], TYPE_LONG)
            tradeSignal = TYPE_LONG
        
        elif tradeSignal == TYPE_LONG and cur == "r":
            # close trade and open new trade as "SHORT"
            closeTrade(endPrice, endTime, bid[i], datestamp[i])
            openTrade(beginPrice, beginTime, tradeType, bid[i], datestamp[i], TYPE_SHORT)
            tradeSignal = TYPE_SHORT

    writeLog(beginPrice, endPrice, beginTime, endTime, tradeType)
        

def openTrade(beginPrice, beginTime, tradeType, mid, datestamp, trtype):
    beginPrice.append(mid)
    beginTime.append(datestamp)
    tradeType.append(trtype)


def closeTrade(endPrice, endTime, mid, datestamp):
    endPrice.append(mid)
    endTime.append(datestamp)