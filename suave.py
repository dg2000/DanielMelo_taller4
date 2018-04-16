import numpy as np

import matplotlib.pyplot as plt 

from scipy.misc import imread

import sys


def fourier_inversa(salida):

    N = len(salida)

    M = len(salida[0])

    real = np.zeros([N, M])

    img = np.zeros([N, M])

    a = np.zeros([N, M])

    for u in range(N):
        for v in range(M):
            
            for x in range(N):
                for y in range(M):
                    
                    w = 2.0*np.pi

                    real[u][v] = real[u][v] + salida[x][y]*np.cos(w * (u*x/N  + v*y/M))

                    img[u][v] = img[u][v] + salida[x][y]*np.sin(w * (u*x/N  + v*y/M)/N)


            a[u][v] = ( (real[u][v])**2.0 + (img[u][v])**2.0 )**0.5

    return a


def fourier(salida):

    N = len(salida)

    M = len(salida[0])

    real = np.zeros([N, M])

    img = np.zeros([N, M])

    a = np.zeros([N, M])

    for u in range(N):
        for v in range(M):
            
            for x in range(N):
                for y in range(M):
                    
                    w = 2.0*np.pi

                    real[u][v] = real[u][v] + salida[x][y]*np.cos(-w * (u*x/N  + v*y/M))

                    img[u][v] = img[u][v] + salida[x][y]*np.sin(-w * (u*x/N  + v*y/M))


            a[u][v] = ( (real[u][v]/(M*N))**2.0 + (img[u][v]/(M*N))**2.0 )**0.5

    return a




print A[0][0]

entra= sys.argv[1]
N=int(sys.argv[2])

imagen = imread(entra, (1==1))

print len(imagen), len(imagen[0])
f = fourier(imagen)
b = fourier_inversa( f )

plt.imshow(b)

plt.show()

plt.figure()
plt.imshow(imagen)
plt.show()



