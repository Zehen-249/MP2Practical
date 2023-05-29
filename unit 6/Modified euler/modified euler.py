# Mehendi Hasan B.SC.(H) Physics 2230248

#To Solve First Order Differential Equation by Modified Euler Method and compare it with Exact Solution and Inbuilt Function.

# import libraries

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint



def f(y,x):         #Differential Equation to solve
    return np.exp(x)

def f_exact(y,x):   #Exact Equation
    return np.exp(x)


def eulersMethod(xn,yn):
    return yn + h*(f(yn,xn))

print("\n\n\tMehendi Hasan\n\n\t2230248\n\n")


#User Inputs
x0=float(input("Enter Initial value of X: "))
y0=float(input("Enter Value of Y at Initial value of X: "))
h=float(input("Enter Step Size: "))
b=float(input("Enter last value of interval: "))

x_values=np.arange(0,b+h,h)
y_values=np.zeros(len(x_values))
y_exact=np.zeros(len(x_values))
y_odeint=np.zeros(len(x_values))
x_values[0]=x0
y_values[0]=y0
for i in range(len(y_values)-1):
    y_values[i+1] = y_values[i] +(h/2)*(f(y_values[i],x_values[i])+f(eulersMethod(x_values[i],y_values[i]),x_values[i+1]))

y_exact=np.array(f_exact(y_values,x_values))
y_odeint=odeint(f,y0,x_values)

plt.subplot(3,1,1)
plt.plot(x_values,y_values,label="F(x) Modified Eulers",color="red")
plt.xlabel("X Points")
plt.ylabel("Y Points")
plt.grid()
plt.legend()
plt.subplot(3,1,2)
plt.plot(x_values,y_exact,label="F(x) Exact",color="blue")
plt.xlabel("X Points")
plt.ylabel("Y Points")
plt.grid()
plt.legend()
plt.subplot(3,1,3)
plt.plot(x_values,y_odeint,label="F(x) Odeint",color="green")
plt.xlabel("X Points")
plt.ylabel("Y Points")
plt.grid()
plt.legend()
plt.suptitle("Mehendi Hasan B.SC.(H) Physics 2230248\nTo Solve First Order Differential Equation by Modified Euler Method and compare it with Exact Solution and Inbuilt Function.")
plt.show()






 