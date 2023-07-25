#Funcion de ejercicio
def funcion(x):
  if(x==0):
    resultado = float('inf')
  else:
    resultado =pow(x,2)+ (54/x)

  return resultado

#Funcion para los numeros de fibonacci
def fibonacci(n):
  if n < 2:
    return n
  return fibonacci(n-1) + fibonacci(n-2)

#Funcion para hacer el calculo
a = float(input("Digite el valor de a: "))
b = float(input("Digite el valor de b: "))
n = float(input("Digite el valor de n: "))
L = b - a
k = 2
ronda = 0

while(k != n):
    ronda = ronda + 1
    print("Ronda: ",ronda)
    
    numerador = ((n - k) + 1)+1
    denominador = n + 1
    Lk = (fibonacci(numerador)/fibonacci(denominador)) * L
    print("LK: ",Lk)
    
    x1 = a + Lk
    x2 = b - Lk
    print("Valor de xa: ",x1)
    print("Valor de xb: ",x2)
    
    fx1 = funcion(x1)
    fx2 = funcion(x2)
    print("Valor de Fxa: ",fx1)
    print("Valor de Fxb: ",fx2)
    
    if (fx1 > fx2):
      a = x1
      b = b
      if (k == n):
        print("El minimo esta en: ",a,",",b)
      else:
        k = k + 1

    elif (fx1 < fx2):
        a = a
        b = x2
        if ( k == n):
            print("El minimo esta en: ",a,",",b)
        else:
            k = k + 1
    
    elif (fx1 == fx2):
          a = x1
          b = x2
          if ( k == n):
            print("El minimo esta en: ",a,",",b)
          else:
            k = k + 1
    else:
       break