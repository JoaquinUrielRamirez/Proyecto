from scipy.optimize import minimize
from revenue import revenues


def optimizar(a,b):
    p0 = 51

    restricciones = [
        {'type': 'ineq', 'fun': lambda x: x[0] - p0},  # a ≥ p
        {'type': 'ineq', 'fun': lambda x: p0 - x[1]}  # b ≤ p
    ]
    bounds = [(p0, None), (0, p0)]  # a ≥ p, 0 ≤ b ≤ p

    resultado = minimize(revenues, x0=[a, b], bounds=bounds, method="SLSQP")

    return resultado
