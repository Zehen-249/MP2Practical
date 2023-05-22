# Mehendi Hasan B.SC.(H) Physics 2230248

#To Solve First Order Differential Equation by RK2 Method and compare it with Exact Solution and Inbuilt Function.

# import libraries
import numpy as np
from scipy.integrate import odeint
from prettytable import PrettyTable
import matplotlib.pyplot as plt
tb=PrettyTable()


def f(y,x):         #Eqution to solve
    return np.exp(x)
def f_exact(y,x):
    return np.exp(x)

print("\n\n\tMehendi Hasan\n\n\t2230248\n\n")


#initial values
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
y_odeint[0]=y0
y_exact[0]=y0
for i in range(len(x_values)-1):
    k1=h*f(y_values[i],x_values[i])
    k2=h*f(y_values[i]+k1,x_values[i]+h)
    delY=0.5*(k1+k2)
    y_values[i+1]=y_values[i]+delY
y_exact=f_exact(y_exact,x_values)
y_odeint=odeint(f,y0,x_values)

plt.subplot(1,3,1)
plt.plot(x_values,y_values,label="RK2")
plt.xlabel("X Points")
plt.ylabel("Y Points")
plt.legend()

plt.subplot(1,3,2)
plt.plot(x_values,y_exact,label="Exact Solution")
plt.xlabel("X Points")
plt.ylabel("Y Points")
plt.legend()

plt.subplot(1,3,3)
plt.plot(x_values,y_odeint,label="Odeint solution")
plt.xlabel("X Points")
plt.ylabel("Y Points")
plt.legend()
plt.show()






