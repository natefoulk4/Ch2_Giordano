import math

def calculator(x,y,xVelocity,yVelocity,Velocity,i,timestep,choice):
    """Given the x and y positions and x and y velocities, this program returns the new x,y positions and x,y velocities, one timestep later. Taking into account drag and variable air density

    ARGS:
        x (list): List of previous x positions
        y (list): List of previous y positions
        xVelocity (list): List of previous x velocities
        yVelocity (list): List of previous y velocities
        i (int): The iterator count
        timestep (int): The timestep
        choice (int): The user's choice of projection motion models

    RETURNS:
        x (list of floats): same list of x positions, with new x position appended to the previous list
        y (list of floats): same list of y positions, with new y position appended to the previous list
        xVelocity (list of floats): same list of x velocities, with new x velocity appended to the previous list
        yVelocity (list of floats): same list of y velocities, with new y velocity appended to the previous list
    """
    gravity = 9.81
    tempAtSeaLevel = 283.15
    if choice == 1:
        dragconstant = 0
        a            = 0
    elif choice == 2:
        dragconstant = 4e-5
        a            = 0
    elif choice == 3:
        dragconstant = 4e-5
        a            = 6.5e-3
    
    xVelocity.append(float(xVelocity[i] - ((1 - ((a * y[i])/tempAtSeaLevel)) * (dragconstant * xVelocity[i] * Velocity[i] * timestep))))
    x.append(float(x[i] + xVelocity[i] * timestep))
    yVelocity.append(float(yVelocity[i] - (gravity * timestep) - ((1 - ((a * y[i])/tempAtSeaLevel)) * (dragconstant * yVelocity[i] * Velocity[i] * timestep))))
    y.append(float(y[i] + yVelocity[i] * timestep))
    Velocity.append(float(math.sqrt(xVelocity[i+1]**2 + yVelocity[i+1]**2)))

    return x,y,xVelocity,yVelocity

