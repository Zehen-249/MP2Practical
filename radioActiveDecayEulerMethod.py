#plot Radioactive Decay using euler's method and verify it by ploting solution equation and odeint solution

#importing libraries
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as it

def diff_Equ(N,t):      #dfferential equation of Radio activee decay
    return (-1)*(K)*(N)     # K is the decay constant and N is the number of parent atoms at time instant any

def Exact_Equ(N,t):     #solution equation of Radio activee decay
    return N0*(np.exp((-1)*(K)*(t)))    # N0 is the number of parent atoms at t=0

print("\n\nMehendi Hasan\n\nRadioactive Decay \n\nTime is in Seconds\n")


#itaking input from user
N0=int(input("Enter Number of Parent Atoms at t=0: "))
t=int(input("Enter time instant at which Remaining of Parent Atoms to be calculated: "))
K=float(input("Enter Radioactive Decay constant value: "))        # Radioactive Decay Constant

h=0.001       # Step size for Euler method

t_array=np.arange(0,t+h,h)      #initializing time array(independent Variable)
Y_differential=np.zeros(len(t_array))        #Initializing array for values of dependent variable(Euler's metod)
Y_Exact=np.zeros(len(t_array))          # #Initializing array for values of dependent variable(Solution equation)
Y_differential[0] = Y_Exact[0] = N0         #Initial values of dependent variable Y at independent variable t=0 
for i in range(len(t_array)-1):      #updating values of dependent variable
    Y_differential[i+1]=Y_differential[i] + h*(diff_Equ(Y_differential[i],t_array[i]))            #Euler's Method
    Y_Exact[i+1]=Exact_Equ(Y_Exact[i],t_array[i])                                                 # solution equation
solOdeint=it.odeint(diff_Equ,N0,t_array)                                                          # odeint solution

#ploting all the values of dependent variable with respect to independent variable
plt.subplot(3,1,1)
plt.plot(t_array,Y_differential,color="green",label="Euler's Solution")
plt.xlabel("Time (Second)")
plt.ylabel("Number of Remaining Atoms")
plt.legend()
plt.subplot(3,1,2)
plt.plot(t_array,Y_Exact,color="red",label='Exact Equation Solution')
plt.xlabel("Time (Second)")
plt.ylabel("Number of Remaining Atoms")
plt.legend()
plt.subplot(3,1,3)
plt.plot(t_array,solOdeint,color="blue",label='Odeint Solution')
plt.xlabel("Time (Second)")
plt.ylabel("Number of Remaining Atoms")
plt.legend()
plt.show()