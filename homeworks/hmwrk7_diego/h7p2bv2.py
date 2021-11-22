import numpy as np
from scipy.integrate import ode
import matplotlib.pyplot as plt
plt.style.use('seaborn')


def pendulum(t, X, l, g):
    theta1, omega1, theta2, omega2 = X
    return [omega1,
            -(omega1**2 * np.sin(2*theta1 - 2*theta2) + 2 * omega2**2 * np.sin(theta1 - theta2) + (g/l)
              * (np.sin(theta1 - 2*theta2) + 3 * np.sin(theta1)))/(3 - np.cos(2*theta1 - 2*theta2)),
            omega2,
            (4 * omega1**2 * np.sin(theta1 - theta2) + omega2**2 * np.sin(2*theta1 - 2*theta2) + 2 * (g/l) * (np.sin(2*theta1 - theta2) - np.sin(theta2)))/(3 - np.cos(2*theta1 - 2*theta2))]


l = 0.40
m = 1.0
g = 9.81
X0 = [np.pi/2, 0, np.pi/2, 0]
t0 = 0
t1 = 100

# backend = 'dopri5'
backend = 'dop853'
solver = ode(pendulum).set_integrator(backend, nsteps=10000)

sol = []


def solout(t, X):
    sol.append([t, *X])


solver.set_solout(solout)
solver.set_initial_value(X0, t0).set_f_params(l, g)
solver.integrate(t1)

sol = np.array(sol)

# plt.plot(sol[:, 0], sol[:, 1], 'b.-')
# plt.savefig("h7p2.pdf")

t1 = sol[:, 1]
o1 = sol[:, 2]
t2 = sol[:, 3]
o2 = sol[:, 4]

V = - m*g*l*(2*np.cos(t1) + np.cos(t2))
T = m*(l**2)*(o1**2 + 0.5*o2**2 + o1*o2*np.cos(t1 - t2))
E = T + V

plt.plot(sol[:, 0], E)

# aesthetics
plt.xlabel('$t$ (s)')
plt.ylabel('$E$ (J)')
plt.title('Energy conservation')
plt.savefig("h7p2b.pdf")
