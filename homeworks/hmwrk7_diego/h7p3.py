import numpy as np
from scipy.integrate import ode
import matplotlib.pyplot as plt
plt.style.use('seaborn')


def orbit(t, X, G, M):
    x, vx, y, vy = X
    return [vx,
            - G * M * x / np.sqrt(x**2 + y**2)**3,
            vy,
            - G * M * y / np.sqrt(x**2 + y**2)**3]


G = 6.674e-1            # meters^3 per kilogram second^2
M = 1.989e+8            # e22 kilogram
X0 = [4e4, 0, 0, 5]     # e8 meter, e2 meter per second
t0 = 0                  # e6 second
t1 = 1550

backend = 'dopri5'
# backend = 'dop853'
solver = ode(orbit).set_integrator(backend, nsteps=10000)

sol = []


def solout(t, X):
    sol.append([t, *X])  # the star allows more than one argument


solver.set_solout(solout)
solver.set_initial_value(X0, t0).set_f_params(G, M)
solver.integrate(t1)

sol = np.array(sol)

plt.plot(sol[:, 1], sol[:, 3], '.-')

# aesthetics
plt.xlabel('$x$ ($10^8$ m)')
plt.ylabel('$y$ ($10^8$ m)')
plt.title('Comet orbit')

plt.savefig("h7p3.pdf")
