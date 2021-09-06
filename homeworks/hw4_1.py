# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 18:10:47 2021
"""

import numpy as np
import matplotlib.pyplot as plt
def df0(x):
    return (1/np.cosh(2*x))**2
def f(x):
    return 1+0.5*np.tanh(2*x)

def df(x,h):
    return (f(x+h/2)-f(x-h/2))/h

x0=np.linspace(-2.0,2.0,1000)

x1,h=np.linspace(-2.0,2.0,200,retstep=True)

d=[]
for x in x1:
    d.append(df(x,h))
    

plt.plot(x0,df0(x0),"r",lw=2,label="derivada real")
plt.plot(x1,d,"b--",label="dif. central, h=%.3f"%h)
plt.title("derivada por diferencia central", )
plt.ylabel("f'(x)")
plt.xlabel("x")
plt.savefig("der.pdf",dpi=300)
plt.legend(loc="upper right")
plt.show()