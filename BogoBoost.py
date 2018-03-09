from numpy.random import choice
import sympy as sp

# we want a bag o parts

bag = (
    lambda: sp.Add,
    lambda: sp.Mul,
    lambda: sp.Min,
    lambda: sp.Max,

    lambda: sp.Pow,
    lambda: sp.log,

    # invert and negate??
)

class Node:
    func = NotImplemented
    slot_limit = None
    slots = []

class Sum(Node):
    func = sp.Add

class Product(Node):
    func = sp.Mul

class Minimum(Node):
    func = sp.Min

class Maximum(Node):
    func = sp.Max

class Power(Node):
    func = sp.Pow
    slot_limit = 2

class Logarithm(Node):
    func = sp.ln
    slot_limit = 2


def RandomTree
