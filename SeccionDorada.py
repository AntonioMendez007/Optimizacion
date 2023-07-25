import math

'''
def fun(x):
    if(x==0):
        return float('inf')
    else:
        resultado=pow(x,2)+(54/x)
    return resultado
'''
def fun(x):
    if(x==0):
        return float('inf')
    else:
        resultado=pow(x,2)+(4)
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
        f_w1=25*(pow(w1,2))+(54/((5)*(w1)))
        f_w2=25*(pow(w2,2))+(54/((5)*(w2)))
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
                print(f'El minimo esta en {a_w,b_w} = {a_w*5,b_w*5}')
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
                print(f'El minimo esta en {a_w,b_w} = {a_w*5,b_w*5}')
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
            print("El minimo esta en: ",a_w,",",b_w, "= ", a_w*5,", ",b_w*5)
            repetir=False
          else:
            k = k + 1

dorada(-2,2,pow(10,-3))
print()
