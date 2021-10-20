# packages
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()
sns.set_style("darkgrid")

def main():
    # PART A
    # loading data
    piano = np.loadtxt("../../comp_physics/resources/piano.txt", float)
    ap = np.fft.rfft(piano)
    trumpet = np.loadtxt("../../comp_physics/resources/trumpet.txt", float)
    at = np.fft.rfft(trumpet)
    
    # plot
    plt.plot(np.absolute(ap)) # ap, at

    # aesthetics
    plt.title('Fourier coefficients')
    plt.xlabel('$k$')
    plt.ylabel('$| a_k |$')

    plt.savefig("h6p1a.pdf")

    # PART B
    fp_max = np.argmax(ap)*44100/100000
    ft_max = np.argmax(at)*44100/100000

    print("Piano: {0} Hz, Trumpet: {1} Hz.".format(fp_max, ft_max))

main()
