# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 17:06:45 2021

@author: Abel
"""

import matplotlib.pyplot as plt
import numpy as np
a=np.loadtxt("stm.txt",float)
d_x=np.empty((663,676))  
d_y=np.empty((663,676))
I=np.empty((663,676))
h=2.5

for i in range(663):
    for j in range(676):
        if i<662:
            d_x[i][j]=(a[i+1][j]-a[i][j])/h
        else:
            d_x[i][j]=(a[i][j]-a[i-1][j])/h
       
for i in range(663):
    for j in range(676):
        if j<675:
            d_y[i][j]=(a[i][j+1]-a[i][j])/h
        else:
            d_y[i][j]=(a[i][j]-a[i][j-1])/h

for i in range(663):
    for j in range(676):
        I[i][j]=(np.cos(np.pi/4)*d_x[i][j]+np.sin(np.pi/4)*d_y[i][j])/(pow(d_x[i][j]**2+d_y[i][j]**2+1,0.5))

vmax=np.amax(I)
vmin=np.amin(I)
print(vmax,vmin)
plt.imshow(I,cmap="bone",origin="lower")
plt.savefig("sil.jpg",dpi=300)
plt.show()