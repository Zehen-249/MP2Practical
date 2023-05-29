import matplotlib.pyplot as plt

def f(x):
    return x**3
def fDash(x):
    return 3*(x**2)

x=[1]
y=[f(1)]
x.append(x[0]-(f(x[0])/fDash(x[0])))
y.append(f(x[-1]))
i=1
while(x[i]!=x[i-1]):
    if fDash(x[i])==0:
        x.append(0)
        y.append(0)
        i+=1
        continue
    x.append(x[i]-(f(x[i])/fDash(x[i])))
    y.append(f(x[i+1]))
    i+=1
root=x[-1]

plt.plot(x,y)
plt.plot(x[-1],f(x[-1]),marker="o")
plt.show()