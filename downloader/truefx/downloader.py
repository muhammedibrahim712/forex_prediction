import os

def main():
    pairs = [
        "AUDJPY", "AUDNZD", "AUDUSD",
        "CADJPY",
        "CHFJPY",
        "EURCHF", "EURGBP", "EURJPY", "EURUSD",
        "GBPJPY", "GBPUSD",
        "NZDUSD",
        "USDCAD", "USDCHF", "USDJPY"
    ]

    for pair in pairs:
        cmd = "truefx2018.bat " + pair + " 2017 4 2017 12"
        os.system(cmd)


def check(pair):
    # cmd = "truefx2018.bat " + pair + " 2018 1 2018 9"
    cmd = "truefx.bat " + pair + " 2012 1 2012 2"
    os.system(cmd)


if __name__ == "__main__":
    # main()
    check("EURUSD")
