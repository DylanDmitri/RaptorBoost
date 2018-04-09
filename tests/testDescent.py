import unittest
from sympy_descent.model import Model

import sympy
import pandas as pd

x1 = sympy.Symbol('x1')
x2 = sympy.Symbol('x2')
y = sympy.Symbol('y')
t1 = sympy.Symbol('t1')
t2 = sympy.Symbol('t2')
t3 = sympy.Symbol('t3')


tnum = 0
def disp(m):
    global tnum
    tnum += 1
    print()
    print(f'test{tnum}')
    print(m.weighted_model + y)
    print('error:', m.error())


class TestGradientDescent(unittest.TestCase):

    def test_simplest(self):

        solver = Model(
            t1 * x1,
            pd.DataFrame({'x1':(1,2,3), 'y':(1.0,1.9,3.1)}),
            target = 'y')

        solver.descend('rand')

        disp(solver)

    def test_double_thetas(self):

        solver = Model(
            t1*x1**2 + t2,
            pd.DataFrame({'x1':(0,1,2), 'y':(1,2,5)}),
            target = 'y'
        )

        solver.descend([0.0, 0.0], alpha=.05, momentum=.5, threshold=.001)
        disp(solver)

    def test_double_xs(self):

        solver = Model(
            t1*x1 + t2*x2 + t3,
            pd.DataFrame({'x1':(0, 3, 6), 'x2':(0, 1, 2), 'y':(.1, .4, .8)}),
            target = 'y'
        )
        solver.descend([0.0, 0.0, 0.0])
        disp(solver)



if __name__ == '__main__':
    unittest.main()
