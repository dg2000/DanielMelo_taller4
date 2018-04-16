import numpy as np

import matplotlib.pyplot as plt 

from scipy.misc import imread

import sys



def fourier_inversa(salida):

    N = len(salida)

    M = len(salida[0])

    real = np.zeros([N, M   ])

    img = np.zeros([N, M   ])

    a = np.zeros([N, M ])

    for u in range(N):
        for v in range(M):
            
            for x in range(N):
                for y in range(M):

                  

                    w = 2.0*np.pi

                        #for i in range(4):

                    c= 1j*1.0

                    a[u][v]    += salida[x][y]*np.exp(w *c*(float(u)*float(x)/float(N)   + (float(v)*float(y)/float(M)))) 
                        
                        #eal[u][v][i] = real[u][v][i] + salida[x][y][i]*np.cos(w * ((float(u)*float(x)/float(N))  + (float(v)*float(y)/float(M))))
                        
                        #mg[u][v][i] = img[u][v][i] + salida[x][y][i]*np.sin(w * ((float(u)*float(x)/float(N))  + (float(v)*float(y)/float(M))))


            
            #[u][v] = ( ((real[u][v])**2.0) + ((img[u][v])**2.0) ) **0.5

    return a





def fourier(salida):

    N = len(salida)

    M = len(salida[0])

    real = np.zeros([N, M   ])

    img = np.zeros([N, M   ])

    a = np.zeros([N, M   ], dtype=complex)

    for u in range(N):
        for v in range(M):
            
            for x in range(N):
                for y in range(M):

                  
                    
                    w = 2.0*np.pi

                    c = 1j*1.0

                    a[u][v]    = a[u][v]    + salida[x][y]*np.exp(-w *c*(float(u)*float(x)/float(N)  + float(v)*float(y)/float(M)))

                        #mg[u][v][i] = img[u][v][i] + salida[x][y][i]*np.sin(-w * (float(u)*float(x)/float(N)  + float(v)*float(y)/float(M)))

          
            #[u][v] = ( (real[u][v])**2.0 + (img[u][v])**2.0 ) **0.5

    return a/(N*M)



def gauss(x, y, s):

    a = 1/(s*(2.0*np.pi)**0.5)

    b = -1/(2.0*s*s)

    return a*np.exp(b * (x + y) *(x+y))




entra= sys.argv[1]
sigma=int(sys.argv[2])

imagen = imread(entra, (1==1))



gaussiana = np.zeros([len(imagen), len(imagen[0])])

for i in range(len(imagen)):
    for j in range(len(imagen[0])):

        gaussiana[i][j]    = gauss(1.0*i, 1.0*j, 1.0*sigma )

g = fourier(gaussiana)
            
f = fourier(imagen)
b = fourier_inversa(f*g )


plt.imshow(b, cmap=plt.cm.binary)

plt.savefig("suave.png")

plt.imshow(imagen)

