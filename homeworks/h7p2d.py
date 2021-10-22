# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 15:52:30 2021

@author: user
"""


import numpy as np
import matplotlib.pyplot as plt

g=9.81
l=0.4

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


t,h=np.linspace(0,30,1000,retstep=True)
the0=0
ome0=0
th1=[]
th2=[]
om1=[]
om2=[]
r=np.array([90*np.pi/180,90*np.pi/180,0.0,0.0])
for i in (t):
    th1.append(r[0])
    th2.append(r[1])
    om1.append(r[2])
    om2.append(r[3])
    
    k1=f(r)*h
    k2=f(r+0.5*k1)*h
    k3=f(r+0.5*k2)*h
    k4=f(r+k3)*h
    r+=(k1+2*k2+2*k3+k4)/6


# plt.plot(t,th1)
# plt.savefig("h7p2c.jpg",dpi=300)
# plt.show()

import matplotlib.animation as animation
ths1=np.array(th1)
ths2=np.array(th2)
fig=plt.figure()
ax=fig.gca()

def actualizar(i):
    ax.clear()
    plt.plot([0,l*np.sin(ths1[i])],[0,-l*np.cos(ths1[i])],'b-')
    plt.plot([l*np.sin(ths1[i]),l*np.sin(ths1[i])+l*np.sin(ths2[i])],
             [-l*np.cos(ths1[i]),-l*np.cos(ths1[i])-l*np.cos(ths2[i])],'b-')
    plt.plot(l*np.sin(ths1[i]),-l*np.cos(ths1[i]), 'ro')
    plt.plot(l*np.sin(ths1[i])+l*np.sin(ths2[i]),-l*np.cos(ths1[i])-l*np.cos(ths2[i]), 'ro')
    plt.title(str(round(t[i],3)))
    ax.set_aspect('equal', adjustable='box') 
    plt.xlim(-2*l,2*l)
    plt.ylim(-2*l,2*l)

ani=animation.FuncAnimation(fig,actualizar,range(len(t)))

ani.save('PendulumDo.gif', writer='Pillow', fps=10)
plt.show()
