from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn')


t0 = 0
tf = 10
h = 0.01
V0 = [0]
RC = [0.01, 0.1, 1]


# PART A

def V_in(t):
    if int(2*t) % 2 == 0:
        return 1
    else:
        return -1


def main():
    for rc in RC:
        def f(t, V):  # V = V_out
            return (V_in(t) - V)/rc

        V_out = solve_ivp(f, [t0, tf], V0, method='RK45',
                          t_eval=np.arange(t0, tf + h, h))

        plt.plot(np.array(V_out.t).flatten(), np.array(
            V_out.y).flatten(), label='$RC = {0}$'.format(rc))

    # aesthetics
    plt.xlabel('$t$')
    plt.ylabel('$V_{out}$')
    plt.legend()
    plt.savefig("h6p4.pdf")


main()
