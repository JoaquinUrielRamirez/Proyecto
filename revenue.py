import scipy.stats as stats
from scipy.integrate import quad as int
import numpy as np

def revenues(params):
    a,b = params
    i = 0.4
    k = 10
    lambda_ = 50
    p = 51
    f = lambda x: stats.weibull_min.pdf(x, c=k, scale=lambda_)
    s1 = a - p
    s2 = p - b
    lb = max(0, max(0, 0.5 - 0.8 * s1))
    ls = max(0, max(0, 0.5 - 0.8 * s2))
    # Realizar las integrales
    integral1, _ = int(lambda x: f(x)*(x-p), a, np.inf)
    integral2, _ = int(lambda x: f(x)*(p-x), 0, b)

    rev = ((a - p) * lb + (p - b) * ls) * (1 - i) - (integral1 + integral2) * i
    return -rev

