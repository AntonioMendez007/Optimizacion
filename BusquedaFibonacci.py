

import math
'''
def fun(x):
    if(x==0):
        return float('inf')
    else:
        resultado=pow(x,2)+(54/x)
    return resultado
'''
def fun(x):
    if(x==0):
        return float('inf')
    else:
        resultado=pow(x,2)+(4)
    return resultado

def busqueda_F(a,b,n):
    #Paso 1
    k=2
    L=b - (a)
    print(f'L: {L}')
    
    #Calcular la sucesión de fibinacci
    f = 15   # número de términos de la lista
    fibo = [0,1]
    for i in range (f-2):
        fibo.append(fibo[-1] + fibo[-2])
    print(f'Sucesión de fibonacci {fibo}')

    repetir=True
    while(repetir):
        #Paso 2
        posicion1=((n-k) + 1) + 1
        posicion2=((n+1)) + 1
        # Estas líneas solo son para imprimir la posición y el número de la serie de fibonacci y ver que coincida; no es 
        # importante una vez que sale, imprimirlas.
        print(f'Posición 1: {posicion1}')
        print(f'Posición 2: {posicion2}')

        print(f'valor: {fibo[posicion1]}')
        print(f'valor: {fibo[posicion2]}')
        ##################################################
        L_Estrella_K= ( (fibo[posicion1]) / (fibo[posicion2]) ) *L
        print(f'L_estrella: {L_Estrella_K}')
        x1=a+L_Estrella_K
        x2=b-L_Estrella_K
        print(f'x1: {x1}')
        print(f'x2: {x2}')

        #Paso 3
        f_x1=fun(x1)
        f_x2=fun(x2)
        print(f'fun1 {f_x1}')
        print(f'fun2 {f_x2}')
        if (f_x1 > f_x2):
            print(f'El mínimo no esta en (a,x1)')
            a=x1
            b=b
            #Paso 4
            if (k==n):
                print(f'El minimo esta en ({a,b})')
                repetir=False
            else:
                k=k+1
                
        elif (f_x1 < f_x2):
            print("El minimo no esta en (x2,b)")
            a=a
            b=x2
            #Paso 4
            if (k==n):
                print(f'El minimo esta en ({a,b})')
                repetir=False
            else:
                k=k+1
        elif (f_x1 == f_x2):
          a = x1
          b = x2
          if ( k == n):
            print("El minimo esta en: ",a,",",b)
            repetir=False
          else:
            k = k + 1

busqueda_F(-2,2,2)
print()


#Valores a probar n=3, n=10, n=100, n = 1000
