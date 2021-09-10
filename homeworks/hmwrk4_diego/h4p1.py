# Loading packages
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()
sns.set_style("darkgrid")

import numpy as np
from scipy.misc import derivative    # scipy implementation


a, b = -2, 2
h    = 5.e-2

def f(x):
    return 1 + 0.5 * np.tanh(x)

def Df(x):
    return 0.5 * np.cosh(x)**(-2)

def main():
    # analytical
    d = 1.e-5
    x = np.arange(a, b + d, d)
    y = Df(x)
    
    # numerical
    x_n = np.arange(a + h, b, h)
    y_n = []
    y_s = []    # scipy implementation
    
    for x_i in x_n:
        delta_f = f(x_i + h/2) - f(x_i - h/2)
        y_n.append(delta_f/h)
        y_s.append(derivative(f, x_i, dx=h/2))     # scipy implementation
        
    # Plots
    plt.plot(x, y, color='red', label='$sech^2(x)/2$')
    plt.scatter(x_n, y_n, color='black', marker='x', label='numerical') # linestyle='--'
    plt.scatter(x_n, y_s, color='green', marker='.', label='scipy')     # scipy implementation
    
    # Error beetwen implementations
    # error = [y_s[i] - y_n[i] for i in range(len(y_n))]
    # plt.scatter(x_n, error, marker='.', label='error')
    
    # Aesthetics
    plt.title('Derivative of $f(x) = 1+tanh(x)/2$')
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.legend()
    # plt.gca().set_aspect('equal', adjustable='box') 
    
    plt.savefig("plot.pdf")
    # plt.show()

main()
