import random
'''
def cajanegra(entrada):
    secreta = "holamundo"
    puntuacion = 0
    for i in range(len(secreta)):
        puntuacion += 1 if  secreta[i] == entrada[i] else 0
    return puntuacion/len(secreta)

def mono(longitud):
    palabra = ""
    for _ in range(longitud):
        # 97,122 letras minusculas (aski)
        palabra += chr(random.randint(97,122))
    return palabra

g = 0
while(True):
    palabra = mono(9)
    puntuacion = cajanegra(palabra)
    print(g, palabra, puntuacion)
    if puntuacion == 1:
        break
    g+= 1
'''

# --------------------------------------------------cambio-------------------------------------------------------------------
def evaluar(original,individuo):
    puntuacion = 0
    for i in range(len(original)):
        puntuacion += 1 if  original[i] == individuo[i] else 0
    return puntuacion/len(original)

def generar_individuo(longitud):
    palabra = ""
    for _ in range(longitud):
        # 97,122 letras minusculas (aski)
        palabra += chr(random.randint(97,122))
    return palabra

def cruza(cadena1, cadena2):
    punto_cruza = random.randint(0, len(cadena1))
    cadena_hijo1 = cadena1[0:punto_cruza] + cadena2[punto_cruza:]
    cadena_hijo2 = cadena2[0:punto_cruza] + cadena1[punto_cruza:]
    return cadena_hijo1, cadena_hijo2

def mutacion(cadena, prob_mutar):
    cadena_mutada = list(cadena)
    for i in range(len(cadena)):
        cadena_mutada[i] = chr(random.randint(97, 122)) \
        if random.random() < prob_mutar else cadena_mutada[i]
    return "".join(cadena_mutada)

def crear_poblacion(tamaño,original):
    poblacion = []
    for _ in range(tamaño):
        palabra = generar_individuo(len(original))
        poblacion.append(
            {
            "cadena": palabra,
            "aptitud": evaluar(original, palabra)
            }
        )
    return poblacion

def seleccion_padres(poblacion):
    padres = []
    while len(padres) < len(poblacion):
        for individuo in poblacion:
            fit = 0.1 if individuo['aptitud'] == 0 else individuo['aptitud']
            if random.random() < fit:
                padres.append(individuo)
    return padres

def estadisticas(poblacion):
    mejor = poblacion[0]
    peor = poblacion[0]
    suma_fit = 0
    for individuo in poblacion:
        mejor = individuo if individuo['aptitud'] >= mejor['aptitud'] else mejor
        peor = individuo if individuo['aptitud'] >= peor['aptitud'] else peor
        suma_fit += individuo['aptitud']
    return mejor, peor, suma_fit/len(poblacion)

prob_cruza = 1.0
prob_mutar = 0.1
generaciones = 100
tam_pob = 500
objetivo = "mojarlaanguila"
poblacion = crear_poblacion(tam_pob,objetivo)
for g in range(generaciones):
    mejor, peor, prom_fit = estadisticas(poblacion)
    print("{:.0f} {} {:.2f} {:.2f}".format(g, mejor['cadena'], mejor['aptitud'], prom_fit))
    if(mejor['aptitud']== 1):
       break
    padres = seleccion_padres(poblacion)

    siguiente_generacion = []
    for p in range(0,tam_pob,2):
        hijo1 = {}
        hijo2 = {}
        if random.random() < prob_cruza:
            cadena_hijo1, cadena_hijo2 = cruza(padres[p]['cadena'], padres[p+1]['cadena'])
            hijo1 = {"cadena": cadena_hijo1, "aptitud":0}
            hijo2 = {"cadena": cadena_hijo2, "aptitud":0}
        else:
            hijo1 = padres[p]
            hijo2 = padres[p+1]
        hijo1['cadena'] = mutacion(hijo1['cadena'], prob_mutar)
        hijo2['cadena'] = mutacion(hijo2['cadena'], prob_mutar)
        hijo1['aptitud'] = evaluar(objetivo, hijo1['cadena'])
        hijo2['aptitud'] = evaluar(objetivo, hijo2['cadena'])
        siguiente_generacion.append(hijo1)
        siguiente_generacion.append(hijo2)
    poblacion = siguiente_generacion
    poblacion[0] = mejor

print(estadisticas(poblacion))


#print(estadisticas(crear_poblacion(10,"hola")))
#print(seleccion_padres(crear_poblacion(10,"hola")))
#print(crear_poblacion(100,"pedro"))
#print(mutacion("hola",0.9))
#print(cruza("pedro","pablo"))

else:
            print("No es factible")
            r_1 = random.uniform(-0.5, 0.5)
            r_2 = random.uniform(-0.5, 0.5)
            print(f'r1: {r_1}')
            print(f'r2: {r_2}')
            x_1 = np.array([ x_0[0] + (r_1*z_0[0]), x_0[1] + (r_2*z_0[1]) ])
            print(f'x_1: {x_1}')
            # Paso 3
            g1x = 26 -(x_1[1]-5)**2 - (x_1[1]**2)
            g2x = 20 - (4*x_1[0]) - x_1[1]
            if g1x >= 0 and g2x >= 0:
                print("El punto es factible")
                for i in range(3):
                    equis_1.append(x_1)
                    f_x1 = himelblau(x_1[0], x_1[1])
                    print(f'f_x1: {f_x1}')
                    funcion.append(f_x1)
                    print(f'funcion: {funcion}')
                    
                    r_1 = random.uniform(-0.5, 0.5)
                    r_2 = random.uniform(-0.5, 0.5)
                    print(f'r1: {r_1}')
                    print(f'r2: {r_2}')
                    x_1 = np.array([ x_0[0] + (r_1*z_0[0]), x_0[1] + (r_2*z_0[1]) ])
                    g1x = 26 -(x_1[1]-5)**2 - (x_1[1]**2)
                    g2x = 20 - (4*x_1[0]) - x_1[1]
                    print(f'g1x: {g1x}')
                    print(f'g2x: {g2x}')
                    
                    pe = pe + 1
                #print(f'pe: {pe}')
                minimo_puntos = np.min(equis_1)
                minimo_funcion = np.min(funcion)
                print(f'minimo de la funcion: {minimo_funcion}')
                pe = 1



