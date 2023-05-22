import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1/(1+(x**2))

#user inputs
upperLimit=float(input("Enter Upper Limit: "))
lowerLimit=float(input("Enter Lower Limit: ")) 
n=int(input("Enter Number of Intervals: "))      # No. of intervals
h=(upperLimit-lowerLimit)/n         #step size

xPoints = np.arange(lowerLimit,upperLimit+(h/2),h)
yPoints =np.array(1/(1+(xPoints**2)))

integrationFxDx = h*(((yPoints[0]+yPoints[-1])/2)+(np.sum(yPoints)-(yPoints[0]+yPoints[-1])))
print(integrationFxDx)

plt.plot(xPoints,yPoints,label="F(x) using Trapezoidal Rule")
plt.legend()
plt.show()