# loading packages
import numpy as np
import pylab as pl
import dcst
    

def main():
    # PART A
    data = np.loadtxt("./house.txt", float)
    pl.imshow(data)
    pl.savefig('h6p3a.pdf')
    pl.clf()
    
    # PART B
    fourier = np.empty_like(data)
    dim = 1024
    dim_blocks = 16
    num_blocks = int(dim/dim_blocks)

    for i in range(num_blocks):
        for j in range(num_blocks):
            fourier[dim_blocks*i : dim_blocks*i + dim_blocks, dim_blocks*j : dim_blocks*j + dim_blocks] = dcst.dct2(data[dim_blocks*i : dim_blocks*i + dim_blocks, dim_blocks*j : dim_blocks*j + dim_blocks])

    # PART C, D
    count = 0
    threshold = 100000 # 10, 20, 50, 100, etc.

    for i in range(dim):
        for j in range(dim):
            if np.absolute(fourier[i, j]) < threshold:
                fourier[i, j] = 0
                count += 1

    print("Compression ratio: {0:.2f}%".format(count*100/dim**2))

    # PART E
    inv_data = np.empty_like(data)

    for i in range(num_blocks):
        for j in range(num_blocks):
            inv_data[dim_blocks*i : dim_blocks*i + dim_blocks, dim_blocks*j : dim_blocks*j + dim_blocks] = dcst.idct2(fourier[dim_blocks*i : dim_blocks*i + dim_blocks, dim_blocks*j : dim_blocks*j + dim_blocks])

    # PART F
    pl.imshow(inv_data)
    pl.savefig('h6p3f.pdf')

main()
