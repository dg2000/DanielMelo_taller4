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




entra= sys.argv[1]
lim=str(sys.argv[2])

imagen = imread(entra, (1==1))

f = fourier(imagen)

if(lim == "alto"):

    mucho = 13.0

    for i in range(len(f)):

        for k in range(len(f[0])):

            a = i**2.0

            b = k**2.0

            if( (a+b)**0.5 > mucho):

                f[i][k] = 0.0

    plt.imshow(fourier_inversa(f), cmap=plt.cm.binary)

    plt.savefig("altas.png")

else:

    mucho = 5.0

    for i in range(len(f)):

        for k in range(len(f[0])):

            a = i**2.0

            b = k**2.0

            if( (a+b)**0.5 < mucho):

                f[i][k] = 0.0

    plt.imshow(fourier_inversa(f), cmap=plt.cm.binary)

    plt.savefig("bajas.png")
                
    


