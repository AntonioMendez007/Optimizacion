def himelblau(x1,x2):
    resultado = pow( pow(x1,2) + x2 - 11, 2 ) + pow( x1 + pow(x2,2) - 7, 2 )
    return resultado

def centroide(x_1,x_2,n):
    x_c=((1/n)*(x_1[0]+x_2[0]),(1/n)*(x_1[1]+x_2[1]))
    return x_c

def q(f1,f2,f3,fc,n):
    q_1=(((f1-fc)**2)/(n+1) + ((f2-fc)**2)/(n+1) + ((f3-fc)**2)/(n+1))**0.5
    return q_1

def main(gama,beta,epsilon):
    

    x1=[0,0]
    x2=[2,0]
    x3=[1,1]

    f1=himelblau(x1[0],x1[1])
    f2=himelblau(x2[0],x2[1])
    f3=himelblau(x3[0],x3[1])
    print(f'fx1: {f1}')
    print(f'fx2: {f2}')
    print(f'fx3: {f3}')

    lista=[f1,f2,f3]

    minimo=min(lista)
    index_min=lista.index(min(lista))
    maximo=max(lista)
    index_max=lista.index(max(lista))
    x_aux=[x1,x2,x3]
    x_h=x_aux[index_max]
    x_l=x_aux[index_min]
    x_g=-1
    for i in range(len(x_aux)):
        if not (i == index_min or i == index_max):
            x_g=x_aux[i]
    
    x_c=centroide(x_l,x_g,2)
    fc=himelblau(x_c[0],x_c[1])
    q1=q(f1,f2,f3,fc,2)
    iteracion=0
    while(q1>epsilon):
        iteracion+=1
        print(f'Iteracion: {iteracion}')
        x_r=(2*(x_c[0]-x_h[0]),2*(x_c[1]-x_h[1]))
        fr=himelblau(x_r[0],x_r[1])
        #x_new=x_r
        if fr < lista[index_min]:
            x_new=((1+gama)*x_c[0]-(gama*x_h[0]),(1+gama)*x_c[1]-(gama*x_h[1]))
            f_xnew=himelblau(x_new[0],x_new[1])
            x_aux[x_aux.index(x_h)]=x_new
            lista[x_aux.index(x_new)]=f_xnew
            index_min=lista.index(min(lista))
            index_max=lista.index(max(lista))
            x_h=x_aux[index_max]
            x_l=x_aux[index_min]
            x_g=-1
            for i in range(len(x_aux)):
                if not (i == index_min or i == index_max):
                    x_g=x_aux[i]
            
            x_c=centroide(x_l,x_g,2)
            fc=himelblau(x_c[0],x_c[1])
            q1=q(lista[0],lista[1],lista[2],fc,2)
        elif (fr >= lista[index_max]):
            x_new=((1-beta)*x_c[0]+beta*x_h[0],(1-beta)*x_c[1]+beta*x_h[1])
            f_xnew=himelblau(x_new[0],x_new[1])
            x_aux[x_aux.index(x_h)]=x_new
            lista[x_aux.index(x_new)]=f_xnew
            index_min=lista.index(min(lista))
            index_max=lista.index(max(lista))
            x_h=x_aux[index_max]
            x_l=x_aux[index_min]
            x_g=-1
            for i in range(len(x_aux)):
                if not (i == index_min or i == index_max):
                    x_g=x_aux[i]
            
            x_c=centroide(x_l,x_g,2)
            fc=himelblau(x_c[0],x_c[1])
            q1=q(lista[0],lista[1],lista[2],fc,2)
        elif (fr < lista[index_max] and fr > lista[index_max]):
            x_new=((1+beta)*x_c[0]-beta*x_h[0],(1+beta)*x_c[1]-beta*x_h[1])
            f_xnew=himelblau(x_new[0],x_new[1])
            x_aux[x_aux.index(x_h)]=x_new
            lista[x_aux.index(x_new)]=f_xnew
            index_min=lista.index(min(lista))
            index_max=lista.index(max(lista))
            x_h=x_aux[index_max]
            x_l=x_aux[index_min]
            x_g=-1
            for i in range(len(x_aux)):
                if not (i == index_min or i == index_max):
                    x_g=x_aux[i]
            
            x_c=centroide(x_l,x_g,2)
            fc=himelblau(x_c[0],x_c[1])
            q1=q(lista[0],lista[1],lista[2],fc,2)
        else:
            x_new=x_r
            f_xnew=himelblau(x_new[0],x_new[1])
            x_aux[x_aux.index(x_h)]=x_new
            lista[x_aux.index(x_new)]=f_xnew
            index_min=lista.index(min(lista))
            index_max=lista.index(max(lista))
            x_h=x_aux[index_max]
            x_l=x_aux[index_min]
            x_g=-1
            for i in range(len(x_aux)):
                if not (i == index_min or i == index_max):
                    x_g=x_aux[i]
            
            x_c=centroide(x_l,x_g,2)
            fc=himelblau(x_c[0],x_c[1])
            q1=q(lista[0],lista[1],lista[2],fc,2)
            print("F")
            print(x_l)
    return



gama=1.5
beta=0.5
epsilon=0.001
simplex=main(gama,beta,epsilon)
print(simplex)
