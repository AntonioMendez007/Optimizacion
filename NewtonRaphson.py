import math

def fun(x):
    if(x==0):
        return float('inf')
    else:
        resultado=pow(x,2)+(54/x)
    return resultado

def deltaX_t(x_t):
    if x_t > 0.01:
        return ( (0.01)*(abs(x_t)) )
    else:
        return 0.0001
#Derivada 1
def f_prima(x):
    delta_x=0
    if abs(x) > 0.01:
        delta_x= ( (0.01)*(abs(x)) )
        deri_x=( fun(x+delta_x) - fun(x-delta_x) ) / (2*delta_x)
        return deri_x
    else:
        delta_x= 0.0001
        deri_x=( fun(x+delta_x) - fun(x-delta_x) ) / (2*delta_x)
        return deri_x
    
#Derivada 2
def f_prima2(x):
    delta_x=0
    if abs(x) > 0.01:
        delta_x= ( (0.01)*(abs(x)) )
        deri_x=( (fun(x + delta_x)) -(2 * (fun(x))) + (fun(x - delta_x)) ) / (pow(delta_x,2))
        return deri_x
    else:
        delta_x= 0.0001
        deri_x=( (fun(x + delta_x)) -(2 * (fun(x))) + (fun(x - delta_x)) ) / (pow(delta_x,2))
        return deri_x
''' 
def N_R(x,e):
    #paso 1
    k=1
    f1=f_prima(x)
    print(f'f1: {f1}')
    repetir=True
    while(repetir):
        #Paso 2
        f2=f_prima2(x)
        print(f'f2: {f2}')
        #Paso 3
        x_k=k-(f1/f2)
        print(f'x_k: {x_k}')

        f_xk=f_prima(x_k)
        print(f'f_xk: {f_xk}')

        if (abs(f_xk) < e):
            print(f'ola')
            repetir=False
        else:
            k=k+1
            x=x+1
'''
def N_R(x,e):
    #paso 1
    k=1
    f1=f_prima(x)
    print(f'f1: {f1}')
    repetir=True
    iteracion=0
    while(repetir):
        iteracion=iteracion+1
        print(f'Iteración: {iteracion}')
        
        print(f'k: {k}')
        #Paso 2
        f2=f_prima2(k)
        print(f'f2_x^k: {f2}')
        #Paso 3
        x_k=k-(f_prima(k)/f_prima2(k))
        print(f'x_k: {x_k}')

# Lo que hice en este apartado, es que como ya me había salido la primera iteración, en la segunda los valores ya no me coincidian, y como a k
# la tomé en general, vi que en una de las fórmulas, cambiaba x y k y ya no eran iguales, es por ello que opté por cambiar x por k para
# ya no volver a reestructurar las variables. Le pongo esto por si observa otra variable que no es la "correcta" pero en mi caso si lo es y
# en general el programa funciona, solo era ese detalle.
        f_xk=f_prima(x_k)
        print(f'f_x^k+1: {f_xk}')

        if (abs(f_xk) < e):
            print(f'Punto mínimo: {k}')
            repetir=False
        else:
            x=x+1
            k=x_k
N_R(1,pow(10,-3))
print()