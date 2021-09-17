import numpy as np
import numpy.linalg as la

# PART B "God-given units"
L  = (5.e-10)/(1.97337e-7)
hb = 1 
M  = (9.1094e-31)/(1.782662e-36)
a  = 10

def h(m, n):
    A = (1/(M * L)) * ((n * np.pi * hb)/L)**2
    B = (2 * a)/L**2
    
    if m == n:
        return A * (L/2) + B * (L**2/4)
    elif (m + n) % 2 == 1:
        return B * (-(2 * L/np.pi)**2 * (m * n)/(m**2 - n**2)**2)
    else:
        return 0


def main():
    # PART C, D
    N = 100
    H = np.zeros((N, N), float)
    
    for i in range(N):
        for j in range(i + 1):
            H[i, j] = h(i + 1, j + 1)
    
    E = la.eigvalsh(H)
    print(E)

main()
