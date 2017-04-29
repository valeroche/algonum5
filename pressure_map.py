#=================================IMPORTS======================================#

import load_data_file as ldf
import numpy as np
import matplotlib.pyplot as plt
import math as m

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

    M = int(input("How many upper airflow curves do you wish to plot ?\t"))
    tab = np.linspace(0, 1, M)

        # Upper Curves
    for l in tab:
        Y = [((1 - l)*ey[i] + l*3*hmax) for i in range(Ne)]
        curve_l = curve_length(ex, Y)
        plt.plot(ex, Y, c=str((curve_l-1)*22))

    Q = int(input("How many lower airflow curves do you wish to plot ?\t"))
    tab_2 = np.linspace(0, 1, Q)

        # Lower curves
    for l in tab_2:
        Y = [((1 - l)*iy[i] + l*3*hmin) for i in range(Ni)]
        curve_l = curve_length(ix, Y)
        plt.plot(ix, Y, c=str((curve_l-1)*22))

    plt.plot(ex, ey, c="black", label="extrados")
    plt.plot(ix, iy, c="black", label="intrados")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.title("~Pressure map~")
    plt.legend()
    plt.ylim((-0.1,0.32))
    plt.show()

#airflow()
pressure_map()
