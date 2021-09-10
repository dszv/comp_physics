import numpy as np

A = np.array([[ 0,  1,  4,  1 ],
           [ 3,  4, -1, -1 ],
           [ 1, -4,  1,  5 ],
           [ 2, -2,  1,  3 ]],float)
v = np.array([ -4, 3, 9, 7 ],float)
N = len(v)

# Gaussian elimination
for m in range(N):

    # Partial pivoting
    arr = np.abs(np.copy(A[m:, m]))
    ind = m + np.argmax(arr, axis=0)

    A[[m, ind], :] = A[[ind, m], :]
    v[[m, ind]] = v[[ind, m]]

    # Divide by the diagonal element
    div = A[m,m]
    A[m,:] /= div
    v[m] /= div

    # Now subtract from the lower rows
    for i in range(m+1,N):
        mult = A[i,m]
        A[i,:] -= mult*A[m,:]
        v[i] -= mult*v[m]

# Backsubstitution
x = np.empty(N,float)
for m in range(N-1,-1,-1):
    x[m] = v[m]
    for i in range(m+1,N):
        x[m] -= A[m,i]*x[i]
print(x)
