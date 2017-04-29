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
    """
    plt.plot(ex, ey)
    plt.plot(ix, iy)
    plt.show()
    """
airflow()
