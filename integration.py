import numpy as np
import pylab as pl

def length(df):
    g = lambda x : np.sqrt(1 + df(x)**2)
    return integration(g)

def integration(f, method, a, b, step):
    g = lambda t,xi,xi1 : f((1-t)/2*xi + (1+t)/2*xi1)
    x = a
    s = 0
    while(x < b):
        if(method == "trapezium"):
            I = g(-1, x, x + step) + g(1, x, x + step)
        if(method == "middle point"):
            I = 2 * g(0, x, x + step)
        if(method == "simpson"):
            I = 1/3*g(-1,x, x + step) + 4/3 * g(0, x, x + step) + 1/3*g(1, x, x + step)
        s += I * step / 2
        x += step
    return s

f = lambda x : x**2 + 2*x + 5
print(integration(f, "trapezium", 0, 4, 0.01))
print(integration(f, "middle point", 0, 4, 0.01))
print(integration(f, "simpson", 0, 4, 0.01))
print(integration(f, "simpson", 0, 2, 0.01))

def graph(f, a, b, step):
    x = np.linspace(a, b, (b-a)/step)
    t = []
    m = []
    s = []
    for i in x:
        t.append(integration(f, "trapezium", a, i, step))
        m.append(integration(f, "middle point", a, i, step))
        s.append(integration(f, "simpson", a, i, step))
    pl.plot(x, t)
    pl.plot(x, m)
    pl.plot(x, s)
    pl.show()

graph(f, 0, 0.5, 0.01)
