#=================================IMPORTS======================================#

import load_data_file as ldf
import numpy as np
import matplotlib.pyplot as plt

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

    N = dim[0] # Number of values to compute
    X = np.linspace(0, 1, N)
    hmax = max(ey)
    print(X)

airflow()
