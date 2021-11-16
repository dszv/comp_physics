from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn')


# PART A

l = 1.0
g = 9.81
X0 = [np.pi/2, 0]
t0 = 0
tf = 10
h = 0.001


def f(t, X):
    theta, omega = X
    return [omega, -(g/l)*np.sin(theta)]


def main():
    X = solve_ivp(f, [t0, tf], X0, method='RK45',
                  t_eval=np.arange(t0, tf + h, h))

    x = l*np.sin(np.array(X.y[0]).flatten())
    y = -l*np.cos(np.array(X.y[0]).flatten())

    fig = plt.figure()
    axis = plt.axes(xlim=(-1.5*l, 1.5*l), ylim=(-1.5*l, l/2))
    line1, = axis.plot([], [], 'k-')
    line2, = axis.plot([], [], 'ko')

    def init():
        line1.set_data([], [])
        return line1,

    def animate(i):
        j = int(np.around(1/(h * 50))) * i
        plt.title("$t = ${0:.1f} s".format(i/50))

        line1.set_data([0, x[j]], [0, y[j]])
        line2.set_data(x[j], y[j])
        return line1,

    anim = FuncAnimation(fig, animate, init_func=init, frames=50*tf, blit=True)
    anim.save('simple_pendulum.mp4', writer='ffmpeg', fps=50)


main()
