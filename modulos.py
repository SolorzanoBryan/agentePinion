
import sys # Importa el módulo para manejar exepciones personalizadas 

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

