import matplotlib.pyplot as plt
import numpy as np
def bisection_method(f, a, b, tolerance=1e-6, max_iterations=100000):
    x=[]
    y=[]
    if f(a) * f(b) >= 0:
        raise ValueError("The function must have opposite signs at the endpoints of the interval.")

    for iteration in range(1, max_iterations + 1):
        c = (a + b) / 2
        x.append(c)
        y.append(f(c))
        if f(c) == 0 or abs(b - a) / 2 < tolerance:
            plt.plot(x,y,"r--")
            plt.plot(x[-1],0,marker="o",label="root")
            plt.legend()
            plt.show()
            print(x)
            return c
        
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    raise RuntimeError("The method did not converge within the maximum number of iterations.")

# Example usage
def f(x):
    return np.sin(x)

root = bisection_method(f,2*np.pi/3, -(np.pi/2))
print("Approximate root:", root)