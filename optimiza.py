from scipy.optimize import minimize
from revenue import revenues
import numpy as np


def optimizar(a,b):
    p0 = 51
    x0 = (p0*1.10,p0*0.90)

    restricciones = [
        {'type': 'ineq', 'fun': lambda x: x[0] - p0},  # a ≥ p
        {'type': 'ineq', 'fun': lambda x: p0 - x[1]}  # b ≤ p
    ]
    bounds = [(p0, p0+20), (p0-20, p0)]  # a ≥ p, 0 ≤ b ≤ p
    params= a,b

    resultado = minimize(revenues, x0=x0, bounds=bounds, constraints=restricciones)

    return resultado
