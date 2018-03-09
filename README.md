# RaptorBoost

Like XGBoost, except using equation trees, rather than decision trees.

An equation tree is just an abstract mathematical expression, represented with prefix notation. This python implementation uses sympy.

## Basis -- Done
Core functionality - gradient descent on abstract mathematical expressions

ie take a function ```y = theta_1 x + theta_2```
compute the inner product space function (gradient of cost function)
descend to okay values for all thetas

from this basis, we can build more sophisticated solvers

## BogoBoost -- In Process
Build a bunch of equation trees, composed of functions (Sum, Product, etc.) and Variables (either thetas or input features).
For each tree
  descend to find values of the weights
  evaluate error
  evaluate tree complexity
  
choose a tree with a good mix of accuracy and simplicity


## Raptor Boost -- Todo

Recursively Added Parent Trees On Residuals
What xgBoost does.


## Useful submodules -- Todo

If subtrees keep showing up in good equations, save those subtrees and mix them in later.

For example, a (width * length * height) term probably is significant as an additional feature.

This lets the process do feature engineering.

Additionally, run this on many example prob sets, so it can build a library of generally useful functions (eg multiply by negative one then add, for substraction). It can learn good ratios of these general functions for general problems, and thus have a strong basis for starting your specific problem

This submodules can be used alongside any boosting method.





