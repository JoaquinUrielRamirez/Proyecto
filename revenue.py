import numpy as np
from scipy.integrate import quad

def weibull(s_range, lambda_, k):
    return (k / lambda_) * (s_range / lambda_)**(k - 1) * np.exp(-(s_range / lambda_)**k)

def weibull_pdf(p, k, lambda_):
    """Función de densidad de probabilidad de Weibull."""
    return (k / lambda_) * (p / lambda_)**(k - 1) * np.exp(-(p / lambda_)**k)

def revenues(params):
    a,b = params
    p = 51
    k = 10
    lambda_ = 50
    lb = max(0, 0.5 - 0.8 * (a - p))
    ls = max(0, 0.5 - 0.8 * (p - b))
    i = 0.4

    # Integrales de pérdidas esperadas
    integral1, _ = quad(lambda P: (P - a) * weibull_pdf(P, k, lambda_), a, np.inf)
    integral2, _ = quad(lambda P: (b - P) * weibull_pdf(P, k, lambda_), 0, b)

    # Ecuación de ingresos esperados
    revenue = (a - p) * lb + (p - b) * ls - (integral1 + integral2) * i
    return -revenue



