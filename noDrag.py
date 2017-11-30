"""
Description: Program calculates trajectory of projectile, not taking into 
account air resistance, nor the change in air pressure according to altitude.
"""

import math
import matplotlib.pyplot as plt
import csv
from matplotlib.backends.backend_pdf import PdfPages

#Prompt user for inputs
initialVelocity = input("Enter initial velocity: ")
angle = input("Enter initial angle of elevation (radians): ")
timestep = input("Enter time step: ")

#intialize other variables and lists
gravity = 9.81
x = [0]
y = [0]
xVelocity = []
yVelocity = []

#Initializing velocities in the x and y directions
xVelocity.append(float(math.cos(angle) * initialVelocity))
yVelocity.append(float(math.sin(angle) * initialVelocity))

#Define subroutines to calculate and output results
def calculate(farg):
    xVelocity.append(float(xVelocity[farg]))
    x.append(float(x[farg] + xVelocity[farg] * timestep))
    yVelocity.append(float(yVelocity[farg] - (gravity * timestep)))
    y.append(float(y[farg] + yVelocity[farg] * timestep))


#print output to csv files
f = open('output.csv', 'w')
i = 0
while y[i] >= 0:
    calculate(i)
    outputLine       = x[i], y[i]
    outputString     = str(outputLine).strip('()')+"\n"
    f.write(outputString)
    i += 1

#interpolate to solve for projectile range
r = -y[i-1]//y[i]
projectileRange = (x[i-1] + (r * x[i]))//(r + 1)
print 'Range: %.2f' % projectileRange
f.close()

#Plot path of projectile
plt.plot(x,y,)
plt.xlabel('Distance')
plt.ylabel('Altitude')
plt.title('Flight of cannonball')
plt.text(projectileRange*0.7, 0, 'Range: %.2f' % projectileRange)
plt.legend()
plt.savefig('mostrecentplot.pdf')
plt.show()


    
"""
FIXME:
Push to github
Unit testing on those modules
"""
