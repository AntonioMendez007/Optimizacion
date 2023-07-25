def fun(x):
    if(x==0):
        return float('inf')
    else:
        resultado=pow(x,2)+(54/x)
    return resultado

   
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

    


def sec(a,b,e):
    f_a=f_prima(a)
    f_b=f_prima(b)
    print(f'f(a): {f_a}')
    print(f'f(b): {f_b}')
    if (f_a < 0 or f_b > 0):
        print("Se cumple la condición")
    else:
        print('Da nuevos valores de a o b')
        

    x1=a
    x2=b

    repetir=True
    iteraciones=0
    while(repetir):
        iteraciones=iteraciones+1
        print(f'Iteracion: {iteraciones}')
        z=x2 - ( f_prima(x2) /( ( f_prima(x2) - f_prima(x1) ) / (x2-x1) ) )
        f_z=f_prima(z)
        print(f'z: {z}')
        print(f'f_z: {f_z}')

        if abs(f_prima(z)) <= e:
            print(f'El intervalo esta en: {x1,x2}')
            repetir=False
        elif (f_prima(z)<0):
            x1=z
        elif (f_prima(z)>0):
            x2=z

sec(2,5,pow(10,-3))
print()