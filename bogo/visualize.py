# -0.10544438075674*n**3 + n + 0.0927434048707628

import pandas as pd
import numpy as np

lumpy = pd.DataFrame({
    'n': (56, 56, 65, 65, 50, 25, 87, 44, 35),
    'y': (87, 91, 85, 91, 75, 28, 122, 66, 58),
})

# match(lumpy)

lumpy -= lumpy.min()
lumpy /= lumpy.max()


import matplotlib.pyplot as plt

plt.scatter(lumpy.n, lumpy.y)

xaxis = np.arange(0,1,.001)

@np.vectorize
def f(n):
    return -.1054444380*n**3 + n + .0927434

plt.plot(xaxis, f(xaxis))

plt.show()
