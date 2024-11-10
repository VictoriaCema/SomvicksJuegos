import random

lista_espacios = ["programacion", "matematica", "arso", "org_emp", "buffete", "biblioteca", "banio"]

def validar_entrada(lista, espacio):
    if espacio not in lista:
        print("Ya entraste a este espacio, elige otro.")
        entrar = "no"
    else:
        entrar = "si"
        return entrar

materia = "programacion"
puede_rendir = validar_entrada(lista_espacios, materia)

print(puede_rendir)



