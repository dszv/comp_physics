# loading packages
import numpy as np
import dcst

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()
sns.set_style("darkgrid")


def main():
    # PART F
    data = np.loadtxt("../../comp_physics/resources/dow2.txt", float)
    
    f_coeff = np.fft.rfft(data)

    f_coeff1 = np.copy(f_coeff)
    for k in range(int(0.02*len(f_coeff1)), len(f_coeff1)):
        f_coeff1[k] = 0

    inv_data2 = np.fft.irfft(f_coeff1)
    
    # plot
    plt.plot(data)
    plt.plot(inv_data2)

    # aesthetics
    plt.title('Dow Jones Industral Average')
    plt.xlabel('Day')
    plt.ylabel('Daily closing value')

    plt.savefig("h6p2f.pdf")
    plt.clf()

    # PART G
    f_coeff = dcst.dct(data)

    f_coeff2 = np.copy(f_coeff)
    for k in range(int(0.02*len(f_coeff2)), len(f_coeff2)):
        f_coeff2[k] = 0

    inv_data2 = dcst.idct(f_coeff2)
    
    # plot
    plt.plot(data)
    plt.plot(inv_data2)

    # aesthetics
    plt.title('Dow Jones Industral Average')
    plt.xlabel('Day')
    plt.ylabel('Daily closing value')

    plt.savefig("h6p2g.pdf")


main()
