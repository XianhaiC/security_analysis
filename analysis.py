import numpy as np
import pandas as pd

def calculate_iv(latest_fcf, growth_rate_fcf, t, r,):
    pass

# formula:
# rate = (future_value / principal_value) ^ (1 / time) - 1
def avg_growth_rate(pv, fv, t):
    return (fv / pv) ** (1 / t) - 1
    pass

# formula:
# principal_value = future_value / (1 + rate) ^ time
def discount_future(fv, t, r):
    return fv / (1 + r) ** t
