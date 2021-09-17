import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()
sns.set_style("darkgrid")

import numpy as np
import scipy.integrate as int

# parameters
h  = 6.6260e-34
c  = 2.9979e+8
kB = 1.3806e-23
l1 = 390.0e-9
l2 = 750.0e-9

#PART A
def integrand(x):
    return (x**3)/(np.exp(x) - 1)

def efficiency(T):
    # integration limits
    a = h*c/(l2*kB*T)
    b = h*c/(l1*kB*T)

    return (15/np.pi**4)*(int.fixed_quad(integrand, a, b, n=100)[0])

def main():
    T = np.arange(300, 10000, 1)
    N = []
    
    for t in T:
        N.append(efficiency(t))
    
    # plot
    plt.plot(T, N, color='black')
    
    # aesthetics
    plt.title('Efficiency')
    plt.xlabel('$T (K)$')
    plt.ylabel(r'$\eta $')
    # plt.gca().set_aspect('equal', adjustable='box') 
    
    plt.savefig("h5p4.pdf")

main()
