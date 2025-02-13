import scipy.stats as stats
from scipy.integrate import quad
import numpy as np
from scipy.stats import weibull_min


def revenues(params):
    a,b = params
    i = 0.4
    k = 10
    lambda_ = 50
    p = 51
    x = np.linspace(0, 5, 100)

    def f(x, k, lam):
        """ Función de densidad de probabilidad de Weibull """
        return (k / lam) * (x / lam) ** (k - 1) * np.exp(-(x / lam) ** k)

    s1 = a - p
    s2 = p - b
    lb = max(0, max(0, 0.5 - 0.8 * s1))
    ls = max(0, max(0, 0.5 - 0.8 * s2))
    rev = (a-p)*lb + (p-b)*ls - (quad(lambda x:(p-a)*f(x, k, lambda_), p, np.inf) + quad(lambda x:(b-p)*f(x, k, lambda_), 0, p))* i
    return -rev

