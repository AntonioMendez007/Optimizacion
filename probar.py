import math
def himelblau(x1,x2):
    resultado = pow( pow(x1,2) + x2 - 11, 2 ) + pow( x1 + pow(x2,2) - 7, 2 )
    return resultado

def examen(x1,x2):
    resultado = (x1+1)**2 + (x2)**2
    return resultado

#d = himelblau(1.66293898, 4.34189622)
#print(d)
import numpy as np

import random
def x1(x_0, z_0):
    r_1 = None
    r_2 = None
    x_1 = None
    equis_1 = None
    funcion = None
    
    while True:
        r_1 = random.uniform(-0.5, 0.5) # generar los puntos aleatorios
        r_2 = random.uniform(-0.5, 0.5)
        print(f'r1: {r_1}')
        print(f'r2: {r_2}')
        x_1 = np.array([ x_0[0] + (r_1*z_0[0]), x_0[1] + (r_2*z_0[1]) ]) # calcular el x_p
        print(f'x_1: {x_1}')
        
        g1x = 26 - (x_1[0] - 5)**2 - (x_1[1]**2)
        g2x = 20 - (4 * x_1[0]) - x_1[1]
        # restricciones para ver que el punto sea feasible
        if (g1x>=0 and g2x >= 0) and (x_1[0]>=0 and x_1[1] >= 0):
            print("El punto es factible")
            equis_1 = x_1
            print(f'Punto factible: {equis_1}')
            f_x1 = himelblau(x_1[0], x_1[1])
            funcion = f_x1
            print(f'funcion: {funcion}')
            break
    return equis_1,funcion

x_0 = np.array([3,3])
z_0 = np.array([6,6])

#r, f = x1(x_0,z_0)
#print(r)

x = np.array([3.41510093, 4.54167881])
g1x = 26 - (x[0] - 5)**2 - (x[1]**2)
g2x = 20 - (4 * x[0]) - x[1]
print(g1x)
print(g2x)