import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn')

# parameters
epsilon_0 = 8.8542e-12   # vacuum permittivity
V_0 = 0.0                # voltage at boundary (volt)
L = 1.0                  # side length (meter)
# accuracy parameters
delta = 1.0             # initiation value
target = 1.e-6

# numbers of squares per side
N = 100
# spacing of grid points
a = L/N


# charge density
def rho(x, y):
    if 0.20 <= x and x <= 0.40:
        if 0.20 <= y and y <= 0.40:
            return -1
    elif 0.60 <= x and x <= 0.80:
        if 0.60 <= y and y <= 0.80:
            return 1
    return 0


# solution
phi = np.zeros([N + 1, N + 1], float)
tmp = np.zeros([N + 1, N + 1], float)

# boundary values
phi[0, :], phi[-1, :], phi[:, 0], phi[:, - 1] = V_0, V_0, V_0, V_0
tmp[0, :], tmp[-1, :], tmp[:, 0], tmp[:, - 1] = V_0, V_0, V_0, V_0

while delta > target:
    for i in range(1, N):
        for j in range(1, N):
            x, y = a * i, a * j
            tmp[i, j] = (1/4) * (phi[i + 1, j] + phi[i - 1, j] +
                                 phi[i, j + 1] + phi[i, j - 1] + a**2 * rho(x, y)/epsilon_0)
    phi, tmp = tmp, phi
    delta = np.amax(np.abs(tmp - phi))


plt.imshow(phi)
plt.gray()
plt.savefig("h8p1.pdf")
