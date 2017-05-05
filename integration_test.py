import integration as int
import numpy as np
import pylab as pl

f = lambda x : x**2 + 2*x + 5
primitive = lambda x : (x**3)/3 + x**2 + 5*x
print(int.integration(f, "trapezium", 0, 4, 0.01))
print(int.integration(f, "middle point", 0, 4, 0.01))
print(int.integration(f, "simpson", 0, 4, 0.01))

def graph(f, primitive, a, b, step):
    x = np.linspace(a, b, (b-a)/step +1)
    t = []
    m = []
    s = []
    p = []
    for i in x:
        t.append(abs(primitive(i) - int.integration(f, "trapezium", a, i, step)))
        m.append(abs(primitive(i) - int.integration(f, "middle point", a, i, step)))
        s.append(abs(primitive(i) - int.integration(f, "simpson", a, i, step)))
    pl.plot(x, t, label = "Trapezium method error")
    pl.plot(x, m, label = "Middle point method error")
    pl.plot(x, s, label = "Simpson method error")
    pl.legend()
    pl.show()

def graph2(f, primitive, a, b, step):
    x = np.linspace(a, b, (b-a)/step +1)
    t = []
    m = []
    s = []
    p = []
    for i in x:
        t.append(int.integration(f, "trapezium", a, i, step))
        m.append(int.integration(f, "middle point", a, i, step))
        s.append(int.integration(f, "simpson", a, i, step))
    pl.plot(x, t, label = "Trapezium method")
    pl.plot(x, m, label = "Middle point method")
    pl.plot(x, s, label = "Simpson method")
    pl.legend()
    pl.show()

graph(f, primitive, 0, 5, 0.01)

graph2(f, primitive, 0, 5, 0.01)
