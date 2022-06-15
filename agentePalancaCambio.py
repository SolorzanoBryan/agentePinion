# Agente Palanca de cambio
# Creador: Bryan Alfredo Solórzano Montero
#          Anthony Mauricio Goyes Díaz           

# Planteamiento:  Agente autónomo capaz de determinar los cambios necesarios de los piñones
#  en las bicicletas, facilitando a los principiante ese proceso de adaptación

# Librerias y/o módulos necesarios
from ctypes import FormatError # Importa el módulo que provee compatibilidad con tipos de dato C
from os import system # Importa el módulo que provee una función para  interactuar con el sistema.
import time  # Importa el módulo para manejar tareas relacionadas con el tiempo
import random # Importa el módulo que puede generar números aleatorios.

from modulos import barraProgreso # Importa el módulo para usar el procedimiento de barra de progreso 
class palancaCambio():
    '''
    Descripción: clase Agente
    -------------------------
    El agente, en base a los atributos de la clase, calculará que opción de la palancna de cambio se debe realizar para optimizar el esfuerzo requerido

    Fórmula para calcular el porcentaje de inclinación 
    --------------------------------------------------
    DV = Distancia Vertical
    DH = Distancia Horizontal
    DV/DH x 100 = % de inclinación

    Atributos
    ------------------
        pinion: diccionario 
            Una colección de datos de tipo diccionario.  Tiene como clave una enumeración representando el numero de piñones; sus valores son 0
        plato: diccionario
            Una colección de datos de tipo diccionario. Tiene ocmo clave una enumeración representando la cantidad de platos
        registrar_pinion: Lista
            Una colección de datos de tipo lista. Almacena el diccionario pinion en cada proceso de la función logica_absoluta
        registrar_plato: Lista
            Una colección de datos de tipo lista. Almacena el diccionario plato en cada proceso de la función logica_absoluta
        
    Métodos
    -------
        __init__()
            Constructor de la clase
        logica_absoluta()
            Implementa toda la logica para determinar si el proceso se va d esarrollar en un ambiente de dicultad o no.
            Ademas, aquí hace el llamado a mas funciones.
        cambios(pin_entrada, plato_entrada)
            Recorre los diccionarios pinion y plato, para validar las dos entradas actuales y a esas modificarlas con acción de 1 y al resto con acción 0.
        resolver(porcentaje_inclinacion)
            Procedimiento que evalúa si es necesario un costo para cambiar los piñones de la bicicleta.
        obtenerLatitud()
            Función que retorna un número aletatorio entre 0 y 4 que simular la latitud de un escenario aleatorio. 


    '''

    def __init__(self, pinion, plato, distancia_horizontal, distancias_verticales, repeticiones=1):
        # Variable que almacena el diccionario de los piñones
        self.pinion = pinion
        # Variable que almacena el diccionario de los platos
        self.plato = plato
        # Variable que almacena el valor de la distancia de la ruta
        self.distancia_horizontal = distancia_horizontal
        # Variable que almacena el valor de la altura
        self.distancias_verticales = distancias_verticales
        # Variable que almacena el valor del número de veces a evaluar
        self.repeticiones = repeticiones
        # Variable que almacena los valores de los piñones por ciclo
        self.registrar_pinion = []
        # Variable que almacena los valores de los platos por ciclo
        self.registrar_plato = []
        # Variable que almacena los valores de las distancias por ciclo
        self.distancias_verticales = []


    def logica_absoluta(self, pasado_pin, pasado_pla, contar):
        '''
        Implementa toda la logica para determinar si el proceso se va d esarrollar en un ambiente de dicultad o no, ademas, aquí hace el llamado a mas funciones.

        Variables 
        ---------
            distancia_horizontal: decimales
                Valor dado en metros por el usuario que decidira cada cuanto tiempo quiere que se hagan los cambios y análisis del ambiente.
            repeticiones: entero
                El usuario asignará cuantos tramos de distancia_horizontal podria considerar en su ruta.
            distancias_verticales: lista
                Almacenara todas los metros generados de manera aleatoria dadas por la función obtenerLatitud().
        
        Retorna
        ------
            Un diccionario de la distancia horizontal, vertical y el numero de repeticiones de cada tramo.

        '''
        # Permite repetir el proceso en relación a la cantidad de repeticiones
        for num in range(0, self.repeticiones):
            '''
            Variables para el ciclo
            ------------------
                vertical: decimal
                    Almacena el resultado de la función obtenerLatitud(). Usada para hacer el calculo del porcentaje de dificultad.
                porcentaje_inclinacion: entero
                    Almacena el resultado de la operación que retorna el porcentaje de dificultad explicada.
                resultado_comparativa: diccionario
                    Almacena un diccionaria que contiene el piñon, plato y la dificultad presente en este ciclo.
                pin: cadena de texto
                    Clave o llave que identifica al piñon.
                dificultad: booleana
                    Determinada si la inclinación es pronunciada o no (mayor a 4 metros).
            '''
            # Almacena un valor aleatorio como la altura vertical
            altura_vertical = self.obtenerLatitud()
            # Almacena el resultado del cálculo del porcentaje de inclinación
            porcentaje_inclinacion = round((altura_vertical/self.distancia_horizontal) * 100)
            # Almacena los posibles cambios en los piñones y/o platos
            resultado_comparatoria = self.resolver(porcentaje_inclinacion)
            # Almacena los piñones en relación a la clave del dicionario retornado
            pin = resultado_comparatoria.get('pinion')
            # Almacena los platos en relación a la clave del diccionario retornado
            pla = resultado_comparatoria.get('plato')
            # Almacena las dificultados en relación a la clave del dicionario retornado
            dificultad = resultado_comparatoria.get('dificultad')
            # llamado al método para la validación de esfuerzo
            self.cambios(pin, pla)
            # Si la ubicación de los piñones entre la actual y la anterior son iguales realiza esfuerzo, caso contrario, no
            if not pasado_pin == pin:
                contar = contar + 1
            # Si la ubicación de los piñones entre la actual y la anterior son iguales realiza esfuerzo, caso contrario, no
            if not pasado_pla == pla:
                contar = contar + 1
            # Se actualizan los valoers a presentar
            pasado_pin = pin
            pasado_pla = pla
            # Estas tres líneas son necesarias para ir registrando los estados de los pinñones, platos y datos de las vertices en cada tramo
            self.registrar_pinion.append(self.pinion.copy())
            self.registrar_plato.append(self.plato.copy())
            self.distancias_verticales.append(altura_vertical)
            # Se procede con el proceso de validación para mostrar la información necesario al usuario
            if dificultad == 1:
                print('-------------------------------------------------------------------------------------------------')
                print(f'En estos {self.distancia_horizontal} metros su grado de dificulad sera del {porcentaje_inclinacion}%.')
                print(f'La combinación sera el piñon {pin} y el plato {pla}.')
                print('En este proceso si representa cualquier problema hasta para un ciclista con experiencia.')
                print('-------------------------------------------------------------------------------------------------\n')
            else:
                print('-------------------------------------------------------------------------------------------------')
                print(f'En estos {self.distancia_horizontal} metros su grado de dificulad sera del {porcentaje_inclinacion}%.')
                print(f'La combinación sera el piñon {pin} y el plato {pla}.')
                print('Este proceso no representa mucho esfuerzo para las personas en general.')
                print('-------------------------------------------------------------------------------------------------\n')

            time.sleep(4) # Un tiempo de cuatro segundos simulando un recorrido hecho
        return {'distancia_horizontal': self.distancia_horizontal, 'distancias_verticales': self.distancias_verticales, 'repeticiones': self.repeticiones, 'contados': contar}



    def cambios(self, pin_entrada, plato_entrada):
        '''
        Descripción
        -----------
        Recorre los diccionarios pinion y plato, para validar las dos entradas actuales para modificarlas con acción 1, o por el contrario, 0.

        Parámetros
        ----------
        pin_entrada: cadena de texto
            Representa, en letras, el piñon al cual se tamara en cuenta para el cambio.
        plato_entrada: cadena de texto
            Representa, en letras, el plato al cual se tamara en cuenta para el cambio.
        
        Retorna
        -------
        Procedimiento que no retorna nada.
        '''
        # Evalúa 
        for pin in self.pinion:
            if pin == pin_entrada:
                self.pinion[pin] = 1
            else:
                self.pinion[pin] = 0

        for pla in self.plato:
            if pla == plato_entrada:
                self.plato[pla] = 1
            else:
                self.plato[pla] = 0

    def resolver(self, porcentaje_inclinacion):
        '''
        Descripción
        -----------
        Genera un diccionario con los las claves y valores de los piñones y platos respectivamente. Determina que piñón o plato debe ser cambiado

        Atributos
        ---------
        porcentaje_inclinacion: entero
            Dato para determinar a que proceso de analisis será llevado y así devolver un resultado con información precisa.

        Retorna
        -------
        Función que retorna un diccionario con los las siguiente claves:
            pinion: cadena de texto
                Número de piñon en letras que se aplicará en el nuevo tramo
            plato: cadena de texto
                Numéro de plato en letras que se aplicará en el nuevo tramo del ciclista.
            dificultad: booleana
                Un dato para facilitar en el proceso de la logica y mostrar información pertinente o clasificada
        '''
        # Se presentan las estructuras de control anidadas que permiten evaluar que cambio tiene que realizar el agente
        # Si el esfuerzo es igual a cero retorna un diccionario único
        if porcentaje_inclinacion == 0:
            return {"pinion": "uno", "plato": "tres", "dificultad": 0}
        else:
            # Si el esfuerzo es menor o igual a tres retorna un diccionario único
            if porcentaje_inclinacion <= 3:
                return {"pinion": "dos", "plato": "tres", "dificultad": 0}
            else:
                # Si el esfuerzo es menor o igual a 6 retorna un diccionario único
                if porcentaje_inclinacion <= 6:
                    return {"pinion": "tres", "plato": "dos", "dificultad": 0}
                else:
                    # Si el esfuerzo es menor o igual a 9 retorna un diccionario único
                    if porcentaje_inclinacion <= 9:
                        return {"pinion": "cuatro", "plato": "dos", "dificultad": 1}
                    else:
                        # Si el esfuerzo es menor o igual a 15retorna un diccionario único
                        if porcentaje_inclinacion <= 15:
                            # Si el esfuerzo es menor a 13 retorna un diccionario único
                            if porcentaje_inclinacion < 13:
                                return {"pinion": "cinco", "plato": "dos", "dificultad": 1}
                            else:
                                return {"pinion": "seis", "plato": "uno", "dificultad": 1}
                        else:
                            return {"pinion": "siete", "plato": "uno", "dificultad": 1}    


    def obtenerLatitud(self):
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
            Función que retorna un número aleatorio entre 0 y 4 redondeado a dos decimales. Representa la latitud del campo
        '''
        # Se genera un número aleatorio uniforme entre 0 y 4
        numero = random.uniform(0,4)
        # Retorna o devuelve el  resultado del número aleatorio redondeado a 2 decimales
        return round(numero, 2)

# Ejecución de los métodos de la clase propuesta
if __name__ == "__main__":

    # Se inicializa el diccionario de piñones
    pinion = {'uno': 0, 'dos': 0, 'tres': 0, 'cuatro': 0, 'cinco': 0, 'seis': 0, 'siete': 0}
    # Se inicializa el diccionario de platos
    plato = {'uno': 0, 'dos': 0, 'tres': 0}
    # Se inicializa la lista de piñones
    registrar_pinion = []
    # Se inicializa la lista de platos
    registrar_plato = []

    # # Se inicializa las variables para las distancias tanto para el eje x como y
    distancia_horizontal = 0
    distancias_verticales = []

    # Se inicializa las variables para el esfuerzo y los piños individuales
    contar = 0
    pasado_pin = 0
    pasado_pla = 0


     # Las siguientes líneas de código, hasta el while, permiten dar una mejor apariencia al agente implementado.
    system("cls") # Borra toda la información que sale en consola
    for i in barraProgreso(range(10), "Cargando: ", 20): # Inicializa el temporizador
        time.sleep(0.2) # Pausa la ejeución por 0.2 segundos
        # Se limpia la pantalla
        system("cls")
    # Se imprime un mensaje de bienvenida
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

    # Se muestra información puntal de lo que se espera del usuario
    print('Nota: Los valores que ingresará a continuación tienen un límite superior de hasta 50 tanto para enteros como decimales')
    while(True):
        # Se capturan las excepciones para el tipo de dato ingresado y que no sea nulo
        try:
            # Se caputra la distancia de la ruta a evaluar
            distancia_horizontal = float(input("Introduzca cada cuantos metros desea que se haga el escaneo del ambiente para poder hacer los cambios a los piñones: "))
        # Se captura la excepción del tipo de valor
        except ValueError:
            # Se imprime en mensaje en base al error propuesto    
            print("¡Vaya! Se esperaba un número decimal. Intente de nuevo...")
        # if (distancia_horizontal<=50):
        else:
            # Se evalúa si el valor ingresado es mayor a 50 
            if(distancia_horizontal>50):
                # Se menciona al usuario que el valor ingresado excede el límite permitido
                print('Límite permitido para la distancia horizontal: 50\nColocando el valor máximo permitido...')
                # Se reajusta a el valor máximo permitido
                distancia_horizontal=50
                time.sleep(3)
            try:
                # Se caputra la cantidad de repeticiones a evaluar
                repeticiones = int(input(f"Introduzca la cantidad de repeticiones de {distancia_horizontal} metros: "))
            # Se captura la excepción del tipo de valor
            except ValueError:
                # Se imprime en mensaje en base al error propuesto    
                print("¡Vaya! Se esperaba un número entero. Intente de nuevo...")
            else:
                # Se evalúa si el valor ingresado es mayor a 50 
                if(repeticiones>50):
                    # Se menciona al usuario que el valor ingresado excede el límite permitido
                    print('Límite permitido para las repeticiones: 50\nColocando el valor máximo permitido...')
                    # Se reajusta a el valor máximo permitido
                    repeticiones=50
                    time.sleep(3)
                break
    
    # Se instancia la clase del agente con los valores iniciales
    agente = palancaCambio(pinion, plato, distancia_horizontal, distancias_verticales, repeticiones)
    # Se llama al método medular de la clase
    resultado = agente.logica_absoluta(pasado_pin, pasado_pla, contar) # Unica llamada al proceso completo

    # Se captura los valores en relación a la clave del diccionario retornada anteriormente
    # Se captura la distancia horizontal
    metros = resultado['distancia_horizontal']
    # Se captura el recorrido
    recorrido = resultado['distancias_verticales']
    # Se captura el fuerzo requerido
    contados = resultado['contados']
    # Se captura las repeticiones necesarias
    repeticiones = resultado['repeticiones']

    # Se imprime el valor del costo
    print(f'Total del costo de acción: {contados}')
    # Se imprime el valor de las repeticiones
    print(f'Usted a recorrido un total de {repeticiones} metros y se pudo completar las sigueintes metricas')
    print('En los piñones tenemos: ')
    # Se imprime los movimientos requeridos de los piñones
    for pin in registrar_pinion:
        print(pin)
    print('En los platos tenemos: ')
    # Se imprime los movimientos requeridos de los platos
    for pla in registrar_plato:
        print(pla)



    