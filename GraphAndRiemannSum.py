# -*- coding: utf-8 -*-
"""
This module contains the function plotRiemannGraph(...)
This function can:
        -plot a given function
        -plot Riemann bars onto the graph of the function
        -return the total area of the Riemann bars
This functon is not foolproof and if nonsensical or contradictory inputs
are given, the results are not valid and the program my terminate abrouptly.
"""

import numpy as np
import matplotlib.pyplot as plt

def plotRiemannGraph(f=lambda x:3*x+4, xGraphLimits=(0,5), yGraphLimits=None,
                     GraphPoints=100, Bars=False, xLabel='x', yLabel='y',
                     Left=True, BarsLimits=None, nBars=0):
    
    """
    Parameters
    f: The function to be graphed. Defaults to f(x)=3x+4
    xGraphLimits: The left and right limits of the graph. Defaults to x=0
                    and x=5
    yGraphLimits: The upper and lower limits of the graph. Defaults to None,
                    in which case the limits are calculated from the function
                    and the left and right limits
    GraphPoints: The number of points to be drawn. Defaults to 100
    Bars: Bars will be drawn only if set to True. Defaults to False
    xLabel: Text. Defaults to 'x'
    yLabel: Text. Defaults to 'y'
    Left: Determines if bars will be "left edge" or "Right edge". Defaults
            to True (i.e. "Left edge")
    BarsLimits: Specifies the interval in which bars will be placed. Defaults
                to None
    nBars: Specifies the number of bars to be drawn. Defaults to 0
        
    """
    
    
    #Get actual points to be ploted

    xValsGraph=np.linspace(xGraphLimits[0], xGraphLimits[1], GraphPoints)
    yValsGraph=f(xValsGraph)
    
    #Define y-limits of plot
    if yGraphLimits==None:
        yU=max(yValsGraph)+0.2*(max(yValsGraph)-min(yValsGraph))
        yL=min(yValsGraph)-0.2*(max(yValsGraph)-min(yValsGraph))
    else:
        yU=yGraphLimits[1]
        yL=yGraphLimits[0]
    
    plt.figure()
    plt.axis([xGraphLimits[0], xGraphLimits[1], yL, yU])
    if yL !=0: plt.axhline(y=0, color='k', linestyle='--')
    plt.plot(xValsGraph, yValsGraph, 'b')#Color of plot is not an option
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    
    BarsArea=None
    
    if Bars:
        #Get x-coordinates of all intervals
        xValsBars=np.linspace(BarsLimits[0], BarsLimits[1],nBars+1)
        yValsBars=f(xValsBars)

        
        #Filter values depending if left edge or right edge
        if Left:
            barWidth=xValsBars[1]-xValsBars[0]
            xValsBars=xValsBars[:-1]
            yValsBars=yValsBars[:-1]
        else:
            barWidth=xValsBars[0]-xValsBars[1]
            xValsBars=xValsBars[1:]
            yValsBars=yValsBars[1:]

        plt.bar(xValsBars, yValsBars, barWidth, alpha=0.2, align='edge',
                edgecolor='b')
        
        BarsArea=sum(yValsBars*abs(barWidth))
    
    plt.show()
    
    return BarsArea