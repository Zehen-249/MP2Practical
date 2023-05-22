# Mehendi Hasan B.SC.(H) Physics 2230248
#To Plot Current in RL circuit ODE with DC source by RK2 Method, Exact solution, Inbuilt solver.

#importing libraries to be used
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as it

def diffEquation(i,t):
    return (V/L)-((R*i)/L)

def solEquation(i,t):
    return (V/R)*(1-(np.exp((((-1)*R)*t)/L)))

print("\n\n\tMehendi Hasan\n\n\t2230248\n\nVariation of curent with time in RL Circuit \n\n")
print("Resistance is in ohm,time is in second,Inductance in henry,voltage in volts.\n\n")

#taking inputs from user for the terms envoled in equations
L=float(input("Enter Inductance of Inductor: "))
V=float(input("Enter EMF of Battery: "))
R=float(input("Enter Resistance of Resistor: "))
t=float(input("Enter time instant at which Current through inductor to be calculated: "))

h=0.001     #step size
time_array=np.arange(0,t+h,h)       # X-coordinate (time)

#   Current v/s time
I0=0      #current in circuit at t=0
yPointsCurrent=np.zeros(len(time_array))       #initializing Y-coordinates as array of zeros of lenght time array(RK2 method )
yPointsCurrentExact=np.zeros(len(time_array))     #initializing Y-coordinates as array of zeros of lenght time array(solution Equation)
yPointsCurrent[0]=I0 
yPointsCurrentExact[0]=I0                             # initializing Initial value for euler's method
for i in range(len(time_array)-1):      # updating the array of zeros with help of euler's method and solution equation
    yPointsCurrent[i+1]=yPointsCurrent[i]+h*diffEquation(yPointsCurrent[i],time_array[i])      #RK2's Method
    k1=h*diffEquation(yPointsCurrent[i],time_array[i])
    k2=h*diffEquation(yPointsCurrent[i]+k1,time_array[i]+h)
    delY=0.5*(k1+k2)
    yPointsCurrent[i+1]=yPointsCurrent[i]+delY
yPointsCurrentExact=solEquation(yPointsCurrentExact,time_array)                     # Solution Equation
solOdeintYPointsCurrent=it.odeint(diffEquation,I0,time_array)             #odeint solution

# plot of I v/s t
plt.subplot(1,3,1)
plt.plot(time_array,yPointsCurrent,color='red',label="I RK2")
plt.xlabel('Time(s)')
plt.ylabel("Current(Ampere)")
plt.title("Current v/s time RK2's")
plt.grid('true')
plt.legend()
plt.subplot(1,3,2)
plt.plot(time_array,yPointsCurrentExact, color='blue',label="I")
plt.xlabel('Time(s)')
plt.ylabel("Current(Ampere)")
plt.title("Current v/s time Solution Equation")
plt.grid('true')
plt.legend()
plt.subplot(1,3,3)
plt.plot(time_array,solOdeintYPointsCurrent, color='green',label="Current")
plt.xlabel('Time(s)')
plt.ylabel("Current(Ampere)")
plt.title("Current v/s time Odeint Solution equation")
plt.grid('true')
plt.suptitle("Mehendi Hasan B.SC.(H) Physics 2230248\nTo Plot Current in RL circuit ODE with DC source by RK2 Method, Exact solution, Inbuilt solver.")
plt.legend()


plt.show()