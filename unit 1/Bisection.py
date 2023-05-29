import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 +5*x

a=float(input("Enter a: "))
b=float(input("Enter b: "))
if f(a)*f(b)<0:
    mid=(a+b)/2
    x=[mid]
    y=[f(mid)]
    while(f(x[-1])!=0):
        if (f(x[-1])*f(a)<0):
            b=mid
            mid=(a+b)/2
            x.append(mid)
            y.append(f(mid))
        elif (f(x[-1])*f(b)<0):
            a=mid
            mid=(a+b)/2
            x.append(mid)
            y.append(f(mid))
    else:
        root = x[-1]
    plt.plot(x,y)
    plt.plot(root,f(root),marker="o")
    plt.show()
else:
    print("The Values of a and b are not suitable for this method")