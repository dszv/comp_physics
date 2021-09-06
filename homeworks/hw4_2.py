# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 15:52:22 2021

@author: user
"""


def f(x):
    return x**4-2*x+1

def df(x,h):
    return (f(x+h/2)-f(x-h/2))/h

a=0
b=2
N=10
h=(b-a)/N
#x1,h=np.linspace(a,b,N+1, retstep=True)
s=0.5*h*(f(a)+f(b))
for i in range(N-1):
    s+=h*f(a+(i+1)*h)

h1=0.00001
I=(s+(h**2)*(df(0,h1)-df(2,h1))/12)
print("valor real es: 4.4")
print("trapezio: %f"  %s)
print("Maclaurin:%f" %I)
