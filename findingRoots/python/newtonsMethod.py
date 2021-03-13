__author__ = "ga-vo"
__license__ = "GPL-3.0"
__version__ = "1.0.1"

import numpy as np
import matplotlib.pyplot as plt

""" Performs the newton's method for a function with initial point at p0
Parameters
----------
fun : function
    Function on which the root will be find
der : function
    Derivate of function fun
p0 : double
    Initial point to perform the root finding
iter : int, default=100
    Max number of iterations
verbose: bool, default=False
    If true print each iteration
graph: bool, default=True
    If true graphically shows the process

Returns
-------
p1
    a double with the value of root for function fun
"""
def newtonsMethod(fun, der, p0, iter=50, verbose=False, graph=True):
    pn=p0
    p=[p0]
    for _ in range(iter):
        if(not der(pn) == 0):
            pn -= fun(pn)/der(pn)
            if(verbose):
                print("{:5} | p_n: {:5.5} | fun(p_n): {:5.5} | der(p_n): {:5.5}".format(_,pn,fun(pn),der(pn)))

            if(graph):
                p.append(pn)
                
        else:
            print("Error: Derivate of {:10.10} equals 0".format(pn))
            break
    
    if(graph):
        p=np.array(p)
        x=np.linspace(min(p),max(p),len(p)*100)
        plt.plot(x,fun(x), 'b-')
        plt.plot(p,fun(p), 'g:+')
        plt.plot(pn,fun(pn),'rx')
        plt.legend(labels=['Function', 'X_n', 'Root'])
        plt.show()
    return pn
