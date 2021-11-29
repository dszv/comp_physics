import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn')


# parameters
A = 10.0      # constant (Celsius)
B = 12.0      # constant (Celsius)
tau = 365     # period (day)
D = 0.1       # thermal diffusivity (meter^2 per day)
L = 20        # total depth (meter)
tf = 10*365   # time of simulation (day)

# numbers of divisions in the grid
N = 100
# grid spacing
a = L/N
# time step
h = 0.1

# time for plotting
t1 = 9*365 + 3*1
t2 = 9*365 + 3*2
t3 = 9*365 + 3*3
t4 = 9*365 + 3*4
tt = [t1, t2, t3, t4]


# temperature at surface in Celsius
def T_surface(t, A, B, tau):
    return A + B * np.sin(2*np.pi*t/tau)


# temperature at the middle in Celsius
T_middle = 10.0
# temperature at deepest point in Celsius
T_deepest = 11.0


# solution, boundary and initial condition
T = np.empty(N + 1)
T[1: N] = T_middle
T[N] = T_deepest
tmp = np.empty(N + 1)
tmp[N] = T_deepest


# FTCS method
c = (h*D/(a**2))
for t in np.arange(0, tf + h, h):
    T[0] = T_surface(t, A, B, tau)
    tmp[0] = T_surface(t, A, B, tau)
    for i in range(1, N):
        tmp[i] = T[i] + c * (T[i + 1] + T[i - 1] - 2*T[i])
    T, tmp = tmp, T
    if t in tt:
        plt.plot(T, label='$t = {0}$ trimester'.format(tt.index(t) + 1))


plt.xlabel('depth (${0}$ m)'.format(L/N))
plt.ylabel('$T$ ($^{\circ}$C)')
plt.title("Thermal diffusion in Earth's crust")
plt.legend()
plt.savefig("h8p2.pdf")
