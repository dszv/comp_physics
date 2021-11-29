from matplotlib.animation import FuncAnimation
import dcst
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


# simulation parameters

tf = 60             # (seconds)
T = a*np.arange(N)


# initial condition

def wave_packet(x):
    return np.exp(-((x - x_0)**2)/(2*(sigma**2)))*np.exp(1j*kappa*x)


psi0_real, psi0_imag = np.zeros(N), np.zeros(N)

for i in range(1, N - 1):
    psi0_real[i], psi0_imag[i] = np.real(
        wave_packet(i * a)), np.imag(wave_packet(i * a))


# spectral method

alpha, eta = dcst.dst(psi0_real), dcst.dst(psi0_imag)


def coeff(t):
    c = np.zeros(N)
    for k in range(1, N - 1):
        tmp = (np.pi**2 * hbar * k**2)/(2 * M * L**2)
        c[k] = alpha[k] * np.cos(tmp * t) - eta[k] * np.sin(tmp * t)
    return c


fig = plt.figure()
axis = plt.axes(xlim=(0, L), ylim=(-1.1, 1.1))
line, = axis.plot([], [], 'k-')


def init():
    line.set_data([], [])
    return line,


def animate(i):
    t = i * h
    psi_real = dcst.idst(coeff(t))

    plt.title("$t = ${0:.2f} 1/eV".format(i*h))

    line.set_data(T, np.real(psi_real))
    return line,


anim = FuncAnimation(fig, animate, init_func=init, frames=100*tf, blit=True)
anim.save('spectral_inverted_wave_function.mp4', writer='ffmpeg', fps=100)
