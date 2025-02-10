def prob_liquidez(S):
    p_l = max(0, min(0.5, 0.5 - 0.8*S))
    return p_l