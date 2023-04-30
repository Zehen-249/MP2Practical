#RC CIRCUIT plot Current v/s time, Voltage across resistor v/s time, Voltage across capacitor v/s time using Euler's meethod and 
# verify it by plotting exact solution equation


#importing libraries to be used
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as it

class RC:                   # Created a class of RC Circuit which have multiple Functions
    def current(I,t):       # Current v/s time graph using Euler's Method
        return ((-1)*(I))/(R*C)
    def current_exact(t):       # Current v/s time graph by ploting the solution equation of ODE
        return I0*(np.exp((-1)*t/(R*C)))
    def Vr(Vr,t):               # Voltage across resistor v/s time graph using Euler's Method
        return -Vr/(R*C)
    def VrExact(t):          # Voltage across resistor v/s time graph by ploting the solution equation of ODE
        return    V*(np.exp((-t)/(R*C)))
    def Vc(Vc,t):               # Voltage across capacitor v/s time graph using Euler's Method
        return (1/(R*C))*(V-Vc)
    def VcExact(t):          # Voltage across capacitor v/s time graph by ploting the solution equation of ODE
        return  V*(1-(np.exp((-t)/(R*C))))
    
print("Mehendi Hasan\n\nRC Circuit\n\n")
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
yPointsCurrent=np.zeros(len(time_array))       #initializing Y-coordinates as array of zeros of lenght time array(Euler method )
yPointsCurrentExact=np.zeros(len(time_array))     #initializing Y-coordinates as array of zeros of lenght time array(solution Equation)
yPointsCurrent[0]=I0                              # initializing Initial value for euler's method
for i in range(len(time_array)-1):      # updating the array of zeros with help of euler's method and solution equation
    yPointsCurrent[i+1]=yPointsCurrent[i]+h*RC.current(yPointsCurrent[i],time_array[i])      #Euler's Method
    yPointsCurrentExact[i]=RC.current_exact(time_array[i])                     # Solution Equation
solOdeintYPointsCurrent=it.odeint(RC.current,I0,time_array)

#   Voltage across resistor v/s time
Vr0=V
yPointsVr=np.zeros(len(time_array))       #initializing Y-coordinates as array of zeros of lenght time array(Euler method )
yPointsVrExact=np.zeros(len(time_array))     #initializing Y-coordinates as array of zeros of lenght time array(solution Equation)
yPointsVr[0]=Vr0                            # initializing Initial value for euler's method
for i in range(len(time_array)-1):      # updating the array of zeros with help of euler's method and solution equation
    yPointsVr[i+1]=yPointsVr[i]+h*RC.Vr(yPointsVr[i],time_array[i])      #Euler's Method
    yPointsVrExact[i]=RC.VrExact(time_array[i])                     # Solution Equation
solOdeintYPointsVr=it.odeint(RC.Vr,Vr0,time_array)

#   Voltage across capacitor v/s time
Vc0=0
yPointsVc=np.zeros(len(time_array))       #initializing Y-coordinates as array of zeros of lenght time array(Euler method )
yPointsVcExact=np.zeros(len(time_array))     #initializing Y-coordinates as array of zeros of lenght time array(solution Equation)
yPointsVc[0]=Vc0                              # initializing Initial value for euler's method
for i in range(len(time_array)-1):      # updating the array of zeros with help of euler's method and solution equation
    yPointsVc[i+1]=yPointsVc[i]+h*RC.Vc(yPointsVc[i],time_array[i])      #Euler's Method
    yPointsVcExact[i+1]=RC.VcExact(time_array[i+1])                     # Solution Equation
solOdeintYPointsVc=it.odeint(RC.Vc,Vc0,time_array)

# plot of I v/s t
plt.subplot(3,2,1)
plt.plot(time_array,yPointsCurrent,color='red',label="I")
plt.xlabel('Time(s)')
plt.ylabel('Current(amps)')
plt.title("Current v/s time Euler's")
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
plt.title("Vr and Vc v/s time Eulers ")
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

plt.show()
    