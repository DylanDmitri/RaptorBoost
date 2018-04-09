from bogo.RandomTree import RandomTree
from sympy_descent.model import Model, NoThetaException, DivergentModelException
import sympy as sp

def match(data):

    def log(*args):
        return
        print(*args)


    best_error = float('inf')
    best_func = None

    features = [c for c in data.columns if c!='y']

    for _ in range(300):
        f = RandomTree(2, features=features)

        log('\n\n----------------------')
        print(f.to_sympy())

        try:
            solver = Model(
                f.to_sympy(),
                data,
                'y'
            )
        except NoThetaException:
            log('no thetas')
            continue

        try:
            solver.descend('rand')
        except DivergentModelException:
            log('model diverged')
            continue

        log(solver.weighted_model)

        error = solver.error()
        print(error)
        print()

        if error < best_error:
            best_error = error
            best_func = solver.weighted_model


    best_func = sp.simplify(best_func + sp.Symbol('y'))

    print()
    print('best:', best_func)
    print('error:', best_error)



import pandas as pd

simple = pd.DataFrame({
     'x1':(1,2,3,4,5,6),
     'y': (3,4,5,6,7,8)
    })

lumpy = pd.DataFrame({
    'n': (56, 56, 65, 65, 50, 25, 87, 44, 35),
    'y': (87, 91, 85, 91, 75, 28, 122, 66, 58),
})

# match(lumpy)

lumpy -= lumpy.min()
lumpy /= lumpy.max()

match(lumpy)




