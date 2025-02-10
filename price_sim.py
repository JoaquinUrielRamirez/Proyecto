import numpy as np
import scipy.special as sp

def price_simulation(lambda_, k, n):
    prices = np.random.weibull(k, n) * (lambda_ / sp.gamma(1 + 1 / k))  # Gamma se utiliza para ajustar los valores que arroja Weibull
    return prices
