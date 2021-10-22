# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 17:03:49 2021

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt

g=9.81
l=0.4
m=1
def f(r):
    th1=r[0]
    th2=r[1]
    om1=r[2]
    om2=r[3]
    fth1=om1
    fth2=om2
    fom1=-(om1**2*np.sin(2*th1-2*th2)+2*om2**2*np.sin(th1-th2)
           +(g/l)*(np.sin(th1-2*th2)+3*np.sin(th1)))/(3-np.cos(2*th1-2*th2))
    fom2=(4*om1**2*np.sin(th1-th2)+om2**2*np.sin(2*th1-2*th2)
           +2*(g/l)*(np.sin(2*th1-th2)-np.sin(th2)))/(3-np.cos(2*th1-2*th2))
    
    return np.array([fth1,fth2,fom1,fom2],float)


t,h=np.linspace(0,100,50000,retstep=True)
the0=0
ome0=0
th1=[]
th2=[]
om1=[]
om2=[]
E=[]
r=np.array([90*np.pi/180,90*np.pi/180,0.0,0.0])
for i in (t):
    E.append(m*l**2*(r[2]**2+0.5*r[3]**2+r[2]*r[3]*np.cos(r[0]-r[1]))-m*g*l*(2*np.cos(r[0])+np.cos(r[1])))
    k1=f(r)*h
    k2=f(r+0.5*k1)*h
    k3=f(r+0.5*k2)*h
    k4=f(r+k3)*h
    r+=(k1+2*k2+2*k3+k4)/6


plt.plot(t,E)
plt.savefig("h7p2c.jpg",dpi=300)
plt.show()