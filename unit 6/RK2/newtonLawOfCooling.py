# Mehendi Hasan B.SC.(H) Physics 2230248

# To Plot Newton's cooling law ODE by RK2 method, Exact solution & Inbuilt solver. 

#libraries
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as  it
def f(T,t):     # Differential Equation of cooling
    return (-K)*(T-Ts)
def fExact(T,t):
    Ts + ((T0-Ts)*np.etp((-K)*(t)))     # Exact Equation of cooling

print("\n\n\tMehendi Hasan\n\n\t2230248\n\n")
print("Newton's Law of Cooling\n\nTemperature is in Degree Celsius and time is in secons\n\n")

T0=int(input("Enter initial Temperature of Object: "))
Ts=int(input("Enter Surrounding temperature: "))
t=int(input("Enter time from t=0, at which temperature of Object to be calculated: "))

h=0.001     #step size
K=0.1      #cooling constant

t_values=np.arange(0,t+h,h)
T_values=np.zeros(len(t_values))
T_Exact=np.zeros(len(t_values))
T_odeint=np.zeros(len(t_values))
t_values[0]=0
T_values[0]=T0
T_odeint[0]=T0
T_Exact[0]=T0

for i in range(len(t_values)-1):
    k1=h*f(T_values[i],t_values[i])
    k2=h*f(T_values[i]+k1,t_values[i]+h)
    delY=0.5*(k1+k2)
    T_values[i+1]=T_values[i]+delY

T_Exact = Ts + ((T0-Ts)*np.exp((-K)*(t_values)))       #solution equation
T_odeint=it.odeint(f,T0,t_values)                                  #odeint solution

#ploting 
plt.subplot(3,1,1)
plt.plot(t_values,T_values,label="RK2 Solution",color="red")
plt.grid()
plt.title("RK2 Method")
plt.xlabel("Time")
plt.ylabel("Temperature of Object")
plt.legend()
plt.subplot(3,1,2)
plt.plot(t_values,T_Exact,label='Exact Equation Solution',color="blue")
plt.grid()
plt.title("Exact Equation")
plt.xlabel("Time")
plt.ylabel("Temperature of Object")
plt.subplot(3,1,3)
plt.plot(t_values,T_odeint,label='Odient Solution',color="orange")
plt.grid()
plt.title("Odeient Solution")
plt.xlabel("Time")
plt.ylabel("Temperature of Object")
plt.legend()
plt.suptitle("Mehendi Hasan B.SC.(H) Physics\nTo Plot Newton's cooling law ODE by RK2 method, Exact solution & Inbuilt solver")
plt.show()