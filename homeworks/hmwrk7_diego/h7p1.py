from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn')

# PART A

t0    = 0
tf    = 50
h     = 0.01
X0    = [0, 1, 0]
sigma = 10
r     = 28
b     = 8/3


def f(t, X):
    x, y, z = X
    return [sigma*(y - x), r*x - y - x*z, x*y - b*z]


def main():

    X = solve_ivp(f, [t0, tf], X0, method='RK45', t_eval=np.arange(t0, tf + h, h))

    # PART B

    plt.plot(np.array(X.y[2]).flatten(), np.array(X.y[0]).flatten())

    # aesthetics
    plt.xlabel('$Z$')
    plt.ylabel('$X$')
    plt.title('Lorenz equations')
    plt.savefig("h7p1.pdf")


main()
