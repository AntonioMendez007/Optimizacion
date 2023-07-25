import math

def f(x):
    if(x==0):
        return float('inf')
    else:
        resultado=pow(x,2)+(54/x)
    return resultado

def Division(a,b,e):
    #Paso 1
    X_m=(a+b)/2
    L=b-(a)
    print(f'X_m= {X_m}')
    print(f'L= {L}')
    lista=[L]
    repetir=True
    
    while(repetir):
        #Paso 2
        x1= a + (L/4)
        x2= b - (L/4)
        f_Xm=f(X_m)
        print(f'X1: {x1}')
        print(f'X2: {x2}')
            #Calcular f(x1) y f(x2)
        f_x1=f(x1)
        f_x2=f(x2)
        print(f'f_X1: {f_x1}')
        print(f'f_X2: {f_x2}')
        print(f'f_xm: {f_Xm}')
        

        if(f_x1 < f_Xm):
            print("Paso 3")
            b=X_m
            X_m=x1
            #Paso 5          
            #print(f'L=b-a condición 1: {L}')
            L=b-a
            if(abs(L)< e):
                print("TERMINADO")
                print(f'El intervalo es: {a,b}')
                print(f'L: {lista}')
                print(f'Ls: {L}')
                repetir=False
            
        elif(f_x2 < f_Xm):
            print("Paso 4")
            a=X_m
            X_m=x2
                #Paso 5
            
            #print(f'L=b-a condicion 2: {L}')
            L=b-a
            if(abs(L)< e):
                print("TERMINADO")
                print(f'El intervalo es: {a,b}')
                print(f'L: {lista}')
                print(f'Ls: {L}')
                repetir=False
            
        else:
            a=x1
            b=x2
                        #Paso 5
            L=b-a
                #print(f'L=b-a la 3: {L}')
            if(abs(L)< e):
                print("TERMINADO")
                print(f'El intervalo es: {a,b}')
                print(f'L: {lista}')
                print(f'Ls: {L}')
                repetir=False
        lista.append(L)
        


        

Division(3,9,pow(10,-3))
print()



    