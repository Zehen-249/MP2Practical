# Mehendi Hasan B.SC.(H) Physics 2230248

#To Plot Current in RC circuit and potential ODE with DC source by RK2 Method, Exact solution, Inbuilt solver.

#importing libraries to be used
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as it

class RC:                   # Created a class of RC Circuit which have multiple Functions
    def current(I,t):       # Current v/s time graph using RK2's Method
        return ((-1)*(I))/(R*C)
    def current_exact(t):       # Current v/s time graph by ploting the solution equation of ODE
        return I0*(np.exp((-1)*t/(R*C)))
    def Vr(Vr,t):               # Voltage across resistor v/s time graph using RK2's Method
        return -Vr/(R*C)
    def VrExact(t):          # Voltage across resistor v/s time graph by ploting the solution equation of ODE
        return    V*(np.exp((-t)/(R*C)))
    def Vc(Vc,t):               # Voltage across capacitor v/s time graph using RK2's Method
        return (1/(R*C))*(V-Vc)
    def VcExact(t):          # Voltage across capacitor v/s time graph by ploting the solution equation of ODE
        return  V*(1-(np.exp((-t)/(R*C))))
    
print("\n\n\tMehendi Hasan\n\n\t2230248\n\nRC Circuit\n\n")
print("Capacitance is in Farad, resistance is in ohm,time is in second,charge in coulomb,voltage in volts.\n\n")


# input constant values
R=float(input('Enter the value of resistance in ohms:'))    #resistance
C=float(input('Enter the value of capacitance in farads:')) # capacitance
V=float(input('Enter the value of EMF in volts:'))          # EMF of battery
T_fin=float(input('Enter time instant at which current to be measured:'))       # time instant
h=0.001     #step size
time_array=np.arange(0,T_fin+h,h)       # X-coordinate (time)

#   Current v/s time
I0=V/R      #current in circuit at t=0
yPointsCurrent=np.zeros(len(time_array))       #initializing Y-coordinates as array of zeros of lenght time array(RK2 method )
yPointsCurrentExact=np.zeros(len(time_array))     #initializing Y-coordinates as array of zeros of lenght time array(solution Equation)
yPointsCurrent[0]=I0                              # initializing Initial value for euler's method
for i in range(len(time_array)-1):      # updating the array of zeros with help of euler's method and solution equation
    k1=h*RC.current(yPointsCurrent[i],time_array[i])
    k2=h*RC.current(yPointsCurrent[i]+k1,time_array[i]+h)
    delY=0.5*(k1+k2)
    yPointsCurrent[i+1]=yPointsCurrent[i]+delY
yPointsCurrentExact=RC.current_exact(time_array)                     # Solution Equation
solOdeintYPointsCurrent=it.odeint(RC.current,I0,time_array)             #odeint solution

#   Voltage across resistor v/s time
Vr0=V
yPointsVr=np.zeros(len(time_array))       #initializing Y-coordinates as array of zeros of lenght time array(RK2 method )
yPointsVrExact=np.zeros(len(time_array))     #initializing Y-coordinates as array of zeros of lenght time array(solution Equation)
yPointsVr[0]=Vr0                            # initializing Initial value for euler's method
for i in range(len(time_array)-1):      # updating the array of zeros with help of euler's method and solution equation
    k1=h*RC.Vr(yPointsVr[i],time_array[i])
    k2=h*RC.Vr(yPointsVr[i]+k1,time_array[i]+h)
    delY=0.5*(k1+k2)
    yPointsVr[i+1]=yPointsVr[i]+delY
yPointsVrExact=RC.VrExact(time_array)                     # Solution Equation
solOdeintYPointsVr=it.odeint(RC.Vr,Vr0,time_array)           #odeint solution

#   Voltage across capacitor v/s time
Vc0=0
yPointsVc=np.zeros(len(time_array))       #initializing Y-coordinates as array of zeros of lenght time array(RK2 method )
yPointsVcExact=np.zeros(len(time_array))     #initializing Y-coordinates as array of zeros of lenght time array(solution Equation)
yPointsVc[0]=Vc0                              # initializing Initial value for euler's method
for i in range(len(time_array)-1):      # updating the array of zeros with help of euler's method and solution equation
    k1=h*RC.Vc(yPointsVc[i],time_array[i])
    k2=h*RC.Vc(yPointsVc[i]+k1,time_array[i]+h)
    delY=0.5*(k1+k2)
    yPointsVc[i+1]=yPointsVc[i]+delY
yPointsVcExact=RC.VcExact(time_array)                     # Solution Equation
solOdeintYPointsVc=it.odeint(RC.Vc,Vc0,time_array)               #odeint solution

# plot of I v/s t
plt.subplot(3,2,1)
plt.plot(time_array,yPointsCurrent,color='red',label="I")
plt.xlabel('Time(s)')
plt.ylabel('Current(amps)')
plt.title("Current v/s time RK2's")
plt.grid('true')
plt.legend()
plt.subplot(3,2,2)
plt.plot(time_array,yPointsCurrentExact, color='blue',label="I")
plt.xlabel('Time(s)')
plt.ylabel('Current(amps)')
plt.title("Current v/s time Solution Equation")
plt.grid('true')
plt.legend()

# plot of Vr v/s t
plt.subplot(3,2,3)
plt.plot(time_array,yPointsVr,color='red',label="Vr")
plt.plot(time_array,yPointsVc,color='blue',label="Vc")
plt.xlabel('Time(s)')
plt.ylabel('(volts)')
plt.title("Vr and Vc v/s time RK2s ")
plt.grid('true')
plt.legend()
plt.subplot(3,2,4)
plt.plot(time_array,yPointsVrExact, color='blue',label="Vr")
plt.plot(time_array,yPointsVcExact, color='red',label="Vc")
plt.xlabel('Time(s)')
plt.ylabel("(volts)")
plt.title("Vr and Vc v/s time Solution equation")
plt.grid('true')
plt.legend()

plt.subplot(3,2,5)
plt.plot(time_array,solOdeintYPointsVr, color='blue',label="Vr")
plt.plot(time_array,solOdeintYPointsVc, color='red',label="Vc")
plt.xlabel('Time(s)')
plt.ylabel("(volts)")
plt.title("Vr and Vc v/s time Odeint Solution")
plt.grid('true')
plt.legend()

plt.subplot(3,2,6)
plt.plot(time_array,solOdeintYPointsCurrent, color='blue',label="Current")
plt.xlabel('Time(s)')
plt.ylabel("(volts)")
plt.title("Current v/s time Odeint Solution equation")
plt.grid('true')
plt.legend()
plt.suptitle("Mehendi Hasan B.SC.(H) Physics 2230248\nTo Plot Current in RC circuit and potential ODE with DC source by RK2 Method, Exact solution, Inbuilt solver.")
plt.show()
    
