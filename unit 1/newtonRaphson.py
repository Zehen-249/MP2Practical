import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**2
def fDash(x):
    return (2*x)

def newtonRaphson(xn):
    return xn-(f(xn)/fDash(xn))
tol=10**(-9)

x=[200]
y=[f(x[-1])]

while True:
    if(f(x[-1]))<=tol:
        root = x[-1]
        break
    else:
        x.append(newtonRaphson(x[-1]))
        y.append(x[-1]) 
print(root)
