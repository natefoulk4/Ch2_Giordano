import math
from mathy import *
import csv

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
           4: Plotting the three different models above on one graph
           5: Plotting various timesteps in comparison to the analytic solution

    RETURNS:
        x (list of floats): List of x coordinates at each timestep to be plotted
        y (list of floats): List of y coordinates at each timestep to be plotted
        projectileRange(float): The range of the cannonball
    """
    
    #initialize lists and convert angle to radians
    x = [0]
    y = [0]
    xVelocity = []
    yVelocity = []
    Velocity = []
    angle = angle * (3.14159265358979323/180)


    #Initializing velocities in the x and y directions
    xVelocity.append(float(math.cos(angle) * initialVelocity))
    yVelocity.append(float(math.sin(angle) * initialVelocity))
    Velocity.append(float(initialVelocity))


    #Calculate path and output results to csv file
    with open('output.csv', 'w') as csvfile:
        i = 0
        while y[i] >= 0:
            x,y,xVelocity,yVelocity = calculator(x,y,xVelocity,yVelocity,Velocity,i,timestep, choice)
            positionwriter = csv.writer(csvfile)
            positionwriter.writerow([x[i], y[i]])
            i += 1

    #interpolate to solve for projectile range
    r = -y[i-1]/y[i]
    projectileRange = (x[i-1] + (r * x[i]))/(r + 1)
    print 'Range: %.2f' % projectileRange
    
    return x, y, projectileRange
