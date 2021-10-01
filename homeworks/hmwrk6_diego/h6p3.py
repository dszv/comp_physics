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
    num_blocks = int(dim/16)

    for i in range(num_blocks):
        for j in range(num_blocks):
            fourier[16*i:16*i+16, 16*j:16*j+16] = dcst.dct2(data[16*i:16*i+16, 16*j:16*j+16])

    # PART C, D
    count = 0
    threshold = 10000 # 10, 20, 50, 100, etc.

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
            inv_data[16*i:16*i+16, 16*j:16*j+16] = dcst.idct2(fourier[16*i:16*i+16, 16*j:16*j+16])

    # PART F
    pl.imshow(inv_data)
    pl.savefig('h6p3f.pdf')

main()
