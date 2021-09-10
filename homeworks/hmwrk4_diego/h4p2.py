# Loading packages
import seaborn as sns
sns.set_theme()
sns.set_style("darkgrid")

import numpy as np
from scipy.misc import derivative    # scipy implementation


# variables
a, b = 0, 2
N = 20 
h = (b - a)/N
x = np.arange(a, b + h, h)

# function
def f(x):
    return x**4 - 2*x + 1

# def Df(x, h):
#     return (f(x + h/2) - f(x - h/2))/h


def main():
    s = sum([f(k) for k in x[1 : -1]]) 
    trap = h * (0.5 * f(a) + 0.5 * f(b) + s)

    # cdiff = (h**2 /12) * (Df(a, 1.e-5) - Df(b, 1.e-5))
    cdiff = (h**2 /12) * (derivative(f, a, dx=1.e-5/2) - derivative(f, b, dx=1.e-5/2))

    I = trap + cdiff
    print('''Integral: {0}'''.format(I))

main()
