import random 
from funciones_juego import (mostrar_menu_inicial, rendir_materia, tirar_suerte, evento_random, comprar_buffet, buscar_en_biblioteca, ingresar_banio, mostrar_atributos, elegir_destino, quitar_vida, terminar_juego, evaluar_respuesta, chequear_vida, rendir_final, explicar_juego)

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

lista_programacion = [["Super().__init__ no son los atributos heredados de la clase padre.", "no"], ["¿Las listas son mutables?", "si"], ["¿Para aprobar Programación I es requisito conocer StarWars?", "si"],["Los elementos de un set tienen un orden determinado", "no"]]
lista_matematica = [["Siempre que una relación es 'asimétrica' también es 'no simétrica'.", "si"], [ "Si V( p->q) = 0. El valor de verdad de la sig. proposición -( p ^ q) -> q = 1", "no"], ["Si el conjunto A está incluido en el conjunto B, la diferencia simetrica de A y B es = B-A"],["si"],["Para que dos matrices puedan multiplicarse, las filas de la primera y las columnas de la segunda tienen que ser iguales","no"]] 
lista_org_emp = [["La amortización SOLO va en el presupuesto financiero: ", "no"],["Las SAS son completamente digitales", "si"], ["Los dividendos pagados se suman al resultado del patrimonio neto.","no"], ["Los intereses ganados en inversiones se incluyen en ingresos extraordinarios","si"]] 
lista_arso = [["Para crear una carpeta desde la terminal se usa el siguiente comando: mkdir <nombreCapeta>", "si"], ["Con el comando ls -l veo el contenido de un archivo.","no"], ["Para modificar un archivo se usa el comando vim","si"], ["El comando 'vagrant up' enciende la maquina virtual y nos inicia sesion dentro de ella","no"] ] 

mensaje_incorrecta = "Respuesta incorrecta, pierdes una vida"

mensaje_programacion = ["Muy bien! sumaste 25 puntos a programación", mensaje_incorrecta,"Te encontraste con Tomy, el perro Somvicks de Enzo, te mordió y perdiste la mitad de tus vidas","¡Felicidades! \n Te encontraste con Tommy, el perro Somvicks de Enzo y te entregó un hack con las respuestas!"]
mensaje_matematica = ["Muy bien! sumaste 25 puntos a matemática", mensaje_incorrecta, "Entro un Phonte salvaje y te encontró con las manos en la masa, sacándole fotos al examen \nPerdiste la mitad de tus vidas.", "¡Felicidades! \nSacaste satisfactoriamente la foto al examen y no fuiste descubierto, diablillo" ]
mensaje_org_emp = ["Muy bien! sumaste 25 puntos a Organización Empresarial", mensaje_incorrecta, "El profe visó por señales de humo que el examen era virtual pero vos fuiste a la facu y te atropelló el 17.  \nPerdiste la mitad de tus vidas.","¡Felicidades! \nRenunció el profe y sacaron la materia del plan de estudio.💖"]
mensaje_arso = ["Muy bien! sumaste 25 puntos a arso",  mensaje_incorrecta,"Te quedaste dormido en todas las clases, quedaste libre.", "¡Felicidades! \nLa michi de la profe te reemplazó en el parcial y aprobaste" ]
preguntas_finales = [["En el paradigma funcional es posible que una función retorne otra función comoresultado", "si"], ["En un diccionario pueden existir claves duplicadas.", "no"]]

contador_p = 0
contador_m = 0
contador_a = 0
contador_o = 0
contador_bi = 0
contador_ba = 0
contador_bu = 0
contador_final = 0
espacio = 1


lista_espacios = ["programacion", "matematica", "org_emp", "arso", "buffet", "biblioteca", "banio"]

def validar_entrada(lista, espacio):
    if espacio not in lista:
        print("Ya entraste a este espacio, elige otro.")
        entrar = "no"
    else:
        entrar = "si"
        return entrar

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
            

