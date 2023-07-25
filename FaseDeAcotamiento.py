import math
'''
def f(x):
    if(x==0):
        return float('inf')
    else:
        resultado=pow(x,2)+(54/x)
    return resultado
'''
def f(x):
    if(x==0):
        return float('inf')
    else:
        resultado=pow(x,2)+(4)
    return resultado

def acotamiento(x,delta,k):
    k=0

    repetir=True
    #calcular f(x^0 - |delta|)
    f1=x - abs(delta)
    print(f'f1: {f1}')
    res1=f(f1)
    print(f'res1: {res1}')
    fx0=f(x)
    #calcular f(x^0 + |delta|)
    f3=x + abs(delta)
    res3=f(f3)
    print(f'fx0: {fx0}')
    print(f'f1: {f1}')
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
            resultado= x + (pow(2,k)*delta)
            print(resultado)
            evaluar=f(resultado)
            t.append(resultado)
            print(f'Evaluar  x^k+1 = {evaluar}')
            if (evaluar < fx0):
                k+=1
                x=resultado
                fx0=f(x)
            else:
                print("La condición  ya no se cumple")
                print(f'El intervalo es {t[k-2]}, {t[k]}') 
                
                
                break
    #print(t)
        
        
               

Parametros=acotamiento(26,0.4,0)
print()