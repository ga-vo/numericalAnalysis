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
def composite_3_8_simpson_integration_rule(fun, a, b, N, verbose=False, graph=True):
    while(N % 3 !=0):
         N+=1 

    h = (b-a)/N 
    intgrl = fun(a)
    if(verbose):
        print("\n Integral between {0} and {1} \n dx= {2}".format(a, b, h))
        
    for k in range(1, N):
        if(k%3 != 3):
            x_k= a + k*h
            intgrl += 3*fun(x_k)
            if(verbose):
                intgrlaux = intgrl*(3*h/8)
                print(
                    "\n x_k: {0}, integral: {1}".format(x_k, intgrlaux))
            if(graph):
                plt.plot([x_k, x_k+h], [fun(x_k), fun(x_k+h)], 'r.')
                plt.fill_between([x_k, x_k+h], [fun(x_k), fun(x_k+h)], alpha=0.5)
    
    for k in range(1,int(N/3)):
        x_3k=a+3*k*h
        intgrl += 2*fun(x_3k)

        if(verbose):
                intgrlaux = intgrl*(3*h/8)
                print(
                    "\n x_k: {0}, integral: {1}".format(x_k, intgrlaux))
        if(graph):
                plt.plot([x_k, x_k+h], [fun(x_k), fun(x_k+h)], 'r.')
                plt.fill_between([x_k, x_k+h], [fun(x_k), fun(x_k+h)], alpha=0.5)\
    
    intgrl+=fun(b)
    intgrl *= 3*h/8

    if(graph):
        x=np.linspace(a,b,300)
        f=fun(x)
        plt.plot(x,f)
        plt.show()

    return intgrl

