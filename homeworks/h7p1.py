# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 16:09:32 2021

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt
a=10
b=8/3
er=28

def f(r):
    x=r[0]
    y=r[1]
    z=r[2]
    fx=a*(y-x)
    fy=er*x-y-x*z
    fz=x*y-b*z
    return np.array([fx,fy,fz])


t,h=np.linspace(0,50,5000,retstep=True)
x=[]
y=[]
z=[]
r=np.array([0.0,1.0,0.0])
for i in (t):
    x.append(r[0])
    y.append(r[1])
    z.append(r[2])
    k1=f(r)*h
    k2=f(r+0.5*k1)*h
    k3=f(r+0.5*k2)*h
    k4=f(r+k3)*h
    r+=(k1+2*k2+2*k3+k4)/6


plt.plot(t,y)
plt.savefig("h7p1a.jpg",dpi=300)
plt.show()
plt.plot(x,z)
plt.savefig("h7p1b.jpg",dpi=300)
plt.show()
