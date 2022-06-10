# Agente Piñon
# Creador: Bryan Alfredo Solórzano Montero
#          Anthony Mauricio Goyes Díaz           

# Planteamiento:  Agente autónomo capaz de determinar los cambios necesarios de los piñones
#  en las bicicletas, facilitando a los principiante ese proceso de adaptación

# Librerias necesarias
import time  # Importa el módulo para manejar tareas relacionadas con el tiempo
import random # Importa el módulo que puede generar números aleatorios. 

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
    logica_absoluta:
        Implementa toda la logica para determinar si el proceso se va d esarrollar en un ambiente de dicultad o no.
        Ademas, aquí hace el llamado a mas funciones.
'''

pinion = {'uno': 0, 'dos': 0, 'tres': 0, 'cuatro': 0, 'cinco': 0, 'seis': 0, 'siete': 0}
plato = {'uno': 0, 'dos': 0, 'tres': 0}
registrar_pinion = []
registrar_plato = []

'''
    FORMULA PARA calcular el porcentaje de inclinación 
    DV = Distancia Verticar
    DH = Distancia Horizontal
    DV/DH x 100 = % de inclinación
'''

def logica_absoluta():
    '''
    Implementa toda la logica para determinar si el proceso se va d esarrollar en un ambiente de dicultad o no
    Ademas, aquí hace el llamado a mas funciones.

    Variables 
    ---------
        distancia_horizontal: decimales
            Valor dado en metros por el usuario que decidira cada cuanto tiempo quiere que se hagan los cambios y análisis del ambiente  
        repeticiones: entero
            El usuario asignará cuantos tramos de distancia_horizontal podria considerar en su ruta
        distancias_verticales: lista
            Almacenara todas los metros generados de manera aleatoria dadas por la función verticalRandom 
    
    retorna
        Un diccionario de la distancia horizontal, vertical y el numero de repeticiones de cada tramo 

    '''
    while(True):
        try:
            distancia_horizontal = float(input("Introduzca cada cuantos metros desea que se haga el escaneo del ambiente para poder hacer los cambios a los piñones: ") )
            try:
                repeticiones = int(input(f"Introduzca la cantidad de repeticiones de {distancia_horizontal} metros: "))
            except ValueError:
                print("¡Vaya! El dato ingresado no es el esperado. Se esperaba un número entero. Intente de nuevo...")
        except ValueError:
                print("¡Vaya! El dato ingresado no es el esperado. Se esperaba un número decimal. Intente de nuevo...")
        except:
            print("¡Vaya! Ha ocurrido un error inesperado.  Intente de nuevo...")
        finally:
            break

    distancias_verticales = []
    for num in range(0, repeticiones):
        '''
        variables internas
        ------------------
            vertical (float): almacena resultado de la función verticalRandom(). Esta variable es necesario para hacer el calculo del porcentaje de dificultad
            porcentaje_inclinación (int): Almacena el resutlado de la operación explicada antes de entrar a la función
            resultado_comparativa (diccionary): almacena un diccionaria que almacena el piñon, plato y dificultad presente en este ciclo
            pin (str): Extra de resultado_comparativa la clave necesario para identificar al piñon
            dificultad (boolean): determinada para saber si es grande el grado de inclinación o no 
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
        # Se procede con el proceso de validación para mostrar la ifnromación necesario al usuario
        if dificultad == 1:
            print(f'En estos {distancia_horizontal} metros su grado de dificulad sera del {porcentaje_inclinacion} %')
            print(f'La combinación sera el piñon {pin} y el plato {pla}')
            print('En este proceso si representa cualquier problema hasta para un ciclista con experiencia')
        else:
            print(f'En estos {distancia_horizontal} metros su grado de dificulad sera del {porcentaje_inclinacion} %')
            print(f'La combinación sera el piñon {pin} y el plato {pla}')
            print('Este proceso no representa mucho esfuerzo para las personas en general')

        time.sleep(4) # Un tiempo de cuatro segundos simulando un recorrido hecho
    return {'distancia_horizontal': distancia_horizontal, 'distancias_verticales': distancias_verticales, 'repeticiones': repeticiones}

def verticalRandom():
    '''
    variable
    --------
        num (floa): se llama al objeto random para aplicarle el metodo uniform, el cual devulve un nuemro aleatoriamente comprendido entre sus dos parametros
    retorna
    -------
        Ese numero pero redondeado para que solo tenda dos decimales
    '''
    num = random.uniform(0,4)
    return round(num, 2)

def cambios(pin_entrada, plato_entrada):
    '''
    parametros
    ----------
        pin_entrada (str): En letras el piñon al cual se tamara en cuenta para el cambio
        plato_entrada (str): En letras el plato al cual se tamara en cuenta para el cambio
        
    No retorna nada pero si hace recorrido a los diccionarios pinion y plato, 
    para validar las dos entradas actuales y a esas modificarlas con acción de 1
    y al resto con acción 0, es decir no haran parte del pequeño tramo del ciclista
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
    parametro
    ---------
        porcentaje_inclinacion(int): es un dato para determinar a que proceso de analisis sera llevado y así devolver un resultado con información precisa

    retorna
    -------
        Un diccionario con los las siguiente claves:
            pinion (str): saber a que numero de piñon en letras se le aplicara en el nuevo tramo
            plato (str): saber a que numéro de plato en letras se aplicara en el nuevo tramo del ciclista
            dificultad (boolean): Un dato para facilitar en el proceso de la logica y mostrar información pertinente o clasificada
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



