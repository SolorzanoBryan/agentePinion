
# Importacion de librerias para prueba unitarias y las funciones y procedimientos de la clase agente
# from agentePalancaCambio import cambios, resolver
from agentePalancaCambio import palancaCambio
import  unittest 

# Módulos para verificar el tipo de dato que se está validando
#-------------------------
from pickletools import int4
from tokenize import Intnumber, String
from typing import List
#--------------------------

class prueba(unittest.TestCase):
    '''
    Descripción
    ----------
    Clase prueba que permite evaluar las distintas funciones y procedimientos en relación a un escenario planteado.
    
    Parámetros
    ---------
    unittest.TestCase: libreria
        Librería que permite las pruebas de unidad.

    Atributos
    ---------
    No aplica.
    '''
    def setUp(self):
        # Se inicializa un diccionario para los piñones para ejemplificar un escenario propuesto
        pinion = {'uno': 0, 'dos': 0, 'tres': 0, 'cuatro': 0, 'cinco': 0, 'seis': 0, 'siete': 0}
        # Se inicializa un diccionario para los platos para ejemplificar un escenario propuesto
        plato = {'uno': 0, 'dos': 0, 'tres': 0}
        # Se inicializa una variable para la distancia horizontal 
        distancia_horizontal = 1
        # Se inicializa una variable para almacenar las distancias verticales
        distancias_verticales = [] 
        # Se inicializa una variable para las repeticiones requeridas
        repeticiones = 0
        # Se inicializa una variable para el porcentaje de inclinación según la formula planteada
        porcentaje_inclinacion = 0
         # Se inicializa una variable para el porcentaje de inclinación según la formula planteada
        pasado_pin = 0
         # Se inicializa una variable para el porcentaje de inclinación según la formula planteada
        pasado_pla = 0
         # Se inicializa una variable para el porcentaje de inclinación según la formula planteada
        contar = 0
        # Se genera una variable que almacena el resultado de la función "resolver"
        self.agente = palancaCambio(pinion, plato, distancia_horizontal, distancias_verticales, repeticiones)
        self.resolver = self.agente.resolver(porcentaje_inclinacion)
        self.logica = self.agente.logica_absoluta(pasado_pin, pasado_pla, contar)
        pass

    # Procedimeinto para realizar el test del agente
    def test_LatitudVerdadero(self):
        '''
        Descripción
        ----------
        Procedimiento que permite evaluar el funcionamiento de la función "número aleatorio" en un escanario acertado. 
        
        Parámetros
        ---------
        No aplica

        Atributos
        ---------
        No aplica

        Retorna
        -------
        El análisis de la prueba concluye que los resultados por parámetros son equivalentes. 
        '''
        # Se almacena el resultado de la función a evaluar
        resultado = self.agente.obtenerLatitud()
        # Se evalúa si el resultado obtenido es el esperado
        self.assertTrue(resultado, range(0,4))

    # Procedimeinto para realizar el test del agente
    def test_LatitudFalso(self):
        '''
        Descripción
        ----------
        Procedimiento que permite evaluar el funcionamiento de la función "número aleatorio" en un escenario errado. 
        
        Parámetros
        ---------
        No aplica

        Atributos
        ---------
        No aplica

        Retorna
        -------
        El análisis de la prueba concluye que los resultados por parámetros no son equivalentes. 
        '''
         # Se almacena el resultado de la función a evaluar
        resultado = self.agente.obtenerLatitud()
        # Se evalúa si el resultado obtenido no es el esperado
        self.assertNotEqual(resultado , 5)
    # Procedimeinto para realizar el test del agente
    def test_resolverVerdadero(self):
        '''
        Descripción
        ----------
        Procedimiento que permite evaluar el funcionamiento de la función "resolver", referente al costo, en un escenario acertado. 
        
        Parámetros
        ---------
        No aplica

        Atributos
        ---------
        No aplica

        Retorna
        -------
        El análisis de la prueba concluye que los resultados por parámetros son equivalentes. 
        '''      
        # Se evalúa si el resultado es el esperado
        self.assertTrue(self.resolver, {"pinion": "uno", "plato": "tres", "dificultad": 0})
    
    def test_resolverFalso(self):
        '''
        Descripción
        ----------
        Procedimiento que permite evaluar el funcionamiento de la función "resolver", referente al costo, en un escenario errado. 
        
        Parámetros
        ---------
        No aplica

        Atributos
        ---------
        No aplica

        Retorna
        -------
        El análisis de la prueba concluye que los resultados por parámetros no son equivalentes. 
        ''' 
        # Se evalúa si el resultado no es el esperado 
        self.assertNotEqual(self.resolver, {"pinion": "dos", "plato": "tres", "dificultad": 0})

    def test_logicaVerdadero(self):
        '''
        Descripción
        ----------
        Procedimiento que permite evaluar el funcionamiento de la función "logica_total", la parte medular, en un escenario acertado. 
        
        Parámetros
        ---------
        No aplica

        Atributos
        ---------
        No aplica

        Retorna
        -------
        El análisis de la prueba concluye que los resultados por parámetros son equivalentes. 
        '''  
        # Se evalúa si el resultado es el esperado
        self.assertEqual(self.logica, {'distancia_horizontal': Intnumber, 'distancias_verticales': List, 'repeticiones': Intnumber, 'contados': Intnumber})

# Se ejecuta el módulo de la clase
if __name__ == "__main__":
    # Se hace el llamado de todos las pruebas generadas
    unittest.main()