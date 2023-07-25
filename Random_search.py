import numpy as np
import math
import random

def himelblau(x1,x2):
    resultado = pow( pow(x1,2) + x2 - 11, 2 ) + pow( x1 + pow(x2,2) - 7, 2 )
    return resultado
# función para obtener los puntos factibles
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

def aleatorio(x_0,z_0):
    # Paso 1: 
    P = 3
    Q = 10
    e = 0.25
    pe = 1
    qu = 1
    iteraciones = 0
    repetir = True
    minimo_funcion_siguiente = None # almacenar el valor de la siguiente iteración
    while(repetir):
        iteraciones = iteraciones + 1
        print("--------------------------------------")
        print(f'Iteracion: {iteraciones}')
        e_x_1 = [] # arreglo para almacenar los puntos x_p
        funcion = [] # vector para almacenar los f_xp
        minimo_funcion = None
        # ciclo for dado que p = 3 = P, es decir, se va a repetir 3 veces
        for i in range(3):
            x_1,f_x1 = x1(x_0,z_0) 
            e_x_1.append(x_1) # se van aregando los x_p al vector
            funcion.append(f_x1) # se van agregando los f_xp al vector
        print(f'funciones: {funcion}')

        minimo_funcion = np.min(funcion) # se obtiene el minimo de todos los f_xp
        index_min = funcion.index(np.min(funcion))
        p_min = e_x_1[index_min] # se obtiene el indice del punto x_p al cual el f_xp pertecenece
        print(f'minimo de la funcion: {minimo_funcion}')
        print(f'mejor punto : {p_min}')
     
        # Comparar el mínimo de la iteración actual con el mínimo de la siguiente iteración
        if minimo_funcion_siguiente is not None and minimo_funcion is not None:
            if minimo_funcion < minimo_funcion_siguiente:
                print(f'El minimo de la funcion anterior: {minimo_funcion}')
            else:
                print(f'minimo de la iteracion siguiente: {minimo_funcion_siguiente}')
        # Paso 4
        z_1 = np.array([(1-e)*z_0[0], (1-e)*z_0[1]])
        print(f'z_1: {z_1}')
        # Paso 5
        if qu > Q:
            print(f'Punto minimo: {x_0}')
            print(f'Rango final: {z_0}')
            repetir = False
        else:
            qu = qu + 1
            x_0 = p_min
            z_0 = z_1
            minimo_funcion_siguiente = minimo_funcion  # Almacenar el mínimo de la iteración actual para la siguiente iteración

x_0 = np.array([3,3])
z_0 = np.array([6,6])

r = aleatorio(x_0,z_0)
print()
