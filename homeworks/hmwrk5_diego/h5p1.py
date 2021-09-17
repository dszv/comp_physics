import numpy as np

# must be a square matrix
a = np.array([[ 1,  4,  8,  4 ],
              [ 4,  2,  3,  7 ],
              [ 8,  3,  6,  9 ],
              [ 4,  7,  9,  2 ]], float)
n = a.shape[1]


def gs(i, A, Q):
    t = np.zeros_like(n)
    for j in range(i):
        t = t + np.dot(Q[:, j], A[:, i])*Q[:, j]
    return t

# PART B
def QR_decomposition(A):
    Q = np.zeros_like(A)
    R = np.zeros_like(A)

    u = A[:, 0] 
    q = u/np.linalg.norm(u)

    Q[:, 0] = q
    R[0, 0] = np.linalg.norm(u)

    for i in range(1, n):
        u = A[:, i] - gs(i, A, Q)
        q = u/np.linalg.norm(u)

        Q[:, i] = q
        R[i, i] = np.linalg.norm(u)
        for j in range(i):
            R[j, i] = np.dot(Q[:, j], A[:, i])

    return Q, R

def error(A):
    z = []
    for i in range(n):
        for j in range(n):
            if i != j:
                z.append(np.abs(A[i, j]))
    return max(z)


#PART C
def main():
    E = np.copy(a)

    # Create an nxn matrix V to hold the eigenvectors
    V = np.eye(n)

    while error(E) > 1.e-6:
        # Calculate the QR decomposition 
        Qi, Ri = QR_decomposition(E)
    
        # Update A to the new value A = RQ
        E = np.dot(Ri, Qi)
    
        # Multiply V on the right by Q
        V = np.dot(V, Qi)

    print("Eigenvalues: \n", [E[i,i] for i in range(n)])
    print("Eigenvectors: \n", V)

main()
