import integration as int
import numpy as np
import pylab as pl

def graph(f, primitive, a, b, step):
    x = np.linspace(a, b, (b-a)/step +1)
    t = []
    m = []
    s = []
    p = []
    g = []
    for i in x:
        t.append(abs(primitive(i) - int.integration(f, "trapezium", a, i, step)))
        m.append(abs(primitive(i) - int.integration(f, "middle point", a, i, step)))
        s.append(abs(primitive(i) - int.integration(f, "simpson", a, i, step)))
        g.append(abs(primitive(i) - int.integration(f, "gauss", a, i, step)))
    pl.plot(x, t, label = "Trapezium method error")
    pl.plot(x, m, label = "Middle point method error")
    pl.plot(x, s, label = "Simpson method error")
    pl.plot(x, g, label = "Gauss method error")
    pl.legend(loc=4)
    pl.show()

def graph2(f, primitive, a, b, step):
    x = np.linspace(a, b, (b-a)/step +1)
    t = []
    m = []
    s = []
    p = []
    g = []
    for i in x:
        t.append(int.integration(f, "trapezium", a, i, step))
        m.append(int.integration(f, "middle point", a, i, step))
        s.append(int.integration(f, "simpson", a, i, step))
        g.append(int.integration(f, "gauss", a, i, step))
    pl.plot(x, t, label = "Trapezium method")
    pl.plot(x, m, label = "Middle point method")
    pl.plot(x, s, label = "Simpson method")
    pl.plot(x, g, label = "Gauss method")
    pl.legend()
    pl.show()



f = lambda x : np.cos(x)
primitive = lambda x : np.sin(x)

graph(f, primitive, 0, 5, 0.01)

graph2(f, primitive, 0, 5, 0.01)
