import v20
import time
import keyboard
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime

def getAPI():
    api = v20.Context(
        'api-fxpractice.oanda.com',
        '443',
        token='29e490836146e881bda3c75693af0f1e-5bff35c47be9dae08c76277e2f008686')
    return api


def order(symbol, units):
    api = getAPI()
    response = api.order.market(
        '101-001-9621481-001',
        instrument=symbol,
        units=units)

    print("Response: {} ({})".format(response.status, response.reason))


def getLatestPrice(api, symbol, latest=None):
    # latest = datetime.utcnow().isoformat('T') + 'Z'
    response = api.pricing.get(
        '101-001-9621481-001',
        instruments=symbol,
        since=latest,
        includeUnitsAvailable=False)

    # variable initialization
    status, bid, ask = "notready", 0, 0
    for price in response.get("prices", 200):
        if latest is None or price.time > latest:
            status = price.status
            latest = price.time
            bid = price.bids[0].price
            ask = price.asks[0].price
    
    return status, bid, ask, latest


def livefeed():
    latest = None
    api = getAPI()
    symbol = "EUR_USD"

    while True:
        time.sleep(1)
        status, bid, ask, latest = getLatestPrice(api, symbol, latest)
        if status == "tradeable":
            print("Market {}, Symbol:{}, Bid:{}, Ask:{}, Latest time:{}".format(status, symbol, bid, ask, latest))

        # if key 'q' is pressed 
        if keyboard.is_pressed('q'):
            break


if __name__ == "__main__":
    # order("EUR_USD", 5000)
    print("Live feed mode - press 'q' to quit")
    livefeed()
