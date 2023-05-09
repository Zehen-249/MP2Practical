#plot Charging and Discharging of Capacitor in  RC Circuit usin Euler's method and verify it by ploting Solution equation and sol of odeint function

#importing libraries
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as it

def diff_equ_charging(q,t):    # Differential Equation of Charging
    return ((C*E - q)/(R*C))

def Exact_equ_charging(t):      #Solution equation of Differential Equation of Charging
    return (C*E)*(1-(np.exp(((-1)*t)/(R*C))))

def diff_equ_discharging(q,t):  # Differential Equation of Discharging
    return ((-1)*q)/(R*C)

def Exact_equ_discharging(t):       #Solution equation of Differential Equation of Discharging
    return ((C*E)*(np.exp(((-1)*t)/(R*C))))

print("\n\nMehendi Hasan\n\nRC Circuit Charging and Discharging of Capacitor\n\n")
print("Capacitance is in Farad, resistance is in ohm,time is in second,charge in coulomb,voltage in volts.\n\n")

#taking inputs from user for the terms envoled in equations
C=float(input("Enter Capacitance of Capacitor: "))
E=float(input("Enter EMF of Battery: "))
R=float(input("Enter Resistance of Resistor: "))
t=float(input("Enter time instant at which charge on capacitor to be calculated: "))

h=0.1       #Step size

Qmax=C*E        #max value of charge on capacitor

t_array=np.arange(0,t+h,h)      #initializing time array(independent Variable)


#Charging of Capacitor
Y_diff_charging=np.zeros(len(t_array))      #Initializing array for values of dependent variable(Euler's method)
Y_Exact_charging=np.zeros(len(t_array))     #Initializing array for values of dependent variable(Solution equation)
Y_Exact_charging[0] = Y_diff_charging[0] = 0    #Initial values of dependent variable Y at dependent variable t=0 
for i in range(len(t_array)-1):                 #updating values of dependent variable
    Y_diff_charging[i+1]=Y_diff_charging[i] + h*(diff_equ_charging(Y_diff_charging[i],t_array[i]))      #Euler's Method
    Y_Exact_charging[i+1]=Exact_equ_charging(t_array[i+1])                                              #Solution Equation
solOdeintCharging=it.odeint(diff_equ_charging,Y_diff_charging[0],t_array)       #Odeint solution

#Discharging of Capacitor
Y_diff_discharging=np.zeros(len(t_array))   #Initializing array for values of dependent variable(Euler's method)
Y_Exact_discharging=np.zeros(len(t_array))  #Initializing array for values of dependent variable(Solution equation)
Y_Exact_discharging[0] = Y_diff_discharging[0] = Qmax   #Initial values of dependent variable Y at independent variable t=0 
for i in range(len(t_array)-1):                          # #updating values of dependent variable
    Y_diff_discharging[i+1]=Y_diff_discharging[i] + h*(diff_equ_discharging(Y_diff_discharging[i],t_array[i]))       #Euler's Method
    Y_Exact_discharging[i+1]=Exact_equ_discharging(t_array[i+1])                                                     #Solution Equation
solOdeintDischarging=it.odeint(diff_equ_discharging,Y_diff_discharging[0],t_array)                                   #Odeint solution


#ploting all the values of dependent variable with respect to independent variable
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
