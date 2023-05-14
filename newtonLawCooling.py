# Mehendi Hasan B.SC.(H) Physics 2230248

# To Plot Newton's cooling law ODE by Euler method, Exact solution & Inbuilt solver. 

#libraries
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as  it
def f(T,t):     # Differential Equation of cooling
    return (-K)*(T-Ts)

print("\n\n\tMehendi Hasan\n\n\t2230248\n\n")
print("Newton's Law of Cooling\n\nTemperature is in Degree Celsius and time is in secons\n\n")

T0=int(input("Enter initial Temperature of Object: "))
Ts=int(input("Enter Surrounding temperature: "))
t=int(input("Enter time from t=0, at which temperature of Object to be calculated: "))

h=0.001     #step size
K=0.1      #cooling constant

x_points=np.arange(0,t+h,h)
T=np.zeros(len(x_points))
TExact=np.zeros(len(x_points))

T[0]=T0
TExact[0]=T0
# print(x_points)
# print(x_points[200])
for i in range(len(x_points)-1):
    T[i+1]= (T[i] + (h*(f(T[i],x_points))))                         #eulers method
    TExact[i+1] = Ts + ((T0-Ts)*np.exp((-K)*(x_points[i+1])))       #solution equation
solOdeint=it.odeint(f,T0,x_points)                                  #odeint solution

#ploting 
plt.subplot(3,1,1)
plt.plot(x_points,T,label="Euler's Solution")
plt.title("Euler's Method")
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