import numpy as np
import pylab as pl
from scipy.special import legendre

def length(f, method, T, step):
    df = lambda x : (f(x + step) - f(x))/step
    g = lambda x : np.sqrt(1 + df(x)**2)
    return integration(g, method, T, step)

def gauss(f, r):
    Pr = legendre(r)
    ##dPr =
    roots = poly1D(Pr).r
    s = 0
    for i in range(r):
        s = 0
    ##    s += (2/((1-roots[i]**2)*dPr(root[i])**2))* f(roots[i])
    return s

def integration(f, method, a, b, step):
    g = lambda t,xi,xi1 : f((1-t)*xi/2 + (1+t)*xi1/2)
    x = a
    s = 0
    while(x < b):
        if(method == "trapezium"):
            I = g(-1, x, x + step) + g(1, x, x + step)
        if(method == "middle point"):
            I = 2 * g(0, x, x + step)
        if(method == "simpson"):
            I = g(-1,x, x + step)/3 + 4* g(0, x, x + step)/3 + g(1, x, x + step)/3
        if(method == "gauss"):
            I = gauss(f, r)
        s += I * step / 2
        x += step
    return s
