# Mehendi Hasan B.SC.(H) Physics 2230248

#To Plot Radioactive Decay ODE by RK4 method, Exact solution & Inbuilt solver.

#importing libraries
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as it

def diff_Equ(N,t):      #dfferential equation of Radio activee decay
    return (-1)*(K)*(N)     # K is the decay constant and N is the number of parent atoms at time instant any

def Exact_Equ(N,t):     #solution equation of Radio activee decay
    return N0*(np.exp((-1)*(K)*(t)))    # N0 is the number of parent atoms at t=0

print("\n\n\tMehendi Hasan\n\n\t2230248\n\nRadioactive Decay \n\nTime is in Seconds\n")


#itaking input from user
N0=int(input("Enter Number of Parent Atoms at t=0: "))
t=int(input("Enter time instant at which Remaining of Parent Atoms to be calculated: "))
K=float(input("Enter Radioactive Decay constant value: "))        # Radioactive Decay Constant

h=0.001       # Step size for RK4 method

t_array=np.arange(0,t+h,h)      #initializing time array(independent Variable)
Y_differential=np.zeros(len(t_array))        #Initializing array for Y_differential of dependent variable(RK4's metod)
Y_Exact=np.zeros(len(t_array))          # #Initializing array for Y_differential of dependent variable(Solution equation)
Y_differential[0] = Y_Exact[0] = N0         #Initial Y_differential of dependent variable Y at independent variable t=0 
for i in range(len(t_array)-1):      #updating Y_differential of dependent variable
    k1=h*diff_Equ(Y_differential[i],t_array[i])
    k2=h*diff_Equ(Y_differential[i]+(k1/2),t_array[i]+(h/2))
    k3=h*diff_Equ(Y_differential[i]+(k2/2),t_array[i]+(h/2))
    k4=h*diff_Equ(Y_differential[i]+(k3),t_array[i]+(h))
    delY=(1/6)*(k1+(2*k2)+(2*k3)+k4)
    Y_differential[i+1]=Y_differential[i]+delY

Y_Exact=Exact_Equ(Y_Exact,t_array)                                                 # solution equation
solOdeint=it.odeint(diff_Equ,N0,t_array)                                                          # odeint solution

#ploting all the Y_differential of dependent variable with respect to independent variable
plt.subplot(3,1,1)
plt.plot(t_array,Y_differential,color="green",label="Number of Parent Atoms")
plt.title("RK4's Solution")
plt.grid()
plt.xlabel("Time (Second)")
plt.ylabel("No. of parent Atoms")
plt.legend()
plt.subplot(3,1,2)
plt.plot(t_array,Y_Exact,color="red",label='Number of Parent Atoms')
plt.title("Exact Equation Solution")
plt.grid()
plt.xlabel("Time (Second)")
plt.ylabel("No. of parent Atoms")
plt.legend()
plt.subplot(3,1,3)
plt.plot(t_array,solOdeint,color="blue",label='Number of Parent Atoms')
plt.title("Odeint Solution")
plt.grid()
plt.xlabel("Time (Second)")
plt.ylabel("No. of parent Atoms")
plt.legend()
plt.suptitle("Mehendi Hasan B.SC.(H) Physics 2230248\nTo Plot Radioactive Decay ODE by RK4 method, Exact solution & Inbuilt solver.")
plt.show()