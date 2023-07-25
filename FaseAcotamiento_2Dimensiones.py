import math
import numpy as np


#Fase de acotamiento
def f(alpha):
    resultado = pow(((2*alpha)-8),2) + pow((5*alpha)-9,2)
    return resultado

def acotamiento(alpha,delta,k):
    k=0

    repetir=True
    #calcular f(x^0 - |delta|)
    f1=alpha - abs(delta)
    print(f'f1: {f1}')
    res1=f(f1)
    print(f'fx1: {res1}')
    fx0=f(alpha)
    #calcular f(x^0 + |delta|)
    f3=alpha + abs(delta)
    res3=f(f3)
    print(f'fx2: {fx0}')
    print(f'fx3: {res3}')
    t=[]

    if((res1 >= fx0 >= res3)):
        delta=abs(delta)
    elif ((res1 <= fx0 <= res3)):
        delta=delta*-1
    else:
        print("Reasigna nuevos valores")
        repetir=False

    while(repetir):
            #delta+=0.5
            print("Calcular el supuesto para k "+str(k))
            sumaX=k+1 #Definir el x^k+1, solo para indicar el orden de x
            print(f'Sea x^k+1 = {sumaX}')
            resultado= alpha + (pow(2,k)*delta)
            print(resultado)
            evaluar=f(resultado)
            t.append(resultado)
            print(f'Evaluar  x^k+1 = {evaluar}')
            if (evaluar < fx0):
                k+=1
                alpha=resultado
                fx0=f(alpha)
            else:
                print("La condición  ya no se cumple")
                print(f'El intervalo es {t[k-2]}, {t[k]}') 
                
                
                break
    #print(t)




#Seccion dorada
def fw(w):
    resultado = pow(((2*((3*w)+0.5))-8),2) + pow(((5*((3*w)+0.5))-9),2)
    return resultado

def dorada(a,b,e):
    #Paso 1
    # x = a porque se va a normalizar
    #x = b porque s eva a normalizar
    w_p=(a-a)/(b-a)
    w_s=(b-a)/(b-a)
    print(f'a_p = {w_p}')
    print(f'b_s = {w_s}')

    a_w=w_p
    b_w=w_s
    print(f'a_w = {w_p}')
    print(f'b_w = {w_s}')

    k=1

    repetir=True
    while(repetir):
        L_w = b_w - a_w
        print(f'L_w: {L_w}')
        #Paso 2
        w1= a_w + ((0.618)*(L_w))
        w2= b_w - ((0.618)*(L_w))
        print(f'w1 = {w1}')
        print(f'w2 = {w2}')
        
        #Funcion transformada
        f_w1=fw(w1)
        f_w2=fw(w2)
        print(f'f_w1 = {f_w1}')
        print(f'f_w2 = {f_w2}')

        if (f_w1 > f_w2):
            print(f'El mínimo no esta en (w1,b_w)')
            a_w=a_w
            b_w=w1
            print(f'a_w {a_w}')
            print(f'b_w {b_w}')
            print(f'l_w {L_w}')
            #Paso 4
            if (abs(L_w) < e):
                #x = 5 *w
                alfa=(3*a_w)+0.5
                alfa2=(3*b_w)+0.5
                print(f'El minimo esta en {a_w,b_w} = {alfa,alfa2}')
                p_medio=(alfa+alfa2)/2
                x=[2,1]
                s=[2,5]
                res=p_medio*s[0]
                res1=p_medio*s[1]
                punto1=x[0]+res
                punto2=x[1]+res1
                print(f'El punto mas minimo esta en= {punto1,punto2}')
                repetir=False
            else:
                k=k+1
                
        elif (f_w1 < f_w2):
            print("El minimo no esta en (a_w,x2)")
            a_w=w2
            b_w=b_w
            print(f'a_w {a_w}')
            print(f'b_w {b_w}')
            #Paso 4
            print(f'l_w {L_w}')
            if (abs(L_w) < e):
                alfa=(3*a_w)+0.5
                alfa2=(3*b_w)+0.5
                print(f'El minimo esta en {a_w,b_w} = {alfa,alfa2}')
                p_medio=(alfa+alfa2)/2
                x=[2,1]
                s=[2,5]
                res=p_medio*s[0]
                res1=p_medio*s[1]
                punto1=x[0]+res
                punto2=x[1]+res1
                print(f'El punto mas minimo esta en= {punto1,punto2}')
                repetir=False
            else:
                k=k+1
                
        elif (f_w1 == f_w2):
          a = w1
          b = w2
          print(f'l_w {L_w}')
          print(f'a_w {a_w}')
          print(f'b_w {b_w}')
          if (abs(L_w) < e):
            alfa=(3*a_w)+0.5
            alfa2=(3*b_w)+0.5
            print(f'El minimo esta en {a_w,b_w} = {alfa,alfa2}')
            p_medio=(alfa+alfa2)/2
            x=[2,1]
            s=[2,5]
            res=p_medio*s[0]
            res1=p_medio*s[1]
            punto1=x[0]+res
            punto2=x[1]+res1
            print(f'El punto mas minimo esta en= {punto1,punto2}')
            repetir=False
          else:
            k = k + 1

Parametros=acotamiento(0,0.5,0)
print()
#0.5 y 3.5 son el resultado del algoritmo fase de acotamiento.
#Lo que se realiza en este primer algoritmo, es acotar el encontrar el espacio de búsqueda,
#y en el de la sección dorada solo se hace más preciso para encontrar los puntos más mínimos.
dorada(0.5,3.5,pow(10,-3))
print()