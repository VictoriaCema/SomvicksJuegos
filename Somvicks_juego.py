from funciones import *
import random
jugador = {
    "nombre": "pepe",
    "porcentaje_somvicks": 0,
    "vidas" : 3
}
lista_preguntas = [["Siempre que una relación es 'asimétrica' también es 'no simétrica'.", "si"], ["Super().__init__ no son los atributos heredados de la clase padre.", "no"], ["¿Las listas son mutables?", "si"], ["¿Para aprobar Programación I es requisito conocer StarWars?", "si"], ["Para crear una carpeta desde la terminal se usa el siguiente comando: mkdir <nombreCapeta>", "si"], ["Los elementos de un set tienen un orden determinado", "no"], ["La amortización SOLO va en el presupuesto financiero: ", "no"]]


mostrar_menu_inicial()

opcion = input("Opcion: ")
while not (opcion == "1" or opcion == "2"):
    opcion = input("Caracter incorrecto, ingrese 1 o 2: ")
    
print(" ")
a = 1
vida = chequear_vida(jugador)
while opcion != "2":
    if a == 1:
        a = 2
        nombre = input("Empecemos por tu nombre!: ")
        jugador["nombre"] = nombre
        print(f'\nHola {jugador["nombre"]}, esta es tu primera pregunta: \n')
    preguntas = len(lista_preguntas)
    indice = random.randint(0, preguntas-1)
    pregunta = lista_preguntas[indice][0]
    print(pregunta)
    respuesta_usuario = input("\nRespuesta (si/no): ").lower()
    while not (respuesta_usuario == "si" or respuesta_usuario == "no"):
        respuesta_usuario = input("Caracter incorrecto, ingrese (si/no): ").lower()
    respuesta_correcta = evaluar_pregunta(lista_preguntas, pregunta)
    if respuesta_correcta == respuesta_usuario:
        agregar_puntos(jugador, 15) 
        print(f'''
            Genial, ganaste 15 puntos.
            ¡Nuevo porcentaje Somvicks!: {jugador['porcentaje_somvicks']}%
            Vidas: {jugador["vidas"]}''')
    else: 
        quitar_vida(jugador)
        print(f'''
            Respuesta incorrecta, pierdes una vida.
            Porcentaje actual de Somvicks: {jugador["porcentaje_somvicks"]}%
            Vidas: {jugador["vidas"]}
        ''')
    if not (chequear_vida(jugador)):
        print("Perdiste todas tus vidas!")
        break
    porcentaje_somvicks = jugador["porcentaje_somvicks"]
    if porcentaje_somvicks > 99:
        jugador["porcentaje_somvicks"] = 100
        print(f'''
        Ganaste, te has convertido en un Somvicks {jugador["porcentaje_somvicks"]}%
        
        Si deseas empezar de nuevo solo elije 'siguiente pregunta' 
        ''')
        jugador["porcentaje_somvicks"] = 0
        jugador["vidas"] = 3
        
    opcion = input('''
        1 - Siguiente pregunta
        2 - Salir
        
        Opcion: ''')
    while not (opcion == "1" or opcion == "2"):
        opcion = input("Caracter incorrecto, ingrese 1 o 2: ")
        
    print(" ")

terminar_juego()


