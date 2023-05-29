# Mehendi Hasan B.SC.(H) Physics 2230248

#To Plot Charging and Discharging of a capacitor in RC circuit ODE with DC source by Modified Euler Method, Exact solution, Inbuilt solver. 


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

def eulersMethod(xn,yn):
    return yn + h*(diff_equ_charging(yn,xn))

print("\n\n\tMehendi Hasan\n\n\t2230248\n\nRC Circuit Charging and Discharging of Capacitor\n\n")
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
Y_diff_charging=np.zeros(len(t_array))      #Initializing array for values of dependent variable(Modified Euler's method)
Y_Exact_charging=np.zeros(len(t_array))     #Initializing array for values of dependent variable(Solution equation)
Y_Exact_charging[0] = Y_diff_charging[0] = 0    #Initial values of dependent variable Y at dependent variable t=0 
for i in range(len(t_array)-1):                 #updating values of dependent variable
    #Modified Euler's Method
    Y_diff_charging[i+1] = Y_diff_charging[i] + (h/2)*(diff_equ_charging(Y_diff_charging[i],t_array[i])+diff_equ_charging(eulersMethod(t_array[i],Y_diff_charging[i]),t_array[i+1]))
Y_Exact_charging=Exact_equ_charging(t_array)                                              #Solution Equation
solOdeintCharging=it.odeint(diff_equ_charging,Y_diff_charging[0],t_array)       #Odeint solution

#Discharging of Capacitor
Y_diff_discharging=np.zeros(len(t_array))   #Initializing array for values of dependent variable(Modified Euler's method)
Y_Exact_discharging=np.zeros(len(t_array))  #Initializing array for values of dependent variable(Solution equation)
Y_Exact_discharging[0] = Y_diff_discharging[0] = Qmax   #Initial values of dependent variable Y at independent variable t=0 
for i in range(len(t_array)-1):                          # #updating values of dependent variable
    #Modified Euler's Method
    Y_diff_discharging[i+1] = Y_diff_discharging[i] + (h/2)*(diff_equ_discharging(Y_diff_discharging[i],t_array[i])+diff_equ_discharging(eulersMethod(t_array[i],Y_diff_discharging[i]),t_array[i+1]))
Y_Exact_discharging=Exact_equ_discharging(t_array)                                                     #Solution Equation
solOdeintDischarging=it.odeint(diff_equ_discharging,Y_diff_discharging[0],t_array)                                   #Odeint solution


#ploting all the values of dependent variable with respect to independent variable
plt.subplot(3,2,2)
plt.plot(t_array,Y_diff_charging,color='blue',label="Charge")
plt.grid()
plt.xlabel("Time")
plt.ylabel("Charge at Capacitor")
plt.title("Modified Euler's Solution of Charging")
plt.legend()
plt.subplot(3,2,4)
plt.plot(t_array,Y_Exact_charging,color='red',label="Charge")
plt.grid()
plt.xlabel("Time")
plt.ylabel("Charge at Capacitor")
plt.title("Exact Equation of Charging")
plt.legend()
plt.subplot(3,2,1)
plt.plot(t_array,Y_diff_discharging,color='orange',label="Charge")
plt.grid()
plt.xlabel("Time")
plt.ylabel("Charge at Capacitor")
plt.title("Modified Euler's Solution of Discharging")
plt.legend()
plt.subplot(3,2,3)
plt.plot(t_array,Y_Exact_discharging,color='green',label="Charge")
plt.grid()
plt.xlabel("Time")
plt.ylabel("Charge at Capacitor")
plt.title("Exact Equation of Discharging")
plt.legend()
plt.subplot(3,2,6)
plt.plot(t_array,solOdeintCharging,color='orange',label="Charge")
plt.grid()
plt.xlabel("Time")
plt.ylabel("Charge at Capacitor")
plt.title("Odeint Solution of Charging")
plt.legend()
plt.subplot(3,2,5)
plt.plot(t_array,solOdeintDischarging,color='red',label="Charge")
plt.grid()
plt.xlabel("Time")
plt.ylabel("Charge at Capacitor")
plt.title("Odeint Solution of Discharging")
plt.legend()
plt.suptitle("Mehendi Hasan B.SC.(H) Physics 2230248\nTo Plot Charging and Discharging of a capacitor in RC circuit ODE with DC source by Modified Euler Method, Exact solution, Inbuilt solver")

plt.show()
