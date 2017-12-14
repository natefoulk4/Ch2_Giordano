
""" Tests mathy.py.
"""

import pytest

def test_noDrag():
    """Tests the no Drag equations
    """
    from pyfiles.mathy import noDrag

    x,y,xVelocity,yVelocity  = noDrag([0],[0],[10],[10],0,1)
    assert x         == [0,10]
    assert y         == [0,10]
    assert xVelocity == [10,10]
    assert yVelocity == [10,0.19]

def test_wDrag():
    """Tests the with drag equations
    """
    from pyfiles.mathy import wDrag

    x,y,xVelocity,yVelocity  = wDrag([0],[0],[10],[10],[14.1421356],0,1)
    assert x         == [0,10]
    assert y         == [0,10]
    assert xVelocity == [10,9.99434]
    assert yVelocity == [10,0.1843]

def test_wDenstityChange1():
    """Tests the equations, taking into account variable air density, from the firing angle
   """
    from pyfiles.mathy import wDensityChange

    x,y,xVelocity,yVelocity  = wDensityChange([0],[0],[10],[10],[14.1421356],0,1)
    assert x         == [0,10]
    assert y         == [0,10]
    assert xVelocity == [10,9.99434]
    assert yVelocity == [10,0.1843]

def test_wDenstityChange2():
    """Tests the equations, taking into account variable air density, mid flight
    """
    from pyfiles.mathy import wDensityChange

    x,y,xVelocity,yVelocity  = wDensityChange([1000],[1000],[100],[70],[122.066],0,1)
    assert x         == [1000,1100]
    assert y         == [1000,1070]
    assert xVelocity == [100,99.5229]
    assert yVelocity == [70,59.8561]



    
