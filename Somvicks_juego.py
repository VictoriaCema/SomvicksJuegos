from funciones import *
import random
jugador = {
    "nombre": "pepe",
    "porcentaje_somvicks": 0,
    "vidas" : 3
}

lista_preguntas = ["Siempre que una relación es 'asimétrica' también es 'no simétrica'.", "Super().__init__ no son los atributos heredados de la clase padre.", "¿Las listas son mutables?", "¿Para aprobar Programación I es requisito conocer StarWars?", "Para crear una carpeta desde la terminal se usa el siguiente comando: mkdir <nombreCapeta>", "Los elementos de un set tienen un orden determinado", "La amortización SOLO va en el presupuesto financiero: "]


mostrar_menu_inicial()

opcion = input("Opcion: ")
    
print(" ")
a = 1
vida = chequear_vida(jugador)
while opcion != "2":
    if a == 1:
        a = 2
        nombre = input("Empecemos por tu nombre!: ")
        jugador["nombre"] = nombre
        print(f"Hola {jugador["nombre"]}, esta es tu primera pregunta: \n")
    pregunta = random.choice(lista_preguntas)
    print(pregunta)
    respuesta_usuario = input("\nRespuesta (si/no): ")
    respuesta_correcta = evaluar_pregunta(pregunta)
    if respuesta_correcta == respuesta_usuario:
        agregar_puntos(jugador, 50) 
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
    print(" ")

terminar_juego()


