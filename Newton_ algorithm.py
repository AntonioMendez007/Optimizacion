import numpy as np
import math

#-------------------------------------------Busqueda Unidireccional--------------------------------------------------------------------------------------------------------------
import numpy as np

#Fase de acotamiento
def f(alpha,z,s):
    resultado = ((z[0]+(alpha*s[0]))**2 + (z[1]+(alpha*s[1])) -11)**2 + ((z[0]+(alpha*s[0])) + (z[1]+(alpha*s[1]))**2 -7)**2
    return resultado

def acotamiento(z,s):
    alpha=0
    delta=0.001
    k=0

    repetir=True

    f1=alpha - abs(delta)
    #print(f'f1: {f1}')
    res1=f(f1,z,s)
    #print(f'fx1: {res1}')
    fx0=f(alpha,z,s)
    #calcular f(x^0 + |delta|)
    f3=alpha + abs(delta)
    res3=f(f3,z,s)
    #print(f'fx2: {fx0}')
    #print(f'fx3: {res3}')
    t=[]

    if((res1 >= fx0 >= res3)):
        delta=abs(delta)
    elif ((res1 <= fx0 <= res3)):
        delta=delta*-1
    else:
        print("Reasigna nuevos valores")
        #print(f'delta: {delta}')
        repetir=False

    while(repetir):
            #delta+=0.5
            #print("Calcular el supuesto para k "+str(k))
            sumaX=k+1 #Definir el x^k+1, solo para indicar el orden de x
            #print(f'Sea x^k+1 = {sumaX}')
            resultado= alpha + (pow(2,k)*delta)
            print(resultado)
            evaluar=f(resultado,z,s)
            t.append(resultado)
            #print(f'Evaluar  x^k+1 = {evaluar}')
            if (evaluar < fx0):
                k+=1
                alpha=resultado
                fx0=f(alpha,z,s)
            else:
                #print("La condición  ya no se cumple")
                a=t[k-2]
                b=t[k]
                print(f'El intervalo es {a}, {b}') 
                break
    return a,b


#Seccion dorada
def fw(w,s,a,b):
    return(pow((pow(s[0] * (((b-a) * w) + a),2)+(s[1] * (((b-a) * w) + a))-11),2) 
              + pow(((s[0] * (((b-a) * w) + a))+pow(s[1] * (((b-a) * w) + a),2)-7),2))

def dorada(a,b,e,s1):
    #Paso 1
    # x = a porque se va a normalizar
    #x = b porque s eva a normalizar
    print(f'a: {a}')
    print(f'b: {b}')
    #w_p=(a-a)/(b-a)
    #w_s=(b-a)/(b-a)

    a_w=0
    b_w=1
    k=1

    repetir=True
    while(repetir):
        L_w = b_w - a_w
        w1= a_w + ((0.618)*(L_w))
        
        w2= b_w - ((0.618)*(L_w))
        
        #Funcion transformada
        f_w1=fw(w1,s1,a,b)
        f_w2=fw(w2,s1,a,b)
        #print(w1,w2,f_w1,f_w2)
        if (f_w1 > f_w2):
            #print(f'El mínimo no esta en (w1,b_w)')
            a_w=a_w
            b_w=w1

            if (abs(L_w) < e):
                alfa=a_w*(b-a)+a
                alfa2=b_w*(b-a)+a
                #print(f'El minimo esta en {a_w,b_w} = {alfa,alfa2}')
                p_medio=(alfa+alfa2)/2
                intervalo = x+(p_medio*s1)
                #print(f'Alpha = {p_medio}')
                print(f'Intervalos: {intervalo}')
                
                repetir=False
                return p_medio
            else:
                k=k+1
                
        elif (f_w1 < f_w2):
            #print("El minimo no esta en (a_w,x2)")
            a_w=w2
            b_w=b_w

            if (abs(L_w) < e):
                alfa=a_w*(b-a)+a
                alfa2=b_w*(b-a)+a
                #print(f'El minimo esta en {a_w,b_w} = {alfa,alfa2}')
                p_medio=(alfa+alfa2)/2
                intervalo = x+(p_medio*s1)
                #print(f'Alpha = {p_medio}')
                print(f'Intervalos: {intervalo}')
                
                repetir=False
                return p_medio
            else:
                k=k+1
                
        elif (f_w1 == f_w2):
          a = w1
          b = w2
          if (abs(L_w) < e):
            alfa=a_w*(b-a)+a
            alfa2=b_w*(b-a)+a
            #print(f'El minimo esta en {a_w,b_w} = {alfa,alfa2}')
            p_medio=(alfa+alfa2)/2
            intervalo = x+(p_medio*s1)
            #print(f'Alpha = {p_medio}')
            print(f'Intervalos: {intervalo}')
            
            repetir=False
            return p_medio
          else:
            k = k + 1
            s1=intervalo

