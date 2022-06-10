# Agente Piñon
# Creador: Bryan Alfredo Solórzano Montero
#          Anthony Mauricio Goyes Díaz           

# Planteamiento:  Agente autónomo capaz de determinar los cambios necesarios de los piñones
#  en las bicicletas, facilitando a los principiante ese proceso de adaptación

# Librerias necesarias
from ctypes import FormatError # Importa el módulo que provee compatibilidad con tipos de dato C
from os import system # Importa el módulo que provee una función para  interactuar con el sistema.
import sys # Importa el módulo para manejar exepciones personalizadas 
import time  # Importa el módulo para manejar tareas relacionadas con el tiempo
import random # Importa el módulo que puede generar números aleatorios.

def barraProgreso(it, prefijo="", size=60, archivo=sys.stdout):
    contador = len(it)
    def show(j):
        x = int(size*j/contador)
        archivo.write("%s[%s%s] %i/%i\r" % (prefijo, "-"*x, "."*(size-x), j, contador))
        archivo.flush()
        archivo.write("\n")
    show(0)
    for i, objeto in enumerate(it):
        yield objeto
        show(i+1)
        archivo.write("\n")
    archivo.flush()

'''
Agente
------
El agente sera capaz de detectar 7 tipo de procentalidad para inclinación

Varaibles Globales
------------------
    pinion: diccionario 
        Una colección de datos de tipo diccionario.  Tiene como clave una enumeración representando el numero de piñones; sus valores son 0
    plato: diccionario
        Una colección de datos de tipo diccionario. Tiene ocmo clave una enumeración representando la cantidad de platos
    registrar_pinion: Lista
        Una colección de datos de tipo lista. Almacena el diccionario pinion en cada proceso de la función logica_absoluta
    registrar_plato: Lista
        Una colección de datos de tipo lista. Almacena el diccionario plato en cada proceso de la función logica_absoluta
    
Funciones
-------
    logica_absoluta()
        Implementa toda la logica para determinar si el proceso se va d esarrollar en un ambiente de dicultad o no.
        Ademas, aquí hace el llamado a mas funciones.
    verticalRandom()
        Asigna un valor aleatorio comprendido entre sus dos parametros  y lo trunca con 2 decimales.
    cambios(pin_entrada, plato_entrada)
        Recorre los diccionarios pinion y plato, para validar las dos entradas actuales y a esas modificarlas con acción de 1 y al resto con acción 0.

'''

pinion = {'uno': 0, 'dos': 0, 'tres': 0, 'cuatro': 0, 'cinco': 0, 'seis': 0, 'siete': 0}
plato = {'uno': 0, 'dos': 0, 'tres': 0}
registrar_pinion = []
registrar_plato = []

'''
    Fórmula para calcular el porcentaje de inclinación 
    DV = Distancia Vertical
    DH = Distancia Horizontal
    DV/DH x 100 = % de inclinación
'''

def logica_absoluta():
    '''
    Implementa toda la logica para determinar si el proceso se va d esarrollar en un ambiente de dicultad o no, ademas, aquí hace el llamado a mas funciones.

    Variables 
    ---------
        distancia_horizontal: decimales
            Valor dado en metros por el usuario que decidira cada cuanto tiempo quiere que se hagan los cambios y análisis del ambiente.
        repeticiones: entero
            El usuario asignará cuantos tramos de distancia_horizontal podria considerar en su ruta.
        distancias_verticales: lista
            Almacenara todas los metros generados de manera aleatoria dadas por la función verticalRandom().
    
    Retorna
    ------
        Un diccionario de la distancia horizontal, vertical y el numero de repeticiones de cada tramo.

    '''
    # Las siguientes líneas de código, hasta el while, permiten dar una mejor apariencia al agente implementado.
    system("cls") # Borra toda la información que sale en consola
    for i in barraProgreso(range(10), "Cargando: ", 20): # Inicializa el temporizador
        time.sleep(0.2) # Pausa la ejeución por 0.2 segundos
        system("cls")
    print("""
        »»————-　¡El agente se ha iniciado correctamente! 　————-««
        """)
    time.sleep(2)
    system("cls")
    print("""
                    ╔═══════════════════════════════════╗ 
                    ║           Agente Piñon            ║ 
                    ╚═══════════════════════════════════╝     
        """)
    print('Nota: Los valores que ingresará a continuación tienen un límite superior de hasta 50 tanto para enteros como decimales')
    while(True):
        try:
            distancia_horizontal = float(input("Introduzca cada cuantos metros desea que se haga el escaneo del ambiente para poder hacer los cambios a los piñones: "))
        except ValueError:
                print("¡Vaya! Se esperaba un número decimal. Intente de nuevo...")
        # if (distancia_horizontal<=50):
        else:
            try:
                repeticiones = int(input(f"Introduzca la cantidad de repeticiones de {distancia_horizontal} metros: "))
            except ValueError:
                print("¡Vaya! Se esperaba un número entero. Intente de nuevo...")
            else:
                break   
    if(distancia_horizontal>50):
        print('Límite permitido para la distancia horizontal: 50\nColocando valor máximo posible...')
        distancia_horizontal=50
        time.sleep(3)
    elif(repeticiones>50):
        print('Límite permitido para las repeticiones: 50\nColocando valor máximo posible...')
        repeticiones=50
        time.sleep(3)

    distancias_verticales = []
    for num in range(0, repeticiones):
        '''
        Variables locales
        ------------------
            vertical: decimal
                Almacena el resultado de la función verticalRandom(). Usada para hacer el calculo del porcentaje de dificultad.
            porcentaje_inclinacion: entero
                Almacena el resultado de la operación que retorna el porcentaje de dificultad explicada.
            resultado_comparativa: diccionario
                Almacena un diccionaria que contiene el piñon, plato y la dificultad presente en este ciclo.
            pin: cadena de texto
                Clave o llave que identifica al piñon.
            dificultad: booleana
                Determinada si la inclinación es pronunciada o no (mayor a 4 metros).
        '''
        vertical = verticalRandom()
        porcentaje_inclinacion = round((vertical/distancia_horizontal) * 100)
        
        resultado_comparatoria = resolver(porcentaje_inclinacion)
        pin = resultado_comparatoria.get('pinion')
        pla = resultado_comparatoria.get('plato')
        dificultad = resultado_comparatoria.get('dificultad')
        print(pin, pla, dificultad)
        cambios(pin, pla)
        print(pinion)
        print(plato)
        # Estas tres líneas son necesarias para ir registrando los estados de los pinñones, platos y datos de las vertices en cada tramo
        registrar_pinion.append(pinion.copy())
        registrar_plato.append(plato.copy())
        distancias_verticales.append(vertical)
        # Se procede con el proceso de validación para mostrar la información necesario al usuario
        if dificultad == 1:
            print('-------------------------------------------------------------------------------------------------')
            print(f'En estos {distancia_horizontal} metros su grado de dificulad sera del {porcentaje_inclinacion}%.')
            print(f'La combinación sera el piñon {pin} y el plato {pla}.')
            print('En este proceso si representa cualquier problema hasta para un ciclista con experiencia.')
            print('-------------------------------------------------------------------------------------------------\n')
        else:
            print('-------------------------------------------------------------------------------------------------')
            print(f'En estos {distancia_horizontal} metros su grado de dificulad sera del {porcentaje_inclinacion}%.')
            print(f'La combinación sera el piñon {pin} y el plato {pla}.')
            print('Este proceso no representa mucho esfuerzo para las personas en general.')
            print('-------------------------------------------------------------------------------------------------\n')

        time.sleep(4) # Pausa la ejecución durante cuatro segundos simulando un recorrido hecho
    return {'distancia_horizontal': distancia_horizontal, 'distancias_verticales': distancias_verticales, 'repeticiones': repeticiones}

