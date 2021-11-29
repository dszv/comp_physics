from scipy.sparse import diags
from scipy.sparse import linalg
from matplotlib.animation import FuncAnimation
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn')


# parameters

# natural units
hbar = 1
m = 1.7827e-36
l = 1.9733e-7
s = 6.5823e-16

M = 9.109e-31/m     # (eV)
L = 1.e-8/l         # (eV^-1)

x_0 = L/2
sigma = 1e-10/l     # (eV^-1)
kappa = 5e10*l      # (eV)

N = 1000
a = L/N
h = 1e-18/s         # (eV^-1)


# crank-nicholson method parameters

a1 = 1 + h*hbar*1j/(2*M*a**2)
a2 = -h*hbar*1j/(4*M*a**2)

b1 = 1 - h*hbar*1j/(2*M*a**2)
b2 = h*hbar*1j/(4*M*a**2)


# simulation parameters

tf = 60            # (seconds)
T = a*np.arange(N)


# initial condition

def wave_packet(x):
    return np.exp(-((x - x_0)**2)/(2*(sigma**2)))*np.exp(1j*kappa*x)


psi = np.zeros(N, complex)
for i in range(1, N - 1):
    psi[i] = wave_packet(i*L/N)


# crank-nicholson method

D1 = a1*np.ones(N, complex)
D2 = a2*np.ones(N - 1, complex)
A = diags([D1, D2, D2], [0, -1, 1])

v = np.zeros(N, complex)
for i in range(1, N - 1):
    v[i] = b1*psi[i] + b2*(psi[i + 1] + psi[i - 1])

fig = plt.figure()
axis = plt.axes(xlim=(0, L), ylim=(-1.1, 1.1))
line, = axis.plot([], [], 'k-')


def init():
    line.set_data([], [])
    return line,


def animate(i):
    psi = linalg.lsqr(A, v)[0]

    for j in range(1, N - 1):
        v[j] = b1*psi[j] + b2*(psi[j + 1] + psi[j - 1])

    plt.title("$t = ${0:.2f} 1/eV".format(i*h))

    line.set_data(T, np.real(psi))
    return line,


anim = FuncAnimation(fig, animate, init_func=init, frames=100*tf, blit=True)
anim.save('wave_function.mp4', writer='ffmpeg', fps=100)