def himelblau(x1,x2):
    resultado = pow( pow(x1,2) + x2 - 11, 2 ) + pow( x1 + pow(x2,2) - 7, 2 )
    return resultado

def primera_derivada(x0,delta):
    delta = 0.001
    print(x0)
    if x0[0] < 0.01:
        a = (himelblau(((x0[0])+delta),(x0[1])))
        b = (himelblau(((x0[0])-delta),(x0[1])))
        d1 = (a-b)/(2*delta)
    else:
        a = (himelblau(((x0[0])+(delta*x0[0])),(x0[1])))
        b = (himelblau(((x0[0])-(delta*x0[0])),(x0[1])))
        d1 = (a-b)/((2*delta)*x0[0])
    
    if x0[1]<0.01:
        c = (himelblau((x0[0]),((x0[1])+delta)))
        d = (himelblau((x0[0]),((x0[1])-delta)))
        d2 = (c-d)/(2*delta)
    else:
        c = (himelblau((x0[0]),((x0[1])+(delta)*x0[1])))
        d = (himelblau((x0[0]),((x0[1])-(delta)*x0[1])))
        d2 = (c-d)/((2*delta)*x0[1])

    delta_fx = np.array([d1,d2])
    return delta_fx

def hessian(x):
    matriz = [[0,0],
              [0,0]]
    delta = 0.001
    # x1
    if (x[0] and x[1]) < 0.01:
        primera_parte = [x[0]+delta,x[1]]
        first_evaluacion = himelblau(primera_parte[0],primera_parte[1]) - 2*himelblau(x[0],x[1])
        #print(f'evaluacion: {first_evaluacion}')
        segunda_parte = [x[0]-delta,x[1]]
        second_evaluacion = himelblau(segunda_parte[0],segunda_parte[1])
        suma = first_evaluacion + second_evaluacion
        #print(f'suma: {suma}')
        division = suma / pow(delta,2)
        #print(f'x1 primero: {division}')
    else:
        primera_parte = [x[0]+(delta*x[0]),x[1]]
        first_evaluacion = himelblau(primera_parte[0],primera_parte[1]) - 2*himelblau(x[0],x[1])
        segunda_parte = [x[0]-(delta*x[0]),x[1]]
        second_evaluacion = himelblau(segunda_parte[0],segunda_parte[1])
        suma = first_evaluacion + second_evaluacion
        #print(f'suma: {suma}')
        division = suma / pow((delta*x[0]),2)
        #print(f'x1 segundo: {division}')
    # x2
    if (x[0] and x[1]) < 0.001:
        primera_parte2 = [x[0],x[1]+delta]
        first_evaluacion2 = himelblau(primera_parte2[0],primera_parte2[1]) - 2*himelblau(x[0],x[1])
        segunda_parte2 = [x[0],x[1]-delta]
        second_evaluacion2 = himelblau(segunda_parte2[0],segunda_parte2[1])
        suma2 = first_evaluacion2 + second_evaluacion2
        division2 = suma2 / pow(delta,2)
    else:
        primera_parte2 = [x[0],x[1]+(delta*x[1])]
        first_evaluacion2 = himelblau(primera_parte2[0],primera_parte2[1]) - 2*himelblau(x[0],x[1])
        segunda_parte2 = [x[0],x[1]-(delta*x[1])]
        second_evaluacion2 = himelblau(segunda_parte2[0],segunda_parte2[1])
        suma2 = first_evaluacion2 + second_evaluacion2
        division2 = suma2 / pow((delta*x[1]),2)
    # x1x2
    if (x[0] and x[1]) < 0.001:
        evaluacion = himelblau((x[0]+delta),(x[1]+delta))
        evaluacion2 = himelblau((x[0]+delta),(x[1]-delta))
        evaluacion3 = himelblau((x[0]-delta),(x[1]+delta))
        evaluacion4 = himelblau((x[0]-delta),(x[1]-delta))
        numerador = evaluacion - evaluacion2 - evaluacion3 + evaluacion4
        division3 = numerador / (4*delta*delta)
    else:
        evaluacion = himelblau((x[0]+(delta*x[0])),(x[1]+(delta*x[1])))
        evaluacion2 = himelblau((x[0]+(delta*x[0])),(x[1]-(delta*x[1])))
        evaluacion3 = himelblau((x[0]-(delta*x[0])),(x[1]+(delta*x[1])))
        evaluacion4 = himelblau((x[0]-(delta*x[0])),(x[1]-(delta*x[1])))
        numerador = evaluacion - evaluacion2 - evaluacion3 + evaluacion4
        division3 = numerador / ((4*delta*x[0])*(delta*x[1]))
    
    matriz[0][0]=division
    matriz[1][1]=division2
    matriz[0][1]=division3
    matriz[1][0]=division3
    matriz_= np.array(matriz)
    #print(matriz_)

    return matriz_

