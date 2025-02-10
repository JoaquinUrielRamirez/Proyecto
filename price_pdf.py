import scipy.stats as stats

def price_pdf_(p, k, lanbda_):
    return stats.weibull_min.pdf(p, c=k, scale=lanbda_)