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
                intervalo = x+(np.dot(p_medio,s1))
                #print(f'Alpha = {p_medio}')
                print(f'Intervalos: {intervalo}')
                
                repetir=False
                return p_medio

        elif (f_w1 < f_w2):
            #print("El minimo no esta en (a_w,x2)")
            a_w=w2
            b_w=b_w

            if (abs(L_w) < e):
                alfa=a_w*(b-a)+a
                alfa2=b_w*(b-a)+a
                #print(f'El minimo esta en {a_w,b_w} = {alfa,alfa2}')
                p_medio=(alfa+alfa2)/2
                intervalo = x+(np.dot(p_medio,s1))
                #print(f'Alpha = {p_medio}')
                print(f'Intervalos: {intervalo}')
                
                repetir=False
                return p_medio
        elif (f_w1 == f_w2):
          a = w1
          b = w2
          if (abs(L_w) < e):
            alfa=a_w*(b-a)+a
            alfa2=b_w*(b-a)+a
            #print(f'El minimo esta en {a_w,b_w} = {alfa,alfa2}')
            p_medio=(alfa+alfa2)/2
            intervalo = x+(np.dot(p_medio,s1))
            #print(f'Alpha = {p_medio}')
            print(f'Intervalos: {intervalo}')
            
            repetir=False
            return p_medio
          else:
            k = k + 1
            s1=intervalo
        

# El cambio que tuve que realizar, es que a la primera función tenía que ser vacía, es decir, no recibir parámetros, sino, establecerselos
# ahí mismo, para que la segunda pudiera recibir los dos puntos mínimos.
#z=np.array([0,0])
#x=np.array([0,0])
#s=np.array([14,22])
#parametro_a, parametro_b = acotamiento(z,s)
#alfa = dorada(parametro_a, parametro_b,pow(10,-3),z,s)
#print(alfa)
#----------------------------------------------------Fin de la búsqueda unidireccional-------------------------------------------------------------------

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

#x = [1.788, 2.810]
#delta = 0.001

#f = primera_derivada(x,delta)
#print(f)

def cauchy(M,x_0,e1,e2):
    k = 0
    delta = 1
    
    repetir = True
    iteracion = 0
    while(repetir):
        iteracion+=1
        print("----------------------------------------------")
        print(f'Iteracion cauchy: {iteracion}')

        # Paso 2
        delta_fxk = primera_derivada(x_0,delta)
        print("derivada ",delta_fxk)
        s = (-1*(delta_fxk[0]),-1*(delta_fxk[1]))
        # Paso 3
        if ( math.sqrt((pow(delta_fxk[0],2)) + (pow(delta_fxk[1],2))) ) <= e1:
            print("Java nais dei 1",x_0)
            repetir = False
        elif k >= M:
            print("Java nais dei 2",x_0)
            repetir = False
        #Paso 4
        parametro_a, parametro_b = acotamiento(x_0,s)
        alfa = dorada(parametro_a, parametro_b,pow(10,-3),s)
        print("Paso 4 alfa ",alfa) 
        multiplicacion = (alfa*delta_fxk[0])+(alfa*delta_fxk[1])
        #print("Multiplicacion: ",multiplicacion)
        restaf = np.subtract(x_0, multiplicacion)
        #print(f'restaf: {restaf}')
        fxk1 = himelblau(restaf[0],restaf[1])
        print(f'Paso 4 evaluacion: {fxk1}')
        multiplicacion2 = (fxk1*delta_fxk[0])+(fxk1*delta_fxk[1])
        #print(f'Paso 4 multiplicacion 2: {multiplicacion2}')
        if abs(multiplicacion2)<=e2:
            print("Java nais dei 3",x_0)
            repetir = False
        #Paso 5
        resta = np.subtract(restaf, x_0)
        #print(f'Paso 5 resta: {resta}')
        numerador = ( math.sqrt((pow(resta[0],2)) + (pow(resta[1],2))) )
        #print(f'numerador paso 5: {numerador}')
        
        if np.array_equal(x_0,[0,0]):
            division = 0.01 #pow(10,100)
        else:
            denominador = ( math.sqrt((pow(x_0[0],2)) + (pow(x_0[1],2))) )
            division = numerador/denominador
        
        print(f'Paso 5 resultado division: {division}')
        if(division<=e1):
            print("Java nais dei 4",x_0)
            repetir=False
        else:
            x_0 = restaf
            k = k + 1
    return x_0

z=np.array([0,0])
x=np.array([0,0])
s=np.array([14,22])
parametro_a, parametro_b = acotamiento(z,s)
alfa = dorada(parametro_a, parametro_b,pow(10,-3),s)

c = cauchy(100,x,pow(10,-3),pow(10,-3))
            
