from random import random
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dracula')


# interaction constant
J = 1
# magnetic field
h = 1
# temperature
# T = 1
# dimension of the grid of spins: NxN
N = 20
# steps
steps = int(1.e6)


def energy(S):
    E = 0
    for i in range(N - 1):
        E += -J * np.dot(S[i][:], S[i + 1][:])
        E += -J * np.dot(S[:][i], S[:][i + 1])
    # E -= h * S.sum()
    return E


def magnetization(S):
    return S.sum()


for T in range(1, 4):
    # initial state
    S = np.random.choice([-1, 1], (N, N))

    # main loop
    E_plot = []
    M_plot = []
    E_0 = energy(S)
    M_0 = magnetization(S)

    for _ in range(steps):

        # choose a spin and flip it, then calculate the energy
        i, j = np.random.randint(N), np.random.randint(N)
        S[i][j] = -1 * S[i][j]
        E = energy(S)
        dE = E - E_0

        # decide whether to accept the move
        if dE > 0 and random() > np.exp(-dE/T):
            S[i][j] = -1 * S[i][j]
        else:
            E_0 = E
            M_0 = magnetization(S)

        E_plot.append(E_0)
        M_plot.append(M_0)

    # plt.plot(E_plot, label='T = {0}'.format(T))
    plt.plot(M_plot, label='T = {0}'.format(T))

plt.xlabel('Steps')
plt.ylabel('Magnetization')
plt.title('2D Ising model')
plt.legend()

plt.savefig('ising_magnetization.pdf')
