import math

def f(x):
    if(x==0):
        return float('inf')
    else:
        resultado=pow(x,2)+(54/x)
    return resultado


def Busqueda(a,b,n):
    x1=a
    deltaX=(b-a)/n
    x2=x1+deltaX
    x3=x2+deltaX

    fx1=f(x1)
    fx2=f(x2)
    fx3=f(x3)
    repetir=True
    while(repetir):
        if(fx1>=fx2<=fx3):
            print(f'El punto minimo se encuentra en {x1,x3}')
            repetir=False
        else:
            x1=x2
            x2=x3
            x3=x2+deltaX
            '''
            print(x1)
            print(x2)
            print(x3)
            '''
        if x3<=b:
            fx1=fx2
            fx2=fx3
            fx3=f(x3)
            '''
            print(fx1)
            print(fx2)
            print(fx3)
            '''
        if x3>b:
            print(f'No hay un punto mínimo, pero el valor esta en una de nuestras fronteras {a,b}')
            break
       


Parametros=Busqueda(1,7,10)
print()
