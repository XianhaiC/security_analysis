import numpy as np
import pandas as pd
import scipy.integrate as integrate

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

# formula:
# future_value = pv(1 / ln(r) * (r^t - r) + 1)
# calculates the continuously compounded value of regular investements of pv
# for t periods at rate of r
def compound_invested_earnings(pv, r, t):
    def f(t, pv, r):
        return pv(r)**t
    I = integrate.quad(f, 0, t, args=(pv, r))

    # include the pv since we count the last invested amount as well
    return I[0] + pv

def intrinsic_val(pv, r, dr, t):
    # calculated actual growth, factoring in future discount
    ar = r - dr

    # since we are finding the discounted cash flows/earnings of each
    # of the next t years, this is equivalent to finding the compounded
    # regularly invested earnings
    val = compound_invested_earnings(pv, ar, t)

    return val
