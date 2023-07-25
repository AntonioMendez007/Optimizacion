import math
def himelblau(x1,x2):
    resultado = pow( pow(x1,2) + x2 - 11, 2 ) + pow( x1 + pow(x2,2) - 7, 2 )
    return resultado

def centroide(x_1,x_2,n):
    x_c=((1/n)*(x_1[0]+x_2[0]),(1/n)*(x_1[1]+x_2[1]))
    return x_c

def q(f1,f2,f3,fc,n):
    q_1=(((f1-fc)**2)/(n+1) + ((f2-fc)**2)/(n+1) + ((f3-fc)**2)/(n+1))**0.5
    return q_1

def simple(x1,x2,x3,g,b,e):
    f_x1=himelblau(x1[0],x1[1])
    f_x2=himelblau(x2[0],x2[1])
    f_x3=himelblau(x3[0],x3[1])

    # Paso 2
    lista = [f_x1,f_x2,f_x3]
    minimo = min(lista)
    index_min = lista.index(min(lista))
    maximo = max(lista)
    index_max = lista.index(max(lista))
    x_aux = [x1,x2,x3]
    x_h = x_aux[index_max]
    x_l = x_aux[index_min]
    x_g = -1
    for i in range(len(x_aux)):
       if not (i == index_min or i == index_max):
          x_g = x_aux[i]

    x_c = centroide(x_l, x_g, 2)
    fc = himelblau(x_c[0],x_c[1])
    q_1 = q(f_x1, f_x2, f_x3, fc,2)

    iteracion=0
    while(q_1>=e):
        iteracion+=1
        print("----------------------------------------------")
        print(f'Iteracion: {iteracion}')

        x_r=((2*x_c[0])-x_h[0],(2*x_c[1])-x_h[1])
        fr = himelblau(x_r[0],x_r[1])   
            
        if fr < lista[index_min]:
            x_nuevo = ((1+g)*x_c[0]-(g*x_h[0]),(1+g)*x_c[1]-(g*x_h[1]))
            f_xnuevo = himelblau(x_nuevo[0],x_nuevo[1])
            x_aux[x_aux.index(x_h)]=x_nuevo
            lista[x_aux.index(x_nuevo)]=f_xnuevo
            
        elif fr >= lista[index_max]:
            x_nuevo = ((1 - b) * x_c[0] + (b * x_h[0]), (1 - b) * x_c[1] + (b * x_h[1]))
            f_xnuevo = himelblau(x_nuevo[0],x_nuevo[1])
            x_aux[x_aux.index(x_h)]=x_nuevo
            lista[x_aux.index(x_nuevo)]=f_xnuevo
            
        elif fr < lista[index_max] and fr > lista[x_aux.index(x_g)]:
            x_nuevo = ((1 + b) * x_c[0] - (b * x_h[0]), (1 + b) * x_c[1] - (b * x_h[1]))
            f_xnuevo = himelblau(x_nuevo[0],x_nuevo[1])
            x_aux[x_aux.index(x_h)]=x_nuevo
            lista[x_aux.index(x_nuevo)]=f_xnuevo
        
        else: 
          x_nuevo=x_r
          f_xnuevo=himelblau(x_nuevo[0],x_nuevo[1])
          x_aux[x_aux.index(x_h)]=x_nuevo
          lista[x_aux.index(x_nuevo)]=f_xnuevo
        
        index_min=lista.index(min(lista))
        index_max=lista.index(max(lista))
        x_h = x_aux[index_max]
        x_l = x_aux[index_min]
        x_g = -1
        for i in range(len(x_aux)):
            if not (i == index_min or i == index_max):
                x_g = x_aux[i]

        x_c = centroide(x_l, x_g, 2)
        fc = himelblau(x_c[0],x_c[1])
        q_1 = q(lista[0], lista[1], lista[2], fc,2)
    
    return print(x_l)
x_1=[0.0,0.0]
x_2=[2.0,0.0]
x_3=[1.0,1.0]
y=1.5
b=0.5

s=simple(x_1,x_2,x_3,y,b,pow(10,-4))
