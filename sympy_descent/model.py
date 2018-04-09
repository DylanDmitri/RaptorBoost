from sympy_descent.helpers import *
from sympy_descent.data_loader import DataLoader


class NoThetaException(Exception):
    """No thetas found. Should start with `t`."""

class DivergentModelException(Exception):
    """Whoops"""


class Model:

    # =========================================================================
    def __init__(self, model, df, target:str):
        """
        :param model:
            a sympy equation, containing some number of thetas
            ie generated from helpers.Theta

        :param df:
            a pandas dataframe

        :param target:
            string
            must match a column of data
        """

        self.model = model
        self.data = DataLoader(df)

        if target not in self.data.df.columns:
            raise Exception(f'invalid target string "{target}": not in {self.data.columns}')
        self.model -= Symbol(target)

        # ----- find theta names ------------
        thetas = set()
        def search(head):
            if isinstance(head, Symbol):
                if head.name.startswith(THETA_PREFIX):
                    thetas.add(head)
            else:
                for child in head.args:
                    search(child)
        search(self.model)

        if len(thetas) == 0:
            raise NoThetaException

        self.thetas = sorted(tuple(thetas), key=str)

        # ----- find gradient ---------------
        """
        cost_gradient = []
        for each theta:
            partial = model * model.derivative_with_respect_to(theta)
            grad = (
                partial.evaluate_at(x1=x1, x2=x2, ... y=y)
                for x1, x2, ...y in data
            ).summation().simplify()

            cost_gradient.append(grad)

        return cost_gradient
        """

        @np.vectorize
        def cost_partial(t):
            f = self.model * diff(self.model, t)
            return simplify(np.sum(f.subs(row) for row in self.data))

        self.grad = cost_partial(self.thetas)


    # =========================================================================
    def descend(self, initial_thetas,
                alpha=.01, momentum=0.5, threshold=.01):

        if initial_thetas == 'rand':
            initial_thetas = list(np.random.rand(len(self.thetas)))

        assert len(initial_thetas) == len(self.thetas)

        self.theta_vals = initial_thetas

        deltas = np.zeros(len(self.thetas))

        for i in range(1,500):

            # if not i%50:
            #     self.save_weighted_model()
            #     print(i, '\t', *(f'{float(s):.4f}'.ljust(8) for s in (*self.theta_vals, self.error())))

            deltas = (momentum*deltas
                      + np.array([grad.subs(self.theta_dict) for grad in self.grad]))

            if sum(abs(deltas)) < threshold:
                break

            self.theta_vals -= deltas * alpha

            if any(abs(self.theta_vals) > 9999):
                raise DivergentModelException()


        self.save_weighted_model()

    # =========================================================================
    @property
    def theta_dict(self):
        return tuple(zip(self.thetas, self.theta_vals))

    def save_weighted_model(self):
        self.weighted_model = simplify(self.model.subs(self.theta_dict))

    def error(self):
        return np.sum(self.weighted_model.subs(row)**2 for row in self.data)


    '''
    def solve(model, data):

    model = model - Variable('y')    # ts xs y

    grad = gradients(model, data)    # ts

    try 50 times, keeping model with lowest error as best_model
        thetas = descend(model, grad)

        test_model = model.evaluate_at(ts=thetas)

        error = sum( test_model.evaluate_at(xs,y)**2 for xs,y in data )

    return best_model
    '''

