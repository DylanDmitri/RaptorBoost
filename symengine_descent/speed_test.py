import symengine
from symengine.lib.symengine_wrapper import eval_double

import sympy


from timeit import timeit


run = lambda f: f()



@run
def w_engine():
    x = symengine.var("x")

    f = x**2 + x
    f = f.subs(x, 5)

    print(eval_double(f))




