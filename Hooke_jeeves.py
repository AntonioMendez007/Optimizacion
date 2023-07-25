import math
def himelblau(x1,x2):
    resultado = pow( pow(x1,2) + x2 - 11, 2 ) + pow( x1 + pow(x2,2) - 7, 2 )
    return resultado

# Método exploratorio
def exploratorio(x0,x_c,delta):
    
    i=1
    n=2

    # Paso 1
    f_pos=[(x0[0]+delta[0]),x0[1]]
    fx=x_c
    f_neg=[(x0[0]-delta[0]),x0[1]]

    repetir=True
    iteracion=0
    resultado_satisfactorio = None
    while(repetir):
        iteracion+=1
        print("----------------------------------------------")
        print(f'Iteracion: {iteracion}')
        
        f1=himelblau(f_pos[0],f_pos[1])
        f=himelblau(fx[0],fx[1])
        f2=himelblau(f_neg[0],f_neg[1])

        #paso 2
        lista = [f1,f,f2]
        minimo = min(lista)
        index_min = lista.index(min(lista))
        x_aux = [f_pos,f,f_neg]
        x = x_aux[index_min]

        # Paso 3
        if (i==n):
            print("Ve al paso 4")
            if(x_c != x):
                print("satisfactorio")
                print(f'x: {x}')
                resultado_satisfactorio = x
                repetir=False
            else:
                print("Fallo")
                print(f'x: {x}')
                repetir=False

        else:
            i = i+1
            x0=x
            f_pos = [x0[0],(x0[1]+delta[1])]
            fx = x
            f_neg = [x0[0],(x0[1]-delta[1])]
    return resultado_satisfactorio 

x0 = [0.0,0.0]
x_c = [0.0,0.0]
delta = [0.5,0.5]
alpha = 2
ss = exploratorio(x0,x_c,delta)
#print(ss)
def hooke(delta, alpha,e,s):
    #Paso 1
    k=0
    repetir=True
    iteracion=0
    while(repetir):
        iteracion+=1
        print("----------------------------------------------")
        print(f'Iteracion: {iteracion}')

        #paso 2: aplicar el mov. exploratorio
        x_0=[0.0,0.0]
        xc=[0.0,0.0]
        explo2 = exploratorio(x_0,xc,delta)
        if explo2 is not None:
            print("Ve al paso 4")
            x_1 = explo2
        else:
            print("Ve al paso 3")
            # Paso 3
            operacion_delta=math.sqrt((pow(delta[0],2)) + (pow(delta[1],2)))
            print(f'delta raiz: {operacion_delta}')
            if(operacion_delta < e):
                print("Java nais dei")
                repetir = False
            else:
                delta= delta/alpha

        k=k+1
        # Paso 4: Realizar el movimiento del patrón
        x_p = [float(x_1[0]) + (float(x_1[0]) - x_0[0]), x_1[1] + (x_1[1] - x_0[1])]

        # Paso 5: Aplicar el mov. exploratorio
        explo4 = exploratorio(x_p,xc,delta)
        if explo4 is not None:
            x_2 = explo4
        else:
            print("Ve al paso 3")
            # Paso 3
            operacion_delta=math.sqrt((pow(delta[0],2)) + (pow(delta[1],2)))
            print(f'delta raiz: {operacion_delta}')
            if(operacion_delta < e):
                print("Java nais dei")
                repetir = False
            else:
                delta= delta/alpha
        # Paso 6
        f_x1 = himelblau(x_1[0],x_1[1])
        f_x2 = himelblau(x_2[0],x_2[1])

        if (f_x2 < f_x1):
            print("paso 6: ve al paso 4")
        else:
            operacion_delta=math.sqrt((pow(delta[0],2)) + (pow(delta[1],2)))
            if(operacion_delta < e):
                repetir = False
            else:
                print("Paso 6: regresa al paso 3")

x0 = [0.0,0.0]
x_c = [0.0,0.0]
delta = [0.5,0.5]
alpha = 2

print("Hooke")
j = hooke(delta, alpha,0.001,ss)