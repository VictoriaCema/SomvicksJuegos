import random

jugador = {
    "nombre" : "Osom",
    "suerte" : 0,
    "matematica" : 0,
    "programacion" : 0,
    "arso" : 0,
    "org_emp" : 0,
    "vidas" : 10,
    "porcentaje_somvicks" : 0
    }

def tirar_suerte():
    return random.randint(1, 10)


print(tirar_suerte())