def verticalRandom():
    '''
    Descripción
    ----------
    Asigna un valor aleatorio comprendido entre sus dos parametros  y lo trunca con 2 decimales.

    Variable local
    --------
    numero: decimal
        Se llama al módulo "random" para aplicarle el metodo "uniform", el cual devulve un número de forma aleatoria comprendido entre sus dos parametros.
    
    Retorna
    -------
        Un número aleatorio redondeado a dos decimales.
    '''
    numero = random.uniform(0,4)
    return round(numero, 2)

def cambios(pin_entrada, plato_entrada):
    '''
    Descripción
    -----------
    Recorre los diccionarios pinion y plato, para validar las dos entradas actuales y a esas modificarlas con acción de 1 y al resto con acción 0.

    Parámetros
    ----------
    pin_entrada: cadena de texto
        Representa, en letras, el piñon al cual se tamara en cuenta para el cambio.
    plato_entrada: cadena de texto
        Representa, en letras, el plato al cual se tamara en cuenta para el cambio.
    '''
    for pin in pinion:
        if pin == pin_entrada:
            pinion[pin] = 1
        else:
            pinion[pin] = 0
    for pla in plato:
        if pla == plato_entrada:
            plato[pla] = 1
        else:
            plato[pla] = 0

def resolver(porcentaje_inclinacion):
    '''
    Descripción
    -----------
    Genera un diccionario con los las claves y valores de los piñones y platos respectivamente.

    Atributos
    ---------
    porcentaje_inclinacion: entero
        Dato para determinar a que proceso de analisis será llevado y así devolver un resultado con información precisa.

    Retorna
    -------
        Un diccionario con los las siguiente claves:
            pinion: cadena de texto
                Número de piñon en letras que se aplicará en el nuevo tramo
            plato: cadena de texto
                Numéro de plato en letras que se aplicará en el nuevo tramo del ciclista.
            dificultad: booleana
                Un dato para facilitar en el proceso de la logica y mostrar información pertinente o clasificada
    '''

    if porcentaje_inclinacion == 0:
        return {"pinion": "uno", "plato": "tres", "dificultad": 0}
    else:
        if porcentaje_inclinacion <= 3:
            return {"pinion": "dos", "plato": "tres", "dificultad": 0}
        else:
            if porcentaje_inclinacion <= 6:
                return {"pinion": "tres", "plato": "dos", "dificultad": 0}
            else:
                if porcentaje_inclinacion <= 9:
                    return {"pinion": "cuatro", "plato": "dos", "dificultad": 1}
                else:
                    if porcentaje_inclinacion <= 15:
                        if porcentaje_inclinacion < 13:
                            return {"pinion": "cinco", "plato": "dos", "dificultad": 1}
                        else:
                            return {"pinion": "seis", "plato": "uno", "dificultad": 1}
                    else:
                        return {"pinion": "siete", "plato": "uno", "dificultad": 1}


resultado = logica_absoluta() # Unica llamada al proceso completo
metros = resultado['distancia_horizontal']
recorrido = resultado['distancias_verticales']
total = metros * len(recorrido)
print(f'Usted a recorrido un total de {total} metros y se pudo completar las sigueintes metricas')
print('En los piñones tenemos: ')
for pin in registrar_pinion:
    print(pin)
print('En los platos tenemos: ')
for pla in registrar_plato:
    print(pla)
# {'distancia_horizontal': distancia_horizontal, 'distancias_verticales': distancias_verticales, 'repeticiones': repeticiones}



