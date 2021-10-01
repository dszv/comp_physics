# loading packages
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()
sns.set_style("darkgrid")


def main():
    # PART A
    data = np.loadtxt("../../comp_physics/resources/dow.txt", float)
    
    # plot
    plt.plot(data)

    # aesthetics
    plt.title('Dow Jones Industral Average')
    plt.xlabel('Day')
    plt.ylabel('Daily closing value')

    plt.savefig("h6p2a.pdf")
    plt.clf()

    # PART B
    f_coeff = np.fft.rfft(data)

    # plot
    plt.plot(np.absolute(f_coeff))

    # aesthetics
    plt.title('Fourier coefficients')
    plt.xlabel('$k$')
    plt.ylabel('$| a_k |$')

    plt.savefig("h6p2b.pdf")
    plt.clf()

    # PART C
    f_coeff1 = np.copy(f_coeff)
    for k in range(int(0.1*len(f_coeff1)), len(f_coeff1)):
        f_coeff1[k] = 0

    # PART D
    inv_data1 = np.fft.irfft(f_coeff1)
    
    # plot
    plt.plot(inv_data1)

    # aesthetics
    plt.title('Dow Jones Industral Average')
    plt.xlabel('Day')
    plt.ylabel('Daily closing value')

    plt.savefig("h6p2d.pdf")
    plt.clf()

    # PART E
    f_coeff2 = np.copy(f_coeff)
    for k in range(int(0.02*len(f_coeff2)), len(f_coeff2)):
        f_coeff2[k] = 0

    inv_data2 = np.fft.irfft(f_coeff2)
    
    # plot
    plt.plot(data)
    plt.plot(inv_data1)
    plt.plot(inv_data2)

    # aesthetics
    plt.title('Dow Jones Industral Average')
    plt.xlabel('Day')
    plt.ylabel('Daily closing value')

    plt.savefig("h6p2e.pdf")


main()
