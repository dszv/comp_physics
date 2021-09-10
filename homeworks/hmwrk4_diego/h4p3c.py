# loading packages
import numpy as np
import pylab as pl
# from scipy.misc import derivative


h = 2.5
phi = np.pi/4

def intensity(phi, wx, wy):
    return (np.cos(phi)*wx + np.sin(phi)*wy)/(np.sqrt(wx**2 + wy**2 + 1))


def main():
    # PART A
    # loading data
    w = np.loadtxt("../../comp_physics/resources/stm.txt", float)
    pl.imshow(w)
    # pl.colorbar()
    pl.savefig("p3.pdf")
    
    # partial derivative of w wrt x
    Dxw = np.empty(w.shape)
    for i in np.arange(w.shape[1]):
        Dxw[0, i] = (w[1, i] - w[0, i])/h
        Dxw[-1, i] = (w[-1, i] - w[-1 - 1, i])/h
        
        for j in np.arange(1, w.shape[0] - 1):
            Dxw[j, i] = (w[j + 1, i] - w[j - 1, i])/(2*h)
            
    # partial derivative of w wrt y
    Dyw = np.empty(w.shape)
    for i in np.arange(w.shape[0]):
        Dyw[i, 0] = (w[i, 1] - w[i, 0])/h
        Dyw[i, -1] = (w[i, -1] - w[i, -1 - 1])/h

        for j in np.arange(1, w.shape[1] - 1):
            Dyw[i, j] = (w[i, j + 1] - w[i, j - 1])/(2*h)

    # PART B
    I = np.zeros(w.shape)
    for i in np.arange(I.shape[0]):
        for j in np.arange(I.shape[1]):
            I[i, j] = intensity(phi, Dxw[i, j], Dyw[i, j])

    pl.imshow(I)
    pl.colorbar()
    pl.savefig("p4.pdf")


main()
