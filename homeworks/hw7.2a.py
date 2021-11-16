# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 12:47:18 2021

@author: Abel
"""

import numpy as np
import matplotlib.pyplot as plt

g=9.81
l=0.1

def f(r):
    the=r[0]
    ome=r[1]
    fthe=ome
    fome=-(g/l)*np.sin(the)
    return np.array([fthe,fome],float)


t,h=np.linspace(0,30,1000,retstep=True)
the0=0
ome0=0
the=[]
ome=[]
r=np.array([179*np.pi/180,0.0])
for i in (t):
    the.append(r[0])
    ome.append(r[1])
    k1=f(r)*h
    k2=f(r+0.5*k1)*h
    k3=f(r+0.5*k2)*h
    k4=f(r+k3)*h
    r+=(k1+2*k2+2*k3+k4)/6


plt.plot(t,the)
plt.savefig("h7p2a.jpg",dpi=300)
plt.show()


import matplotlib.animation as animation
theso=np.array(the)
fig=plt.figure()
ax=fig.gca()

def actualizar(i):
    ax.clear()
    plt.plot([0,l*np.sin(theso[i])],[0,-l*np.cos(theso[i])],'b-')
    plt.plot(l*np.sin(theso[i]),-l*np.cos(theso[i]), 'ro')
    plt.title(str(round(t[i],3)))
    ax.set_aspect('equal', adjustable='box') 
    plt.xlim(-l,l)
    plt.ylim(-l,l)

ani=animation.FuncAnimation(fig,actualizar,range(len(t)))

ani.save('Pendulum.gif', writer='Pillow', fps=10)
plt.show()
    
    

