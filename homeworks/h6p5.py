# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 14:51:31 2021

@author: user
"""


import numpy as np
import matplotlib.pyplot as plt
a=1
b=0.5
ga=0.5
de=2
def f(r):
    x=r[0]
    y=r[1]
    fx=a*x-b*x*y
    fy=ga*x*y-de*y
    return np.array([fx,fy])


t,h=np.linspace(0,30,3000,retstep=True)
x0=0
y0=0
x=[]
y=[]
r=np.array([2.0,2.0])
for i in (t):
    x.append(r[0])
    y.append(r[1])
    k1=f(r)*h
    k2=f(r+0.5*k1)*h
    k3=f(r+0.5*k2)*h
    k4=f(r+k3)*h
    r+=(k1+2*k2+2*k3+k4)/6


plt.plot(t,x,label="rabbits")
plt.plot(t,y,label="foxes")
# f,(ax,ax1)=plt.subplots(1,2)
# ax.plot(t,x)
# ax1.plot(t,y)
plt.savefig("LotkaV.jpg",dpi=300)
plt.legend()
plt.show()
