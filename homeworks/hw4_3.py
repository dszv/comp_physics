# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 13:11:54 2021

@author: Abel"""
import matplotlib.pyplot as plt
import numpy as np
a=np.loadtxt("altitude.txt",float)
d_x=np.empty((512,1024))  
d_y=np.empty((512,1024))
I=np.empty((512,1024))
h=30000

for i in range(512):
    for j in range(1024):
        if i<511:
            d_x[i][j]=(a[i+1][j]-a[i][j])/h
        else:
            d_x[i][j]=(a[i][j]-a[i-1][j])/h
       
for i in range(512):
    for j in range(1024):
        if j<1023:
            d_y[i][j]=(a[i][j+1]-a[i][j])/h
        else:
            d_y[i][j]=(a[i][j]-a[i][j-1])/h

for i in range(512):
    for j in range(1024):
        I[i][j]=(np.cos(np.pi/4)*d_x[i][j]+np.sin(np.pi/4)*d_y[i][j])/(pow(d_x[i][j]**2+d_y[i][j]**2+1,0.5))

vmax=np.amax(I)
vmin=np.amin(I)
print(vmax,vmin)
plt.imshow(I)
plt.colorbar()
plt.savefig("mapa.jpg",dpi=300)
plt.show()