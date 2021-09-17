import numpy as np
from scipy.optimize import root_scalar 

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()
sns.set_style("darkgrid")


# parameters
G = 6.674e-1
M = 5.974e+2
m = 7.348       # kg -> e22 kg
R = 3.844       # m  -> e8 m
w = 2.662       # s  -> e6 s

def f(r):
    return G * M * (R - r)**2 - G * m * r**2 - w**2 * r**3 * (R - r)**2


def main():
    x = np.arange(2, R, 1.e-3)
    y = f(x)

    # plot
    plt.plot(x, y, color='red')

    # Aesthetics
    plt.title('Lagrange point')
    plt.xlabel('$r$')
    plt.ylabel('$f(r)$')
    # plt.gca().set_aspect('equal', adjustable='box')

    plt.savefig("h5p3.pdf")

    # initial guess in e+8 m; must be less than R
    r0, r1 = 2, R

    # secant method
    sol = root_scalar(f, method='secant', x0=r0, x1=r1, xtol=1.e-5)

    print("r = {0:.4f}e+8 m\nf(r) = {1}".format(sol.root, f(sol.root)))

main()
