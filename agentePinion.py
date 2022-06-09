# Creador: Bryan Alfredo Solórzano Montero

# Planteamiento: Se trata de un tipo de agente capaz de determinar el lso cambios correctos de los piñones en las bicicletas para facilitarle a los principiante ese proceso de adaptación

# Librerias necesarias
import time
import random

'''
El agente sera capaz de detectar 7 tipo de inclinaciones frontales
Estamos hablando de temas de escala consideradas de la siguiente forma
0: 

'''
distancia_vertical = 0
registrar_pinion = []
registrar_plato = []
pinion = {'uno': 0, 'dos': 0, 'tres': 0, 'cuatro': 0, 'cinco': 0, 'seis': 0, 'siete': 0}
plato = {'uno': None, 'dos': None, 'tres': None}

'''
    FORMULA PARA calcular el porcentaje de inclinación 
    DV = Distancia Verticar
    DH = Distancia Horizontal
    DV/DH x 100 = % de inclinación
'''
index = 0

# for pin in pinion:
#     index += 1
#     print(index, pin, pinion[pin])

# for pla in plato:
#     plato[pla] = 1
#     print(pla, plato[pla])

def logica_absoluta():
    distancia_horizontal = float(input("Introduzca cada cuantos metros desea que se haga el escaneo del ambiente para poder hacer los cambios a los piñones: ") )
    repeticiones = int(input(f"Introduzca la cantidad de repeticiones de {distancia_horizontal} metros") )
   
    for num in range(0, repeticiones):
        vertical = verticalRandom()
        porcentaje_inclinacion = round((vertical/distancia_horizontal) * 100)
        
        resultado_comparatoria = resolver(porcentaje_inclinacion)
        pin = resultado_comparatoria.get('pinion')
        pla = resultado_comparatoria.get('plato')
        dificultad = resultado_comparatoria.get('deficultad')
        cambios(pin, pla)
        if not dificultad:
            print(f'En estos {distancia_horizontal} metros su grado de dificulad sera del {porcentaje_inclinacion} %')
            print(f'La combinación sera el piñon {pin} y el plato {pla}')
        else:
            print(f'En estos {distancia_horizontal} metros su grado de dificulad sera del {porcentaje_inclinacion} %')
            print(f'La combinación sera el piñon {pin} y el plato {pla}')

        registrar_pinion.append(pinion)
        registrar_plato.append(plato)

def verticalRandom():
    num = random.uniform(0,4)
    return round(num, 2)

def cambios(pin_entrada, plato_entrada):
    for pin in pinion:
        if pin == pin_entrada:
            pinion[pin] = 1
        else:
            pinion[pin] = 0
    for pla in plato:
        if pla == plato_entrada:
            pinion[pla] = 1
        else:
            pinion[pla] = 0

def resolver(porcentaje_inclinacion):
    if porcentaje_inclinacion == 0:
        return {"pinion": "uno", "plato": "tres", "dificultad": False}
    else:
        if porcentaje_inclinacion <= 3:
            return {"pinion": "dos", "plato": "tres", "dificultad": False}
        else:
            if porcentaje_inclinacion <= 6:
                return {"pinion": "tres", "plato": "dos", "dificultad": False}
            else:
                if porcentaje_inclinacion <= 9:
                    return {"pinion": "cuatro", "plato": "dos", "dificultad": True}
                else:
                    if porcentaje_inclinacion <= 15:
                        if porcentaje_inclinacion < 13:
                            return {"pinion": "cinco", "plato": "dos", "dificultad": True}
                        else:
                            return {"pinion": "seis", "plato": "uno", "dificultad": True}
                    else:
                        return {"pinion": "siete", "plato": "uno", "dificultad": True}

logica_absoluta()
