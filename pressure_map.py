#=================================IMPORTS======================================#

import load_data_file as ldf
import numpy as np
import matplotlib.pyplot as plt
import math as m
import integration as it

#==================================CORE========================================#

def airflow():
    print("#==============AIRFLOW===============#\n")

    (dim,ex,ey,ix,iy) = ldf.load_foil("boe103.dat")
    print("dim =\n")
    print(dim)
    print("")
    print("ex =\n")
    print(ex)
    print("")
    print("ey =\n")
    print(ey)
    print("")
    print("ix =\n")
    print(ix)
    print("")
    print("iy =\n")
    print(iy)
    print("")


    #================PLOT================#
    print("#================PLOTS================#\n")

    print("~Only the aircraft wing~\n")

    plt.plot(ex, ey, label="extrados")
    plt.plot(ix, iy, label="intrados")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.title("~Only the aircraft wing~")
    plt.legend()
    plt.ylim((-0.25,0.25))
    plt.show()

    print("~The aircraft wing with the airflow~\n")

    Ne = len(ex)
    Ni = len(ix)
    hmax = max(ey)
    hmin = min(iy)
    print("hmax =", hmax)
    print("hmin =", hmin)
    print("")

    M = int(input("How many upper airflow curves do you wish to plot ?\t"))
    tab = np.linspace(0, 1, M)

        # Upper Curves
    for l in tab:
        Y = [((1 - l)*ey[i] + l*3*hmax) for i in range(Ne)]
        plt.plot(ex, Y, c="black")

    Q = int(input("How many lower airflow curves do you wish to plot ?\t"))
    tab_2 = np.linspace(0, 1, Q)

        # Lower curves
    for l in tab_2:
        Y = [((1 - l)*iy[i] + l*3*hmin) for i in range(Ni)]
        plt.plot(ix, Y, c="black")

    plt.plot(ex, ey, label="extrados")
    plt.plot(ix, iy, label="intrados")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.title("~The aircraft wing with the airflow~")
    plt.legend()
    plt.ylim((-0.1,0.32))
    plt.show()

def f_lam(f, lam, h):
    return lambda x : (1 - lam)*f(x) + lam*3*h

def f_upper(x):
    (dim,ex,ey,ix,iy) = ldf.load_foil("boe103.dat")
    for i in range(1, int(dim[0])):
        if (x < ex[i]):
            return (ey[i-1] + ey[i])/2
    return ey[int(dim[0]) - 1]

def f_lower(x):
    (dim,ex,ey,ix,iy) = ldf.load_foil("boe103.dat")
    for i in range(1, int(dim[1])):
        if (x < ix[i]):
            return (iy[i-1] + iy[i])/2
    return iy[int(dim[1]) - 1]

def curve_length(X, Y):
    if (len(X) != len(Y)):
        print("Lengths are not compatible !")
        return
    else :
        s = 0
        for i in range(len(X) - 1):
            s += m.sqrt((Y[i+1] - Y[i])**2 + (X[i+1] - X[i])**2)
        return s

