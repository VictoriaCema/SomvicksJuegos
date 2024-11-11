import random 
from funciones_juego import (mostrar_menu_inicial, rendir_materia, tirar_suerte, evento_random, comprar_buffet, buscar_en_biblioteca, ingresar_banio, mostrar_atributos, elegir_destino, quitar_vida, terminar_juego, evaluar_respuesta, chequear_vida, rendir_final, explicar_juego, validar_entrada)
from listas import (lista_programacion, lista_matematica, lista_org_emp, lista_arso, mensaje_incorrecta, mensaje_programacion, mensaje_matematica, mensaje_org_emp, mensaje_arso, preguntas_finales, lista_espacios )

jugador = {
    "nombre" : "",
    "suerte" : 0,
    "matematica" : 0,
    "programacion" : 0,
    "arso" : 0,
    "org_emp" : 0,
    "vidas" : 10,
    "porcentaje_somvicks" : 0
    }

contador_final = 0
espacio = 1

explicar_juego()
jugador["nombre"] = input("Empecemos por tu nombre: ")
print(f"Hola {jugador["nombre"]}! mucha suerte!\n")
while espacio != "10": 
    mostrar_menu_inicial()
    espacio = input("Opción: ")
    match espacio:
        case "1": 
            materia = "programacion"
            puede_rendir = validar_entrada(lista_espacios, materia)
            if puede_rendir == "si":
                lista_espacios.pop(0)
                rendir_materia(jugador, lista_programacion, mensaje_programacion, materia) 
                contador_final += 1
            suerte = tirar_suerte()
            if suerte == 1 or suerte == 2:
                evento_random(suerte)
            vida = chequear_vida(jugador)
            if vida == False:
                print("Perdiste todas tus vidas.")
                espacio = "10"
                terminar_juego()
        case "2":
            materia = "matematica"
            puede_rendir = validar_entrada(lista_espacios, materia)
            if puede_rendir == "si": 
                lista_espacios.pop(1)
                rendir_materia(jugador, lista_matematica, mensaje_matematica, materia)
                contador_final += 1
            suerte = tirar_suerte()
            if suerte == 1 or suerte == 2:
                evento_random(suerte)
            vida = chequear_vida(jugador)
            if vida == False:
                print("Perdiste todas tus vidas.")
                espacio = "10"
                terminar_juego()
        case "3":
            materia = "org_emp"
            puede_rendir = validar_entrada(lista_espacios, materia)
            if puede_rendir == "si":
                lista_espacios.pop(2)
                rendir_materia(jugador, lista_org_emp, mensaje_org_emp, materia)
                contador_final += 1
            suerte = tirar_suerte()
            if suerte == 1 or suerte == 2:
                evento_random(suerte)
            vida = chequear_vida(jugador)
            if vida == False:
                print("Perdiste todas tus vidas.")
                espacio = "10"
                terminar_juego()
        case "4":
            materia = "arso"
            puede_rendir = validar_entrada(lista_espacios, materia)
            if puede_rendir == "si":
                lista_espacios.pop(3)
                rendir_materia(jugador, lista_arso, mensaje_arso, materia)
                contador_final += 1
            suerte = tirar_suerte()
            if suerte == 1 or suerte == 2:
                evento_random(suerte)
            vida = chequear_vida(jugador)
            if vida == False:
                print("Perdiste todas tus vidas.")
                espacio = "10"
                terminar_juego()
        case "5":
            lugar = "buffet"
            puede_rendir = validar_entrada(lista_espacios, lugar) 
            if puede_rendir == "si":
                lista_espacios.pop(4)
                comprar_buffet(jugador)
                contador_final += 1
            suerte = tirar_suerte()
            if suerte == 1 or suerte == 2:
                evento_random(suerte)
            vida = chequear_vida(jugador)
            if vida == False:
                print("Perdiste todas tus vidas.")
                espacio = "10"
                terminar_juego()
        case "6":
            lugar = "biblioteca"
            puede_rendir = validar_entrada(lista_espacios, lugar)
            if puede_rendir == "si":
                lista_espacios.pop(5)
                buscar_en_biblioteca(jugador)
                contador_final += 1
            suerte = tirar_suerte()
            if suerte == 1 or suerte == 2:
                evento_random(suerte)
            vida = chequear_vida(jugador)
            if vida == False:
                print("Perdiste todas tus vidas.")
                espacio = "10"
                terminar_juego()
        case "7":
            lugar = "banio"
            puede_rendir = validar_entrada(lista_espacios, lugar)
            if puede_rendir == "si":
                lista_espacios.pop(6)
                ingresar_banio(jugador)
                contador_final += 1
            suerte = tirar_suerte()
            if suerte == 1 or suerte == 2:
                evento_random(suerte)
            vida = chequear_vida(jugador)
            if vida == False:
                print("Perdiste todas tus vidas.")
                espacio = "10"
                terminar_juego()
        case "8":
            if contador_final == 7:
                rendir_final(jugador, preguntas_finales)
                vida = chequear_vida(jugador)
                if vida == False:
                    print("Perdiste todas tus vidas.")
                    espacio = "10"
                    terminar_juego()
            else:
                print("No puedes rendir el final sin ingresar a todos los espacios primero.")
        case "9":
            mostrar_atributos(jugador)
        case "10": 
            terminar_juego()
        case _:
            print("Opción inválida, ingrese nuevamente")
