import numpy as np

def p_inf_s(s):
    return np.maximum(0, np.minimum(0.5, 0.5 - 0.08 * s))
