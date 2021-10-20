# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 12:22:34 2021

@author: Abel
"""

import numpy as np
import matplotlib.pyplot as plt


def V_in(x):
    if int(2*x)%2==0:
        return 1
    else:
        return -1
    
def f(x,t):
    return (V_in(t)-V0)/(rc)
    
rc=0.05
t,h=np.linspace(0,4,1000,retstep=True)
V=[]
V_out=[]
V0=0

for i in t:
    V.append(V_in(i)) 
    V_out.append(V0)
    k1=h*f(V0,i)
    k2=h*f(V0+0.5*k1,i+0.5*h)
    k3=h*f(V0+0.5*k2,i+0.5*h)
    k4=h*f(V0+k3,i+h)
    V0+=(k1+2*k2+2*k3+k4)/6

f, (ax1,ax2) =plt.subplots(1,2)
ax1.plot(t,V_out)
ax2.plot(t,V)
plt.savefig("low-pass.jpg",dpi=300)
plt.show()


