import random
import math
import cmath

import numpy as np

import matplotlib.pyplot as plt


pi2 = cmath.pi * 2.0
def DFT(fnList):
    N = len(fnList)
    FmList = []
    for m in range(N):
        Fm = 0.0
        for n in range(N):
            Fm += fnList[n] * cmath.exp(- 1j * pi2 * m * n / N)
        FmList.append(Fm / N)
    return FmList
        
x = np.linspace(0.0, 2.0*np.pi, 100)

y = np.sin(x) 

res = DFT(y)

plt.scatter(x, res)

plt.plot(x, y)

plt.show()
