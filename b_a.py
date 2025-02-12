import numpy as np

def bid_ask(n, p0):
    bid = np.linspace(p0-p0*0.01, p0-p0*0.3, n)
    ask = np.linspace(p0+p0*0.3, p0+p0*0.01, n)
    return bid, ask