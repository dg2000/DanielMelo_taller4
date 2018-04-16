import numpy as np

import matplotlib.pyplot as plt 

from scipy.misc import imread

import sys



def fourier_inversa(salida):

    N = len(salida)

    M = len(salida[0])

    real = np.zeros([N, M, 4])

    img = np.zeros([N, M, 4])

    a = np.zeros([N, M, 4])

    for u in range(N):
        for v in range(M):
            
            for x in range(N):
                for y in range(M):

                    for i in range(4):
                    
                        w = 2.0*np.pi

                        real[u][v][i] = real[u][v][i] + salida[x][y][i]*np.cos(w * (u*x/N  + v*y/M))

                        img[u][v][i] = img[u][v][i] + salida[x][y][i]*np.sin(w * (u*x/N  + v*y/M))


            for z in range(4):
                a[u][v][z] = ( (real[u][v][z]/(M*N))**2.0 + (img[u][v][z]/(M*N))**2.0 )**0.5

    return a





def fourier(salida):

    N = len(salida)

    M = len(salida[0])

    real = np.zeros([N, M, 4])

    img = np.zeros([N, M, 4])

    a = np.zeros([N, M, 4])

    for u in range(N):
        for v in range(M):
            
            for x in range(N):
                for y in range(M):

                    for i in range(4):
                    
                        w = 2.0*np.pi

                        real[u][v][i] = real[u][v][i] + salida[x][y][i]*np.cos(-w * (u*x/N  + v*y/M))

                        img[u][v][i] = img[u][v][i] + salida[x][y][i]*np.sin(-w * (u*x/N  + v*y/M))

            for z in range(4):
                a[u][v][z] = ( (real[u][v][z]/(M*N))**2.0 + (img[u][v][z]/(M*N))**2.0 )**0.5

    return a






entra= sys.argv[1]
N=int(sys.argv[2])

imagen = imread(entra)

print imagen

print len(imagen), len(imagen[0]), len(imagen[0][0])
f = fourier(imagen)
b = fourier_inversa( f )

print b

plt.imshow(b)

plt.show()

plt.figure()
plt.imshow(imagen)
plt.show()



