import csv
import time
import pandas as pd

from os import makedirs
from os.path import join, exists
from dateutil import parser
from datetime import timedelta
from sklearn.preprocessing import MinMaxScaler

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

'''
CSV data format for TrueFX dataset
Example:
    EUR/USD     20180902 21:03:35.201	1.15927     1.16058
    -------     ---------------------   -------     -------
    <Pair>      <Date/time>             <Bid>       <Ask>
'''

def load(filename):
    print("[LOAD] Loading dataset from %s" % filename)
    start = time.time()
    df = pd.read_csv(filename, header=None)
    end = time.time()
    print("[LOAD] Done. Elapsed time is %.2f seconds" % (end - start))
    return df.values


def extractM(dmin, datestr, bid, ask):
    print("[EXTRACT] Building target dataset ...")

    start = time.time()     # time tracker enable
    length = len(datestr)   # get length of total elements
    findex = 0              # can be changed according to the condition

    # return bid and ask values
    newdate = []
    newbid = []
    newask = []
    newdate.append(datestr[findex])
    newbid.append(bid[findex])
    newask.append(ask[findex])

    # previous date/time
    prev = parser.parse(datestr[findex])
    for i in range(findex, length):
        # calculate the difference if the interval is 5mins
        current = parser.parse(datestr[i])
        delta = current - prev
        mindiff = delta / timedelta(minutes=1)

        # if the difference reaches at our time interval
        if (mindiff >= dmin):
            newdate.append(datestr[i])
            newbid.append(bid[i])
            newask.append(ask[i])
            prev = current      # update base date/time

    # report elapsed interval
    end = time.time()
    print("[EXTRACT] Done. Elapsed time is %.2f seconds" % (end - start))

    # return value
    return newdate, newbid, newask


def analyze(filename, m):
    # check extracted file
    datapath = "../extract"
    if not exists(datapath):
        makedirs(datapath)
    
    # get trading info every x minutes (Mx)
    fullpath = join(datapath, filename)

    # if extracted data file does not exist, create new file
    if not exists(fullpath):
        srcpath = "../data"
        values = load(join(srcpath, filename))

        # input data
        pair = values[:, 0]
        srcdate = values[:, 1]
        srcbid = values[:, 2]
        srcask = values[:, 3]

        # extract and save to the csv file
        datestr, bid, ask = extractM(m, srcdate, srcbid, srcask)
        
        with open(fullpath, mode='w', newline='') as csvfile:
            pairtype = pair[0]
            writer = csv.writer(csvfile, delimiter=',')

            for i in range(len(datestr)):
                writer.writerow([pairtype, datestr[i], bid[i], ask[i]])

    # otherwise, read the data from the existing file
    else:
        values = load(fullpath)

        # input data
        pair = values[:, 0]
        datestr = values[:, 1]
        bid = values[:, 2]
        ask = values[:, 3]

    # return
    return datestr, bid, ask
