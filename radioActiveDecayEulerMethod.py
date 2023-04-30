import math
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as it

def diff_Equ(N,t):
    return (-1)*(K)*(N)

def Exact_Equ(N,t):
    return N0*(math.exp((-1)*(K)*(t)))

print("Mehendi Hasan\n\nRadioactive Decay \n\nTime is in Seconds\n")

N0=int(input("Enter Number of Parent Atoms at t=0: "))
t=int(input("Enter time instant at which Remaining of Parent Atoms to be calculated: "))
K=float(input("Enter Radioactive Decay constant value: "))        # Radioactive Decay Constant

h=0.001       # Step size for Euler method
t_array=np.arange(0,t+h,h)
Y_differential=np.zeros(len(t_array))
Y_Exact=np.zeros(len(t_array))
Y_differential[0] = Y_Exact[0] = N0
for i in range(len(t_array)-1):
    Y_differential[i+1]=Y_differential[i] + h*(diff_Equ(Y_differential[i],t_array[i]))
    Y_Exact[i+1]=Exact_Equ(Y_Exact[i],t_array[i])
solOdeint=it.odeint(diff_Equ,N0,t_array)
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