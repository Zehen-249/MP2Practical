import math
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as it

def diff_equ_charging(q,t):
    return ((C*E - q)/(R*C))

def Exact_equ_charging(t):
    return (C*E)*(1-(math.exp(((-1)*t)/(R*C))))

def diff_equ_discharging(q,t):
    return ((-1)*q)/(R*C)

def Exact_equ_discharging(t):
    return ((C*E)*(math.exp(((-1)*t)/(R*C))))

print("\n\nMehendi Hasan\n\nRC Circuit\n\n")
print("Capacitance is in Farad, resistance is in ohm,time is in second,charge in coulomb,voltage in volts.\n\n")

C=float(input("Enter Capacitance of Capacitor: "))
E=float(input("Enter EMF of Battery: "))
R=float(input("Enter Resistance of Resistor: "))
t=float(input("Enter time instant at which charge on capacitor to be calculated: "))

h=0.1
Qmax=C*E
t_array=np.arange(0,t+h,h)
#Charging of Capacitor
Y_diff_charging=np.zeros(len(t_array))
Y_Exact_charging=np.zeros(len(t_array))
Y_Exact_charging[0] = Y_diff_charging[0] = 0
for i in range(len(t_array)-1):
    Y_diff_charging[i+1]=Y_diff_charging[i] + h*(diff_equ_charging(Y_diff_charging[i],t_array[i]))
    Y_Exact_charging[i+1]=Exact_equ_charging(t_array[i+1])
solOdeintCharging=it.odeint(diff_equ_charging,Y_diff_charging[0],t_array)

#Discharging of Capacitor
Y_diff_discharging=np.zeros(len(t_array))
Y_Exact_discharging=np.zeros(len(t_array))
Y_Exact_discharging[0] = Y_diff_discharging[0] = Qmax
for i in range(len(t_array)-1):
    Y_diff_discharging[i+1]=Y_diff_discharging[i] + h*(diff_equ_discharging(Y_diff_discharging[i],t_array[i]))
    Y_Exact_discharging[i+1]=Exact_equ_discharging(t_array[i+1])
solOdeintDischarging=it.odeint(diff_equ_discharging,Y_diff_discharging[0],t_array)



plt.subplot(3,2,2)
plt.plot(t_array,Y_diff_charging,color='blue',label="Charge")
plt.xlabel("Time")
plt.ylabel("Charge at Capacitor")
plt.title("Euler's Solution of Charging")
plt.legend()
plt.subplot(3,2,4)
plt.plot(t_array,Y_Exact_charging,color='red',label="Charge")
plt.xlabel("Time")
plt.ylabel("Charge at Capacitor")
plt.title("Exact Equation Solution of Charging")
plt.legend()
plt.subplot(3,2,1)
plt.plot(t_array,Y_diff_discharging,color='orange',label="Charge")
plt.xlabel("Time")
plt.ylabel("Charge at Capacitor")
plt.title("Euler's Solution of Discharging")
plt.legend()
plt.subplot(3,2,3)
plt.plot(t_array,Y_Exact_discharging,color='green',label="Charge")
plt.xlabel("Time")
plt.ylabel("Charge at Capacitor")
plt.title("Exact Equation Solution of Discharging")
plt.legend()
plt.subplot(3,2,6)
plt.plot(t_array,solOdeintCharging,color='orange',label="Charge")
plt.xlabel("Time")
plt.ylabel("Charge at Capacitor")
plt.title("Odeint Solution of Charging")
plt.legend()
plt.subplot(3,2,5)
plt.plot(t_array,solOdeintDischarging,color='red',label="Charge")
plt.xlabel("Time")
plt.ylabel("Charge at Capacitor")
plt.title("Odeint Solution of Discharging")
plt.legend()


plt.show()