def newton(x,M,e1):
    k = 0
    delta = 1
    repetir = True
    iteracion = 0
    while(repetir):
        iteracion+=1
        print("----------------------------------------------")
        print(f'Iteracion Newton: {iteracion}')
        # Paso 2
        delta_fxk = primera_derivada(x,delta)
        print("Derivada ",delta_fxk)
        # Paso 3
        if ( math.sqrt((pow(delta_fxk[0],2)) + (pow(delta_fxk[1],2))) ) <= e1:
            print("Java nais dei 1",x)
            repetir = False
        elif k >= M:
            print("Java nais dei 2",x)
            repetir = False
        # Paso 4: calcular la matriz hessiana
        he = hessian(x)
        print("Hessian")
        print(he)
        inversa = np.linalg.inv(h)
        print("Inversa")
        print(inversa)
        # Saber si la dirección es descendiente
        transpuesta = delta_fxk.transpose()
        print("Transpuesta")
        print(transpuesta)
        #valor = transpuesta * inversa * delta_fxk
        valor2 = np.dot(np.dot(transpuesta, inversa), delta_fxk)
        print("valor")
        print(valor2)
        if valor2 < 0:
            print("La dirección de búsqueda no es descendente")
            print("Punto nuevo")
            x1 = x - (np.dot(inversa,delta_fxk))
            print(f'x1: {x1}')
            # Búsqueda unidireccional
            parametro_a, parametro_b = acotamiento(x,x1)
            alfa = dorada(parametro_a, parametro_b,pow(10,-3),x1)
            print("Paso 4 alfa ",alfa) 
            if alfa < 0:
                print("No es una direccion descendente")
                print("Ingresa nuevos puntos")
                repetir=False
        else:
            print("La dirección de búsqueda es descendente")
            print("Punto nuevo")
            x1 = x - (np.dot(inversa,delta_fxk))
            print(f'x1: {x1}')
            # Búsqueda unidireccional
            parametro_a, parametro_b = acotamiento(x,x1)
            alfa = dorada(parametro_a, parametro_b,pow(10,-3),x1)
            print("Paso 4 alfa ",alfa) 
        
        # paso 5
        resta = x1 - x
        print(f'resta: {resta}')
        operacion = math.sqrt((pow(resta[0],2)) + (pow(resta[1],2)))/math.sqrt((pow(x[0],2)) + (pow(x[1],2)))
        if operacion <= e1:
            print(f'Puntos finales: {x}')
            repetir = True
        else:
            k = k + 1
            x = x1



x=np.array([2,1])
h = hessian(x) 
n = newton(x,100,0.001)  
