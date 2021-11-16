from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn')


l = 0.40
m = 1.0
g = 9.81
X0 = [np.pi/2, 0, np.pi/2, 0]
t0 = 0
tf = 10
h = 0.001


def f(t, X):
    theta1, omega1, theta2, omega2 = X
    return [omega1,
            -(omega1**2 * np.sin(2*theta1 - 2*theta2) + 2 * omega2**2 * np.sin(theta1 - theta2) + (g/l)
              * (np.sin(theta1 - 2*theta2) + 3 * np.sin(theta1)))/(3 - np.cos(2*theta1 - 2*theta2)),
            omega2,
            (4 * omega1**2 * np.sin(theta1 - theta2) + omega2**2 * np.sin(2*theta1 - 2*theta2) + 2 * (g/l) * (np.sin(2*theta1 - theta2) - np.sin(theta2)))/(3 - np.cos(2*theta1 - 2*theta2))]


def main():
    X = solve_ivp(f, [t0, tf], X0, method='RK45',
                  t_eval=np.arange(t0, tf + h, h))

    # PART B

    t1 = np.array(X.y[0]).flatten()
    o1 = np.array(X.y[1]).flatten()
    t2 = np.array(X.y[2]).flatten()
    o2 = np.array(X.y[3]).flatten()

    V = - m*g*l*(2*np.cos(t1) + np.cos(t2))
    T = m*(l**2)*(o1**2 + 0.5*o2**2 + o1*o2*np.cos(t1 - t2))
    E = T + V

    plt.plot(np.array(X.t).flatten(), E)

    # aesthetics
    plt.xlabel('$t$ (s)')
    plt.ylabel('$E$ (J)')
    plt.title('Energy conservation')
    plt.savefig("h7p2b.pdf")

    # PART C AND D

    x1 = l*np.sin(np.array(X.y[0]).flatten())
    y1 = -l*np.cos(np.array(X.y[0]).flatten())
    x2 = x1 + l*np.sin(np.array(X.y[2]).flatten())
    y2 = y1 - l*np.cos(np.array(X.y[2]).flatten())

    fig = plt.figure()
    axis = plt.axes(xlim=(-2*l, 2*l), ylim=(-2.5*l, l/2))
    line1, = axis.plot([], [], 'k-')
    line2, = axis.plot([], [], 'ko')
    line3, = axis.plot([], [], 'ko')

    def init():
        line1.set_data([], [])
        return line1,

    def animate(i):
        j = int(np.around(1/(h * 50))) * i
        plt.title("$t = ${0:.1f} s".format(i/50))

        line1.set_data([0, x1[j], x2[j]], [0, y1[j], y2[j]])
        line2.set_data(x1[j], y1[j])
        line3.set_data(x2[j], y2[j])
        return line1,

    anim = FuncAnimation(fig, animate, init_func=init, frames=50*tf, blit=True)
    anim.save('double_pendulum.mp4', writer='ffmpeg', fps=50)


main()
