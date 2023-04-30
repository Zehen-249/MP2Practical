# plot newton's law of cooling using euler's method and verify with the solution equation

#libraries
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as  it
def f(T,t):
    return (-K)*(T-Ts)

print("Newton's Law of Cooling\n\nTemperature is in Degree Celsius and time is in secons\n")

T0=int(input("Enter initial Temperature of Object: "))
Ts=int(input("Enter Surrounding temperature: "))
t=int(input("Enter time from t=0, at which temperature of Object to be calculated: "))

h=0.001
K=0.01

x_points=np.arange(0,t+h,h)
T=np.zeros(len(x_points))
TExact=np.zeros(len(x_points))

T[0]=T0
TExact[0]=T0
# print(x_points)
# print(x_points[200])
for i in range(len(x_points)-1):
    T[i+1]= (T[i] + (h*(f(T[i],x_points))))
    TExact[i+1] = Ts + ((T0-Ts)*np.exp((-K)*(x_points[i+1])))
solOdeint=it.odeint(f,T0,x_points)
# print(T)
# print(TExact)
plt.subplot(3,1,1)
plt.plot(x_points,T,label="Euler's Solution")
plt.xlabel("Time")
plt.ylabel("Temperature of Object")
plt.legend()
plt.subplot(3,1,2)
plt.plot(x_points,TExact,label='Exact Equation Solution')
plt.title("Exact Equation")
plt.xlabel("Time")
plt.ylabel("Temperature of Object")
plt.subplot(3,1,3)
plt.plot(x_points,solOdeint,label='Odient Solution')
plt.title("Odeient Solution")
plt.xlabel("Time")
plt.ylabel("Temperature of Object")
plt.legend()

plt.show()