"""
Description: Program calculates trajectory of projectile, taking into 
account air resistance, but not the change in air pressure according to altitude.
"""

import numpy as np
import sys
from matplotlib.backends.backend_pdf import PdfPages
from plotter import *
from looper import *

#pull inputs from command line
initialVelocity = float(sys.argv[1])
angle = float(sys.argv[2])
timestep = float(sys.argv[3])
choice = float(sys.argv[4])




if choice < 4:
    x,y,projectileRange = calculatePath(initialVelocity, angle, timestep, choice)
    plot(x,y,projectileRange)
elif choice == 4:
    #unpack paths from the three different methods of calculation
    x1, y1, projectileRange1  = calculatePath(initialVelocity, angle, timestep, 1)
    x2, y2, projectileRange2  = calculatePath(initialVelocity, angle, timestep, 2)
    x3, y3, projectileRange3  = calculatePath(initialVelocity, angle, timestep, 3)
    plotModels([x1,x2,x3],[y1,y2,y3])
elif choice == 5:
    #pull path coordinates from calculate subroutine for different timesteps
    x1, y1, projectileRange1  = calculatePath(initialVelocity, angle, 5, 1)
    x2, y2, projectileRange2  = calculatePath(initialVelocity, angle, 3, 1)
    x3, y3, projectileRange3  = calculatePath(initialVelocity, angle, 0.5, 1)
    
    # analytic solution
    gravity = 9.81
    xVelocity = math.cos(angle) * initialVelocity
    yVelocity = math.sin(angle) * initialVelocity
    x4 = np.arange(0,projectileRange1,1)
    y4 = eval("((-0.5)*gravity) * ((x4)/xVelocity)**2 + (yVelocity/xVelocity)*x4")
    
    plotTimeSteps([x1,x2,x3,x4],[y1,y2,y3,y4])


 
