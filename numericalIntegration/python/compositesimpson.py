import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style='darkgrid')

""" Performs the integration of a function between a and b using Composite Simpson's 3/8 rule
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
def composite_simpson_integration_rule(fun, a, b, N, verbose=False, graph=True):
    if(N % 2 !=0):
        N+=1
        
    h = (b-a)/N 
    intgrl = 0
    if(verbose):
        print("\n Integral between {0} and {1} \n dx= {2}".format(a, b, h))
        
    for k in range(1, N/2):
        x_2k_2 = (a+(((2*k)-2)*h))
        x_2k_1 = (a+(((2*k)-1)*h))
        x_2k = (a+((2*k)*h))
        intgrl += fun(x_2k_2)+(4*fun(x_2k_1))+(fun(x_2k))

        if(verbose):
            intgrlaux = intgrl*h/3
            print(
                "\n x_2k-2: {0}, x_2k-1: {1}, x_2k : {2}, integral: {3}".format(x_2k_2,x_2k_1, x_2k, intgrlaux))
        if(graph):
            plt.plot([x_2k_2,x_2k_1,x_2k], [fun(x_2k_2),fun(x_2k_1),fun(x_2k)], 'r.')
            plt.fill_between([x_2k_2,x_2k_1,x_2k], [fun(x_2k_2),fun(x_2k_1),fun(x_2k)], alpha=0.5)

    intgrl *= h/3
    if(graph):
        x=np.linspace(a,b,300)
        f=fun(x)
        plt.plot(x,f)
        plt.show()

    return intgrl
