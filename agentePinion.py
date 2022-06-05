# Creador: Bryan Alfredo Solórzano Montero

# Planteamiento: Se trata de un tipo de agente capaz de determinar el lso cambios correctos de los piñones en las bicicletas para facilitarle a los principiante ese proceso de adaptación

# Librerias necesarias
import time

'''
El agente sera capaz de detectar 7 tipo de inclinaciones frontales
Estamos hablando de temas de escala consideradas de la siguiente forma
0: 

'''
DISTANCIA_HORIZONTAL = 40
distancia_vertical = 0
pinion = {'one': 0, 'two': 0, 'three': 0, 'four': 0, 'five': 0, 'six': 0, 'seven': 0}
plato = {'one': None, 'two': None, 'three': None}

'''
    FORMULA PARA calcular el porcentaje de inclinación 
    DV = Distancia Verticar
    DH = Distancia Horizontal
    DV/DH x 100 = % de inclinación
'''
index = 0

for pin in pinion:
    index += 1
    print(index, pin, pinion[pin])

for pla in plato:
    plato[pla] = 1
    print(pla, plato[pla])