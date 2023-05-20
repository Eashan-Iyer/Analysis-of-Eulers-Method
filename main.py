import matplotlib.pyplot as plt
import numpy as np
import math

def yprime(x, y):
  #input whatever function dy/dx is equal to 
  return math.exp(3*x)
def yactual(x):
  #you need to solve for y if you want to compare to yprime euler approximation
  return math.exp(3*x)/3

#input a value for delta x
delx= 0.001

#We need to input the bounds of the interval that we plot
#Constant of integration will need to be provided
#We start plotting from the lower bound of the interval(There is nothing wrong with starting from the upper bound and going backwards)
xmin=0
xmax=4
C=1
x=np.arange(xmin, xmax, delx)
y=[C]
for element in x:
  yhat=(y[-1])+yprime(element, y[-1])*delx
  y.append(yhat)
y.pop(-1)

#generate values of yactual
yactualvals=[]
for element in x:
  realy=yactual(element)
  yactualvals.append(realy)
  
  #Find Local Error
LE = abs(yactualvals[1]-y[1])
print(LE)

#Find Global Error
GE = abs(yactualvals[-1] - y[-1])
print(GE)

#approximated is blue
plt.plot(x, y, linestyle = "-", label = "Approximated function")
plt.title('Euler approximation of y')
plt.xlabel('x_axis')
plt.ylabel('yhat')
#actual is yellow(This plots with the same delta x as the approximation)
plt.plot(x, yactualvals, label = "Actual Function")
plt.legend()
plt.xlabel('x_axis')
plt.ylabel('yactual')
plt.show()
