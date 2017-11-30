#Calculating trajectory of projectile
import math

#Prompt user for inputs
initialVelocity = input("Enter initial velocity: ")
angle = input("Enter initial angle of elevation (radians): ")
mass = input("Enter mass of the object: ")
tempAtSeaLevel = input("Enter temperature (Kelvin): ")
timestep = input("Enter time step: ")

#Declare constants
dragconstant = 4e-5
gravity = 9.8

#initialize arrays
x = range(100)
y = range(100)

xVelocity = range(100)
yVelocity = range(100)

xVelocity[0] = math.cos(angle) * initialVelocity
yVelocity[0] = math.sin(angle) * initialVelocity

f = open('output.csv', 'w')
for i in range(99):
    xVelocity[i + 1] = xVelocity[i] - (((dragconstant * initialVelocity *xVelocity[i])/mass) * (1 - ((6.5e-3 * y[i]) / tempAtSeaLevel)))
    x[i + 1] = x[i] + xVelocity[i] * timestep
    yVelocity[i + 1] = yVelocity[i] - (gravity * timestep) - (((dragconstant * initialVelocity * yVelocity[i])/mass) * (1 - ((6.5e-3 * y[i]) / tempAtSeaLevel)))
    y[i + 1] = y[i] + yVelocity[i] * timestep
    outputLine = x[i], y[i]
    outputString = str(outputLine).strip('()')+"\n"
    f.write(outputString)
    if y[i] * y[i+1] < 0:
        print 'Range: ', x[i]
f.close()

import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('output.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))

plt.plot(x,y,)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Flight of cannonball')
plt.legend()
plt.show()

 
