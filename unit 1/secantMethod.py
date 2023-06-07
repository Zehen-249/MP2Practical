import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**2

def secantMethod(f,x0,x1,tolerance,maxIteration):
    for i in range(maxIteration):
        fx0=f(x0)
        fx1=f(x1)
        x_next=x1-(fx1*(x1-x0))/(fx1-fx0)
        if abs(x_next-x1)<tolerance:
            return x_next
        x0,x1=x1,x_next
    return None

root= secantMethod(f,1.5,2.5,1e-9,10000)
if root is not None:
    print(root)
else:
    print("try more interations")

