
import sys # Importa el módulo para manejar exepciones personalizadas 

import random # Importa el módulo que puede generar números aleatorios.

def barraProgreso(it, prefijo="", size=60, archivo=sys.stdout):
    contador = len(it)
    def mostrar(j):
        x = int(size*j/contador)
        archivo.write("%s[%s%s] %i/%i\r" % (prefijo, "-"*x, "."*(size-x), j, contador))
        archivo.flush()
        archivo.write("\n")
    mostrar(0)
    for i, objeto in enumerate(it):
        yield objeto
        mostrar(i+1)
        archivo.write("\n")
    archivo.flush()

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
            Función que retorna un número aleatorio entre 0 y 4 redondeado a dos decimales.
        '''
        # Se genera un número aleatorio uniforme entre 0 y 4
        numero = random.uniform(0,4)
        # Retorna o devuelve el  resultado del número aleatorio redondeado a 2 decimales
        return round(numero, 2)
