import math
def himelblau(x1,x2):
    resultado = pow( pow(x1,2) + x2 - 11, 2 ) + pow( x1 + pow(x2,2) - 7, 2 )
    return resultado

def caminar(x0,delta,e):
    #Paso 1
    x_barra=x0
    #print("x_barra",x_barra)
    repetir=True
    iteracion=0
    while(repetir):
        iteracion+=1
        print("----------------------------------------------")
        print(f'Iteracion: {iteracion}')
        #Paso 2
        operacion_delta=math.sqrt((pow(delta[0],2)) + (pow(delta[1],2)))
        print(f'delta barra: {operacion_delta}')
        if (operacion_delta < e):
            print("Terminamos pa")
            print(f'x0: {x0}')
            fx0=himelblau(x0[0],x0[1])
            print(f'fx0: {fx0}')
            repetir=False
        else:
            print("Pasamos al else")
            #Dividimos los valores de delta entre 2
            delta1=(delta[0]/2)
            delta2=(delta[1]/2)

            #Resta, Resta
            x1=[x_barra[0]-delta1,x_barra[1]-delta2]
            print(f'x1: {x1}')
            #Suma, Resta
            x2=[x_barra[0]+delta1,x_barra[1]-delta2]
            print(f'x2: {x2}')
            #Resta, Suma
            x3=[x_barra[0]-delta1,x_barra[1]+delta2]
            print(f'x3: {x3}')
            #Suma, Suma
            x4=[x_barra[0]+delta1,x_barra[1]+delta2]
            print(f'x4: {x4}')

            #Pasarlos a la función
            print("Paso 3")
            f_x0=himelblau(x0[0],x0[1])
            print(f'f_x0: {f_x0}')

            f_x1=himelblau(x1[0],x1[1])
            print(f'f_x1: {f_x1}')

            f_x2=himelblau(x2[0],x2[1])
            print(f'f_x2: {f_x2}')

            f_x3=himelblau(x3[0],x3[1])
            print(f'f_x3: {f_x3}')

            f_x4=himelblau(x4[0],x4[1])
            print(f'f_x4: {f_x4}')
        
            #Obtener el valor minimo de la función
            minimo = f_x0

            if f_x1 < minimo:
                minimo = f_x1

            if f_x2 < minimo:
                minimo = f_x2

            if f_x3 < minimo:
                minimo = f_x3

            if f_x4 < minimo:
                minimo = f_x4

            print("El valor más pequeño es:", minimo)

            if minimo == f_x0:
                x_barra = x0

            if minimo == f_x1:
                x_barra = x1

            if minimo == f_x2:
                x_barra = x2

            if minimo == f_x3:
                x_barra = x3
            
            if minimo == f_x4:
                x_barra = x4
            print("x_barra:", x_barra)
            #Paso 4
            print("Paso 4")
            if x_barra == x0:
                delta=[(delta[0]/2),(delta[1]/2)]
                print(f'delta: {delta}')
            else:
                x0=x_barra
                print(f'x0: {x0}')
                
            #repetir=False

x_cero=[1,1]
delta=[2,2]
s=caminar(x_cero,delta,pow(10,-3))
print()