from numpy.random import choice, random, randint
import sympy as sp

# we want a bag o parts



bag = []
class Operation:
    func = NotImplemented
    slot_limit = None

    def __init__(self):
        self.args = []

    def add(self, o):
        assert self.empty
        self.args.append(o)

    def serialize(self):
        sp_args = (
            o.serialize() if isinstance(o, Operation) else o
            for o in self.args
        )
        return self.func(*sp_args)

    @property
    def empty(self):
        return self.slot_limit is None or self.slot_limit > len(self.args)

    def __init_subclass__(cls, **kwargs):
        bag.append(cls)


def rand_op():
    return choice(bag)()


class Sum(Operation):
    func = sp.Add

class Product(Operation):
    func = sp.Mul

# class Min(Operation):
#     func = sp.Min

# class Max(Operation):
#     func = sp.Max

# class Power(Operation):
#     func = sp.Pow
#     slot_limit = 2


class RandomTree:

    def __init__(self, operations=3,
                 features=('x1',)):

        self.head = rand_op()

        for _ in range(operations):
            self.random_child(self.head).add(rand_op())

        self.current_theta = 0
        self.features = features
        self.fill(self.head)

    def random_child(self, node):
        r = randint(0, len(node.args) + node.empty)
        if r >= len(node.args):
            return node
        return self.random_child(node.args[r])

    def random_symbol(self):
        if random() < .5:
            self.current_theta += 1
            return sp.Symbol(f't{self.current_theta}')

        return sp.Symbol(choice(self.features))

    def fill(self, node):

        while len(node.args) < 2:
            node.add(self.random_symbol())

        while node.empty and random()<.4:
            node.add(sp.Symbol(choice(self.features)))

        for child in node.args:
            if isinstance(child, Operation):
                self.fill(child)

    def to_sympy(self):
        return sp.simplify(self.head.serialize())




