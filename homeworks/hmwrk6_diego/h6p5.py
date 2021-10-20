from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn')


t0 = 0
tf = 30
h = 0.01
X0 = [2, 2]
alpha = 1
beta = 0.5
gamma = 0.5
delta = 2.0


# PART A

def f(t, X):
    x, y = X  # rabbits, foxes
    return [alpha*x - beta*x*y, gamma*x*y - delta*y]


def main():

    X = solve_ivp(f, [t0, tf], X0, method='RK45',
                  t_eval=np.arange(t0, tf + h, h))

    plt.plot(np.array(X.t).flatten(), np.array(X.y[0]).flatten(), label='$x$')
    plt.plot(np.array(X.t).flatten(), np.array(X.y[1]).flatten(), label='$y$')

    # aesthetics
    plt.xlabel('$t$')
    plt.ylabel('$V_{out}$')
    plt.legend()
    plt.savefig("h6p5.pdf")


main()
