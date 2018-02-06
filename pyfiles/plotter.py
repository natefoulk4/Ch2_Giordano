import matplotlib.pyplot as plt

def plot(x,y,projectileRange):
    """ Plots a single projectile path based on user inputs.
    ARGS:
       x (list of floats) : list of x positions at every timestep for plotting
       y (list of floats) : list of y positions at every timestep for plotting
       projectileRange (float) : The final range of the projectile
    RETURNS: None
    """
    
    #plot path of projectile
    plt.plot(x,y)
    plt.xlabel('Distance')
    plt.ylabel('Altitude')
    plt.ylim(ymin=0)
    plt.title('Flight of cannonball')
    plt.text( projectileRange*0.7, 250, 'Range: %.2f' % projectileRange)
    plt.legend()
    plt.savefig('mostrecentplot.pdf')
    plt.show()
def plotModels(x,y):
    """ Plots 3 different paths using user given information using our 3 different methods of calculation
    ARGS: 
        x (list of lists): A list of lists of x positions for 3 different paths
        y (list of lists): A list of lists of y positions for 3 different paths
    RETURNS: None
    """
    
    #Plot path of projectile
    plt.plot(x[0],y[0], label = "Without drag")
    plt.plot(x[1],y[1], label = "With drag")
    plt.plot(x[2],y[2], label = "With variable air density")
    plt.xlabel('Distance')
    plt.ylabel('Altitude')
    plt.ylim(ymin=0)
    plt.title('Flight of cannonball')
    plt.legend()
    plt.savefig('mostrecentplot.pdf')
    plt.show()

def plotTimeSteps(x,y):
    """ Plots 3 different paths of a projectile using 3 different timesteps of 5, 3, and 0.5
    ARGS: 
        initialVelocity (float): The velocity at which the cannon ball is shot.
        angle (float): The firing angle, relative to the horizontal.
    RETURNS: None
    """
    
    #Plot path of projectile
    plt.plot(x[0],y[0], label = "deltaT = 5")
    plt.plot(x[1],y[1], label = "deltaT = 3")
    plt.plot(x[2],y[2], label = "deltaT = 0.5")
    plt.plot(x[3],y[3], '--', label = "analytic")
    plt.xlabel('Distance')
    plt.ylabel('Altitude')
    plt.ylim(ymin=0)
    plt.title('Flight of cannonball')
    plt.legend()
    plt.savefig('mostrecentplot.pdf')
    plt.show()

