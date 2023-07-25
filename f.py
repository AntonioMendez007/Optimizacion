import math

# Función de evaluación de Himelblau
def himmelblau(x):
    if len(x) < 2:
        raise ValueError("La lista 'x' debe tener al menos dos elementos.")
    
    return (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2

# Algoritmo Golden Section Search
def golden_section_search(a, b, tol=1e-6):
    phi = (1 + math.sqrt(5)) / 2  # Proporción áurea

    # Calcular los puntos iniciales c y d
    c = b - (b - a) / phi
    d = a + (b - a) / phi

    while abs(c - d) > tol:
        if himmelblau([c]) < himmelblau([d]):
            b = d
        else:
            a = c
        
        # Calcular nuevos puntos c y d
        c = b - (b - a) / phi
        d = a + (b - a) / phi
    
    # Devolver el punto medio entre a y b como la mejor aproximación
    return (a + b) / 2

# Ejemplo de uso
a = -5  # Límite inferior
b = 5   # Límite superior

# Aplicar el algoritmo Golden Section Search
resultado = golden_section_search(a, b)

print("El mínimo se encuentra en:", resultado)


