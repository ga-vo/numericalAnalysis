import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style='darkgrid')

""" Performs the integration of a function between a and b using Trapezoidal rule
Parameters
----------
fun : function
    Function on which the integration will be performed
a : double
    Lower limit
b : double
    Upper limit
N : int
    Number of equally spaced panels
verbose: bool, default=False
    If true print each iteration
graph: bool, default=True
    If true graphically shows the integration process

Returns
-------
intgrl
    a double with the value of integral for the function between a and b
"""
def trapezoidal_integration_rule(fun, a, b, N, verbose=False, graph=True):
    dx = (b-a)/N
    x_k = a
    intgrl = 0
    if(verbose):
        print("\n Integral between {0} and {1} \n dx= {2}".format(a, b, dx))
        
    for _ in range(1, N+1):
        x_k_1 = x_k
        x_k += dx
        intgrl += fun(x_k_1) + fun(x_k)

        if(verbose):
            intgrlaux = intgrl*dx/2
            print(
                "\n x_k-1: {0}, x_k: {1}, integral: {2}".format(x_k_1, x_k, intgrlaux))
        if(graph):
            plt.fill_between([x_k_1,x_k], [fun(x_k_1), fun(x_k)], alpha=0.5)
 
    intgrl *= dx/2
    if(graph):
        x=np.linspace(a,b,300)
        f=fun(x)
        plt.plot(x,f)
        plt.show()

    return intgrl
    
