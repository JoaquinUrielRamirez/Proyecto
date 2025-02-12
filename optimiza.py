from scipy.optimize import minimize

def optimo(f):
    p0 = 51
    b = p0 - 3
    a = p0 + 3
    restricciones = [
        {'type': 'ineq', 'fun': lambda x: b - p0},  # a - p ≥ 0  →  a ≥ p
        {'type': 'ineq', 'fun': lambda x: p0 - a}  # p - b ≥ 0  →  b ≤ p
    ]

    bounds = [(p0, None),  # a ≥ p (sin límite superior)
              (0, p0)]  # 0 ≤ b ≤ p
    op = minimize(f, (a,b), bounds=bounds,method="SLSQP")
    return op