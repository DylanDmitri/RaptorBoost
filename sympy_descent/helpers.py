import numpy as np
from sympy import Symbol, Number, diff, simplify

THETA_PREFIX = 't'
def Theta(i:int):
    return Symbol(THETA_PREFIX + str(i))

@np.vectorize
def apply(f,x):
    return f(x)
