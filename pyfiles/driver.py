"""
Description: Program calculates trajectory of projectile, taking into 
account air resistance, but not the change in air pressure according to altitude.
"""

import math
import numpy as np
import matplotlib.pyplot as plt
import csv
import sys
from matplotlib.backends.backend_pdf import PdfPages
from mathy import *

#Prompt user for inputs
initialVelocity = float(sys.argv[1])
angle = float(sys.argv[2])
timestep = float(sys.argv[3])
choice = int(sys.argv[4])

def calculatePath(initialVelocity, angle, timestep, choice):
    """Calculates the x and y coordinates of the projectile's path.

    ARGS:
        initialVelocity (float): The velocity at which the cannon ball is shot.
        angle (float): The firing angle, relative to the horizontal.
        timestep(float): The time interval chosen for the computational solution
        choice(int): The user's choice of calculation approach:
           1: Only taking into account gravity.
           2: Taking into account gravity and drag force.
           3: Taking into account gravity, drag force, and variable air density

    RETURNS:
        x (list of floats): List of x coordinates at each timestep to be plotted
        y (list of floats): List of y coordinates at each timestep to be plotted
        projectileRange(float): The range of the cannonball
    """
    
    #initialize other variables and lists
    x = [0]
    y = [0]
    xVelocity = []
    yVelocity = []
    Velocity = []


    #Initializing velocities in the x and y directions
    xVelocity.append(float(math.cos(angle) * initialVelocity))
    yVelocity.append(float(math.sin(angle) * initialVelocity))
    Velocity.append(float(initialVelocity))


    #Calculate path and output results to csv file
    with open('output.csv', 'w') as csvfile:
        i = 0
        while y[i] >= 0:
            if choice == 1:
                x,y,xVelocity,yVelocity = noDrag(x,y,xVelocity,yVelocity,i,timestep)
            elif choice == 2:
                x,y,xVelocity,yVelocity = wDrag(x,y,xVelocity,yVelocity,Velocity,i,timestep)
            elif choice == 3:
                x,y,xVelocity,yVelocity = wDensityChange(x,y,xVelocity,yVelocity,Velocity,i,timestep)
            positionwriter = csv.writer(csvfile)
            positionwriter.writerow([x[i], y[i]])
            i += 1

    #interpolate to solve for projectile range
    r = -y[i-1]/y[i]
    projectileRange = (x[i-1] + (r * x[i]))/(r + 1)
    print 'Range: %.2f' % projectileRange
    
    return x, y, projectileRange

def plot(initialVelocity, angle, timestep, choice):
    """ Plots a single projectile path based on user inputs.
    ARGS:
        initialVelocity (float): The velocity at which the cannon ball is shot.
        angle (float): The firing angle, relative to the horizontal.
        timestep(float): The time interval chosen for the computational solution
        choice(int): The user's choice of calculation approach:
           1: Only taking into account gravity.
           2: Taking into account gravity and drag force.
           3: Taking into account gravity, drag force, and variable air density
    RETURNS: None
    """

    x, y, projectileRange  = calculatePath(initialVelocity, angle, timestep, choice)
    
    #Plot path of projectile
    plt.plot(x,y)
    plt.xlabel('Distance')
    plt.ylabel('Altitude')
    plt.ylim(ymin=0)
    plt.title('Flight of cannonball')
    plt.text( projectileRange*0.7, 250, 'Range: %.2f' % projectileRange)
    plt.legend()
    plt.savefig('mostrecentplot.pdf')
    plt.show()

def plotMethods(initialVelocity, angle, timestep):
    """ Plots 3 different paths using user given information using our 3 different methods of calculation
    ARGS: 
        initialVelocity (float): The velocity at which the cannon ball is shot.
        angle (float): The firing angle, relative to the horizontal.
        timestep(float): The time interval chosen for the computational solution
    RETURNS: None
    """

    #unpack paths from the three different methods of calculation
    x1, y1, projectileRange1  = calculatePath(initialVelocity, angle, timestep, 1)
    x2, y2, projectileRange2  = calculatePath(initialVelocity, angle, timestep, 2)
    x3, y3, projectileRange3  = calculatePath(initialVelocity, angle, timestep, 3)
    
    #Plot path of projectile
    #plt.plot(x1,y1, label = "Without drag")
    plt.plot(x2,y2, label = "With drag")
    plt.plot(x3,y3, label = "With variable air density")
    plt.xlabel('Distance')
    plt.ylabel('Altitude')
    plt.ylim(ymin=0)
    plt.title('Flight of cannonball')
    plt.legend()
    plt.savefig('mostrecentplot.pdf')
    plt.show()

def plotTimeSteps(initialVelocity, angle):
    """ Plots 3 different paths of a projectile using 3 different timesteps of 5, 3, and 0.5
    ARGS: 
        initialVelocity (float): The velocity at which the cannon ball is shot.
        angle (float): The firing angle, relative to the horizontal.
    RETURNS: None
    """
    
    #pull path coordinates from calculate subroutine for different timesteps
    x1, y1, projectileRange1  = calculatePath(initialVelocity, angle, 5, 1)
    x2, y2, projectileRange2  = calculatePath(initialVelocity, angle, 3, 1)
    x3, y3, projectileRange3  = calculatePath(initialVelocity, angle, 0.5, 1)
    
    # analytic solution
    gravity = 9.81
    xVelocity = math.cos(angle) * initialVelocity
    yVelocity = math.sin(angle) * initialVelocity
    x = np.arange(0,projectileRange1,1)
    y = eval("((-0.5)*gravity) * ((x)/xVelocity)**2 + (yVelocity/xVelocity)*x")
    
    #Plot path of projectile
    plt.plot(x1,y1, label = "deltaT = 5")
    plt.plot(x2,y2, label = "deltaT = 3")
    plt.plot(x3,y3, label = "deltaT = 0.5")
    plt.plot(x,y, '--', label = "analytic")
    plt.xlabel('Distance')
    plt.ylabel('Altitude')
    plt.ylim(ymin=0)
    plt.title('Flight of cannonball')
    plt.legend()
    plt.savefig('mostrecentplot.pdf')
    plt.show()


plot(initialVelocity, angle, timestep, choice)
#plotMethods(initialVelocity, angle, timestep)
#plotTimeSteps(initialVelocity, angle)

 
