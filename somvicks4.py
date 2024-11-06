import random 
from funciones_juego import (mostrar_menu_inicial, rendir_materia, tirar_suerte, evento_random, comprar_buffet, buscar_en_biblioteca, ingresar_banio, mostrar_atributos, elegir_destino, quitar_vida, terminar_juego, evaluar_respuesta, chequear_vida)


'''
#ideas:
    que el jugador vaya entrando a aulas, donde se encuente con dos opciones, un machete o contestar una pregunta. 
    Si se elige el machete que exista la posibilidad (50%) de que entre el prof y te haga recursar la materia.
    
    1 jugador 
    objetivo: convertirse en Somvicks
    como: contestando bien las preguntas hasta llegar a 70%
    
    hasta encontrar con un npc final 
    non playable character

funciones: 
mostrar_pregunta(lista)
elegir_lugar()
elegir_tudestino() ---> elegir camino del bien o camino del mal
jugar()
quitar_vida()
agregar_vida()
aumentar_suerte() ---> cuando en biblioteca elegis estudiar (reducir vida) / baño / buffet
disminuir_suerte() --> cuando decis dormir (pero aumenta tu vida) / baño
mostrar_estadisticas()
[evento random que pase aleatoriamente yendo de un aula a otra]
[que se pueda entrar una sola vez a cada espacio]

'''
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
lista_matematica = [["Siempre que una relación es 'asimétrica' también es 'no simétrica'.", "si"], ]
lista_org_emp = [["La amortización SOLO va en el presupuesto financiero: ", "no"]]
lista_arso = [["Para crear una carpeta desde la terminal se usa el siguiente comando: mkdir <nombreCapeta>", "si"], ]

mensaje_incorrecta = "Respuesta incorrecta, pierdes una vida"

mensaje_programacion = ["Muy bien! sumaste 25 puntos a programacion", mensaje_incorrecta,"Te encontraste con Tomy, el perro Somvicks de Enzo, te mordió y perdiste la mitad de tus vidas","¡Felicidades! \n Te encontraste con Tommy, el perro Somvicks de Enzo y te entrego un hack con las respuestas!"]
mensaje_matematica = ["Muy bien! sumaste 25 puntos a matematica", mensaje_incorrecta, "Entro un Phonte salvaje y te encontro con las manos en la masa, sacandole fotos al examen \nPerdiste la mitad de tus vidas.", "¡Felicidades! \nSacaste satisfactoriamente la foto al examen y no fuiste descubierto, diablillo" ]
mensaje_org_emp = ["Muy bien! sumaste 25 puntos a Organizacion Empresarial", mensaje_incorrecta, "Aviso por señales de humo que el examen era virtual pero vos fuiste a la facu y te atropelló el 17.  \nPerdiste la mitad de tus vidas.","¡Felicidades! \nRenuncio el profe y sacaron la materia del plan de estudio.💖"]
mensaje_arso = ["Muy bien! sumaste 25 puntos a arso",  mensaje_incorrecta,"Te quedaste dormido en todas las clases, quedaste libre.", "¡Felicidades! \nEl michi de la profe te reemplazo en el parcial y aprobaste" ]
preguntas_finales = ["Pregunta dificil, pregunta facíl"] #Vicky chiquita: pensa una pregunta recontra dificil e integradora, que sea multiplechoice con 5 respuestas posibles  y una muy facil, también con 5 respuetas posibles
contador = 0


while True: 
    mostrar_menu_inicial()
    espacio = input("Opcion: ")
    match espacio:
        case "1": 
            contador = 0
            if contador == 0: 
                materia = "programacion"
                rendir_materia(jugador, lista_programacion, mensaje_programacion, materia) 
                contador += 1
            else:
                print("Ya rendiste Programacion, elige otra aula.")
            suerte = tirar_suerte()
            if suerte == 1 or suerte == 2:
                evento_random(suerte)
        case "2":
            contador = 0
            if contador == 0: 
                materia = "matematica"
                rendir_materia(jugador, lista_matematica, mensaje_matematica, materia)
                contador += 1
            else:
                print("Ya rendiste Matematica, elige otra aula.")
            suerte = tirar_suerte()
            if suerte == 1 or suerte == 2:
                evento_random(suerte)
        case "3":
            contador = 0
            if contador == 0:
                materia = "Organizacion Empresarial"
                rendir_materia(jugador, lista_org_emp, mensaje_org_emp, materia)
                contador += 1
            else:
                print("Ya rendiste Organizacion Empresarial, elige otra aula.")
            suerte = tirar_suerte()
            if suerte == 1 or suerte == 2:
                evento_random(suerte)
        case "4":
            contador = 0
            if contador == 0: 
                materia = "ArSo"
                rendir_materia(jugador, lista_arso, mensaje_arso, materia)
                contador += 1
            else:
                print("Ya rendiste ArSo, elige otra aula.")
            suerte = tirar_suerte()
            if suerte == 1 or suerte == 2:
                evento_random(suerte)
        case "5":
            contador = 0
            if contador == 0:
                comprar_buffet(jugador)
            else:
                print("Ya entraste al Buffet, elige otro espacio.")
            suerte = tirar_suerte()
            if suerte == 1 or suerte == 2:
                evento_random(suerte)
        case "6":
            contador = 0
            if contador == 0:
                buscar_en_biblioteca(jugador)
            else:
                print("Ya entraste a la biblioteca, elige otro espacio.")
            suerte = tirar_suerte()
            if suerte == 1 or suerte == 2:
                evento_random(suerte)
        case "7":
            contador = 0
            if contador == 0:
                ingresar_banio(jugador)
            suerte = tirar_suerte()
            if suerte == 1 or suerte == 2:
                evento_random(suerte)
        case "8":
            pass
            #8. Pregunta Final!
            
        
        case "9":
            #mostrar atributos/estadísticas
            mostrar_atributos(jugador)
        case _:
            print("Opcion invalida, ingrese nuevamente")
            

