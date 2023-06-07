#y = a**x
import numpy as np
import matplotlib.pyplot as plt

n=int(input("Enter numbe data points: "))
a=np.zeros((n,4))
X=[]
Y=[]
X2=[]
XY=[]
for i in range (n):
    a[i][0]=float(input("Enter value of x["+str(i)+"]="))
    X.append(a[i][0])
    a[i][1]=float(input("Enter value of y["+str(i)+"]="))
    Y.append(a[i][1])
    a[i][2]=(a[i][0])**2
    X2.append(a[i][2])
    a[i][3]=(a[i][0])*(a[i][1])
    XY.append(a[i][3])
print("X\tY\tX*X\tX*Y")
for i in a:
    for j in i:
        print(j,end="\t")
    print("\n")
sumX=sum(X)
sumY=sum(Y)
sumXY=sum(XY)
sumX2=sum(X2)
A=np.zeros((2,2))
B=np.zeros((2,1))
A[0][0]=n
A[0][1]=sumX
A[1][0]=sumX
A[1][1]=sumX2
B[0][0]=sumY
B[1][0]=sumXY
coff=np.linalg.solve(A,B)
c=coff[0][0]
m=coff[1][0]
equ="Y = {}*X + {}".format(m,c)
print(equ)

g=int(input("Enter number of grid points: "))
xMin=min(X)
xMax=max(X)
x_points=np.linspace(xMin,xMax,g)
y_points=m*x_points+c
plt.plot(X,Y,label="original points")
plt.plot(x_points,y_points,'g--',label="fitted curve")
plt.legend()
plt.show()