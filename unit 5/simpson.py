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

if n%2==0:
    sumEvenPosition = 0
    for i in range(len(yPoints)-1):
        if i==0 or i==(len(yPoints)-1):
            continue
        elif i%2==0:
            sumEvenPosition+=yPoints[i]
    integrationFxDx = (h/3)*(yPoints[0]+yPoints[-1]+ (4*(sum(yPoints)-(sumEvenPosition + (yPoints[0]+yPoints[-1])))) +2*(sumEvenPosition))

elif n%3==0:
    sumMult3Position = 0
    for i in range(len(yPoints)-1):
        if i==0 or i==(len(yPoints)-1):
            continue
        elif i%3==0:
            sumMult3Position+=yPoints[i]
    integrationFxDx = ((3*h)/8)*(yPoints[0]+yPoints[-1]+ (3*(sum(yPoints)-(sumMult3Position + (yPoints[0]+yPoints[-1])))) +2*(sumMult3Position))
print(integrationFxDx)

plt.plot(xPoints,yPoints,label="F(x) using Simpson's Rule")
plt.legend()
plt.show()