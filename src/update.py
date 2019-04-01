from datetime import datetime
from threading import Timer
from livefeed import livefeed


def tick():
    livefeed(symbols="EUR/USD")
    Timer(0.1, tick).start()


if __name__ == "__main__":
    tick()