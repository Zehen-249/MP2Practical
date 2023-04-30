# Euler's method 

# import libraries
import math
from prettytable import PrettyTable
import matplotlib.pyplot as plt
tb=PrettyTable()


def f(x):         #Eqution to solve
    return math.exp(x)

#initial values
x0=float(input("Enter Initial value of X: "))
y0=float(input("Enter Value of Y at Initial value of X: "))
h=float(input("Enter Step Size: "))
b=float(input("Enter last value of interval: "))
x_values=[x0]
y_values=[y0]
while x0<b:
    y1=y0+((h)*f(x0))
    y_values.append(y1)
    x0=x0+h
    x_values.append(x0)
    y0=y1
plt.plot(x_values,y_values,label="Funtion Curve")
plt.xlabel("X Points")
plt.ylabel("Y Points")
plt.legend
plt.show()






