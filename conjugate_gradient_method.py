import numpy as np
import math

#Seccion dorada
def fw(w,s,a,b):
    return(pow((pow(s[0] * (((b-a) * w) + a),2)+(s[1] * (((b-a) * w) + a))-11),2) 
              + pow(((s[0] * (((b-a) * w) + a))+pow(s[1] * (((b-a) * w) + a),2)-7),2))

def dorada(a,b,e,s1):
    print(f'ese 1: {s1}')
    #Paso 1
    # x = a porque se va a normalizar
    #x = b porque s eva a normalizar
    #print(f'a: {a}')
    #print(f'b: {b}')
    #w_p=(a-a)/(b-a)
    #w_s=(b-a)/(b-a)

    a_w=0
    b_w=1
    k=1
    print(f's[0]: {s1[0]}')
    print(f's[1]: {s1[1]}')
    #intervalo = np.array([])
    repetir=True
    iteracion = 0
    while(repetir):
        iteracion+=1
        print("----------------------------------------------")
        print(f'Iteracion dorada: {iteracion}')
        L_w = b_w - a_w
        w1= a_w + ((0.618)*(L_w))
        print("l_w: ",L_w)
        w2= b_w - ((0.618)*(L_w))
        
        #Funcion transformada
        f_w1=fw(w1,s1,a,b)
        f_w2=fw(w2,s1,a,b)
        #print("Dorada")
        print(w1,w2,f_w1,f_w2)
        if (f_w1 > f_w2):
            print(f'El mínimo no esta en (w1,b_w)')
            a_w=a_w
            b_w=w1

            if (abs(L_w) < e):
                alfa=a_w*(b-a)+a
                alfa2=b_w*(b-a)+a
                print(f'El minimo esta en {a_w,b_w} = {alfa,alfa2}')
                p_medio=(alfa+alfa2)/2
                intervalo = x+(np.dot(p_medio,s1))
                print(f'Alpha = {p_medio}')
                print(f'Intervalos: {intervalo}')
                
                repetir=False
                return p_medio
        elif (f_w1 < f_w2):
            print("El minimo no esta en (a_w,x2)")
            a_w=w2
            b_w=b_w

            if (abs(L_w) < e):
                alfa=a_w*(b-a)+a
                alfa2=b_w*(b-a)+a
                #print(f'El minimo esta en {a_w,b_w} = {alfa,alfa2}')
                p_medio=(alfa+alfa2)/2
                intervalo = x+(np.dot(p_medio,s1))
                print(f'Alpha = {p_medio}')
                print(f'Intervalos: {intervalo}')
                
                repetir=False
                return p_medio
                
        elif (f_w1 == f_w2):
          print("Pasa por aqui")
          a = w1
          b = w2
          #print("abs: ",abs(L_w))
          if (abs(L_w) < e):
            alfa=a_w*(b-a)+a
            alfa2=b_w*(b-a)+a
            #print(f'El minimo esta en {a_w,b_w} = {alfa,alfa2}')
            p_medio=(alfa+alfa2)/2
            
            intervalo = x+(np.dot(p_medio,s1))
            print(f'Alpha = {p_medio}')
            print(f'Intervalos: {intervalo}')
            repetir=False
            return p_medio
          else:
            s1=intervalo
            print(f's1: {s1}')
            k = k + 1
            print(f'k: {k}')
            
    

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

def gradiente(x):
    # Paso 2
    delta = 1
    print("Inicia el gradiente-------")
    delta_fxk = primera_derivada(x,delta)
    print("Derivada ",delta_fxk)
    s0 = (-1*(delta_fxk[0]),-1*(delta_fxk[1]))
    print("s0")
    print(s0)
    # Paso 3
    busqueda0 = dorada(x[0],x[1],pow(10,-3),s0)
    print("busqueda")
    print(busqueda0)
    x1 = x + (np.dot(busqueda0,s0))
    print("X1: ")
    print(x1)
    k = 1
    delta_fx1 = primera_derivada(x1,delta)
    print("Derivada x1: ")
    print(delta_fx1)
    repetir = True
    iteracion = 0
    while(repetir):
        iteracion+=1
        print("----------------------------------------------")
        print(f'Iteracion Gradient: {iteracion}')

        # Paso 4
        s_1 = (-1*(delta_fx1[0]),-1*(delta_fx1[1])) + ( ((delta_fx1[0])**2+(delta_fx1[1])**2)/((delta_fxk[0])**2+(delta_fxk[1])**2) ) 
        s1 = s_1*s0
        print("S1: ")
        print(s1)

        # Calcular su ángulo
        cos_u = [s0[0]/(math.sqrt((s0[0])**2 + (s0[1])**2)),s0[1]/(math.sqrt((s0[0])**2 + (s0[1])**2))]
        cos_o = [s1[0]/(math.sqrt((s1[0])**2 + (s1[1])**2)),s1[1]/(math.sqrt((s1[0])**2 + (s1[1])**2))]
        cos_f = (cos_u[0]*cos_o[0]) + (cos_u[1]*cos_o[1])
        cos_1 = math.acos(cos_f)
        print("Coseno -1: ")
        print(cos_1)

        # Paso 5
        busqueda1 = dorada(x1[0],x1[1],0.001,s1)
        print("busqueda 2")
        print(busqueda1)
        x2 = x1 + (np.dot(busqueda1,s1))
        print("X2: ")
        print(x2)

        # Paso 6
        x_3 = x2 - x1
        x_4 = math.sqrt(((x_3[0])**2+(x_3[1])**2))/math.sqrt(((x1[0])**2+(x1[1])**2))
        fx2 = primera_derivada(x2,delta)
        delta_fx2 = math.sqrt(((fx2[0])**2+(fx2[1])**2))
        if x_4 < 0.001 or delta_fx2 < 0.001:
            print(f'Puntos minimos: {x}')
            repetir = False
        else:
            k = k + 1
            x = x2




x = np.array([0,0])
g = gradiente(x)