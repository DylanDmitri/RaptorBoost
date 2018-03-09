import sympy as sp



def list_thetas(model):
    thetas = set()

    def search(head):
        if isinstance(head, sp.Symbol):
            if head.name.startswith('t'):
                thetas.add(head)
        else:
            for child in head.args:
                search(child)

    search(model)
    return tuple(thetas)


def DataLoader(data):
    pass


"""
def gradients(model, data):

    cost_gradient = []
    for each theta:
        partial = model * model.derivative_with_respect_to( theta )
        grad = (
            partial.evaluate_at(x1=x1, x2=x2, ... y=y)
            for x1,x2,...y in data
        ).summation().simplify()

        cost_gradient.append(grad)

    return cost_gradient
"""

def gradient(model, data):
    """
    :param model: sympy equation
    :param data: pandas df, row names match sp variables
    :return:
    """

    thetas = list_thetas(model)

    cost_gradient = []

    for t in thetas:
        partial = model * sp.diff(model, t)
        grad_t = sp.Number(0)
        for row in data:
            grad_t += partial.subs(tuple(row.items()))

        cost_gradient.append(sp.simplify(grad_t))

    return cost_gradient




"""
def descend(model, gradient):

    thetas = [[ random init values ]]

    repeat until okay
        thetas -= gradient(thetas)

    return thetas

"""

"""
def solve(model, data):

    model = model - Variable('y')    # ts xs y

    grad = gradients(model, data)    # ts

    try 50 times, keeping model with lowest error as best_model
        thetas = descend(model, grad)

        test_model = model.evaluate_at(ts=thetas)

        error = sum( test_model.evaluate_at(xs,y)**2 for xs,y in data )

    return best_model

"""