def pressure_map():
    print("#============PRESSURE_MAP============#\n")

    (dim,ex,ey,ix,iy) = ldf.load_foil("boe103.dat")
    print("dim =\n")
    print(dim)
    print("")
    print("ex =\n")
    print(ex)
    print("")
    print("ey =\n")
    print(ey)
    print("")
    print("ix =\n")
    print(ix)
    print("")
    print("iy =\n")
    print(iy)
    print("")

    print("#================PLOTS================#\n")

    print("~Pressure map~\n")

    Ne = len(ex)
    Ni = len(ix)
    hmax = max(ey)
    hmin = min(iy)
    print("hmax =", hmax)
    print("hmin =", hmin)
    print("")

    print("Black & white\n")

    #M = int(input("How many upper airflow curves do you wish to plot ?\t"))
    M = 150
    tab = np.linspace(0, 1, M)

        # Upper Curves
    Y1 = [((1 - tab[0])*ey[i] + tab[0]*3*hmax) for i in range(Ne)]
    for j in range(M):
        Ye = [((1 - tab[j])*ey[i] + tab[j]*3*hmax) for i in range(Ne)]
        #curve_l = curve_length(ex, Ye)
        curve_l = it.length(f_lam(f_upper, tab[j], hmax), "trapezium", 1, 0.02)
        print(curve_l)
        plt.fill_between(ex, Y1, Ye, color='black')
        plt.plot(ex, Ye, c=str((curve_l-1)*22))
        Y1 = Ye

    #Q = int(input("How many lower airflow curves do you wish to plot ?\t"))
    Q = 110
    tab_2 = np.linspace(0, 1, Q)

        # Lower curves
    Y2 = [((1 - tab_2[0])*iy[i] + tab_2[0]*3*hmin) for i in range(Ni)]
    for j in range(Q):
        Yi = [((1 - tab_2[j])*iy[i] + tab_2[j]*3*hmin) for i in range(Ni)]
        #curve_l = curve_length(ix, Yi)
        curve_l = it.length(f_lam(f_lower, tab_2[j], hmin), "trapezium", 1, 0.02)
        print(curve_l)
        plt.fill_between(ix, Y2, Yi, color='black')
        plt.plot(ix, Yi, c=str((curve_l-1)*22))
        Y2 = Yi

    plt.plot(ex, ey, c="black", label="extrados")
    plt.plot(ix, iy, c="black", label="intrados")
    Iy = np.zeros(len(ey))
    for i in range(int((len(iy) - 1)/2)):
        Iy[i] = iy[i]
    for i in range(int((len(iy) - 1)/2), len(iy) - 1):
        Iy[i] = iy[i] - 0.004
    Iy[len(iy) - 1] = Iy[len(iy) - 2]/2
    Iy[len(iy)] = 0
    plt.fill_between(ex, ey, Iy, color='black')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.title("~Pressure map~")
    plt.legend()
    plt.ylim((-0.1,0.32))
    plt.show()

    print("Dark & Red\n")

    #M = int(input("How many upper airflow curves do you wish to plot ?\t"))
    M = 200
    tab = np.linspace(0, 1, M)

        # Upper Curves
    Y1 = [((1 - tab[0])*ey[i] + tab[0]*3*hmax) for i in range(Ne)]
    for j in range(M):
        Ye = [((1 - tab[j])*ey[i] + tab[j]*3*hmax) for i in range(Ne)]
        curve_l = curve_length(ex, Ye)
        #print(curve_l)
        n = int((curve_l - 1)*242)
        colour = '#' + str(n) + str(n) + '0000'
        plt.fill_between(ex, Y1, Ye, color=colour)
        plt.plot(ex, Ye, c=colour)
        Y1 = Ye

    #Q = int(input("How many lower airflow curves do you wish to plot ?\t"))
    Q = 150
    tab_2 = np.linspace(0, 1, Q)

        # Lower curves
    Y2 = [((1 - tab_2[0])*iy[i] + tab_2[0]*3*hmin) for i in range(Ni)]
    for j in range(Q):
        Yi = [((1 - tab_2[j])*iy[i] + tab_2[j]*3*hmin) for i in range(Ni)]
        curve_l = curve_length(ix, Yi)
        #print(curve_l)
        n = int((curve_l - 1)*242)
        colour = '#' + str(n) + str(n) + '0000'
        plt.fill_between(ix, Y2, Yi, color=colour)
        plt.plot(ix, Yi, c=colour)
        Y2 = Yi

    plt.plot(ex, ey, c="black", label="extrados")
    plt.plot(ix, iy, c="black", label="intrados")
    Iy = np.zeros(len(ey))
    for i in range(int((len(iy) - 1)/2)):
        Iy[i] = iy[i]
    for i in range(int((len(iy) - 1)/2), len(iy) - 1):
        Iy[i] = iy[i] - 0.004
    Iy[len(iy) - 1] = Iy[len(iy) - 2]/2
    Iy[len(iy)] = 0
    plt.fill_between(ex, ey, Iy, color='black')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.title("~Pressure map~")
    plt.legend()
    plt.ylim((-0.1,0.32))
    plt.show()

airflow()
pressure_map()
