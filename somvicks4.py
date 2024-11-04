import random 
from funciones import *

'''
#ideas:
    que el jugador vaya entrando a aulas, donde se encuente con dos opciones, un machete o contestar una pregunta. 
    Si se elige el machete que exista la posibilidad (50%) de que entre el prof y te haga recursar la materia.
    
    1 jugador 
    objetivo: convertirse en Somvicks
    como: contestando bien las preguntas hasta llegar a 70%
    
    hasta encontrar con un npc final 
    non playable character
    
    jugador = {
        "nombre" : "",
        "suerte" : "",
        "matematica" : "",
        "programacion" : "",
        "ArSo" : "",
        "Org. Emp" : "",
        "vidas" : 4,
        "porcentaje_somvicks" : ""
    }

4 lista de preguntas por materia

1 - Aula prog
2 - Aula mat
3 - Aula org. emp
4 - Aula Arso
5 - Buffet
6 - Biblioteca    
7 - Baños

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
pregunta_final_dificil = "" #Vicky chiquita: pensa una pregunta recontra dificil e integradora, que sea multiplechoice con 5 respuestas posibles
pregunta_final_facil = "" #Vicky chiquita: pensa una pregunta recontra dificil e integradora, que sea multiplechoice con 5 respuestas posibles
contador = 0

while True: 
    espacio = input("""Ingrese el numero del espacio al que quiere acceder. 
                    1. Programación
                    2. Matematica
                    3. Organización Empresarial
                    4. ArSo
                    5. Buffet
                    6. Biblioteca
                    7. Baño
                    8. Pregunta Final! 
                    9. Salir
                    """)
    match espacio:
        case "1": 
            contador = 0
            if contador == 0: 
                materia = "programacion"
                #rendir_materia(jugador, lista_programacion, mensaje_programacion, materia)
                contador += 1
            else:
                print("Ya rendiste Programacion, elige otra aula.")
            
        case "2":
            contador = 0
            if contador == 0: 
                materia = "matematica"
                #rendir_materia(jugador, lista_matematica, mensaje_matematica, materia)
                contador += 1
            else:
                print("Ya rendiste Matematica, elige otra aula.")
        
        case "3":
            contador = 0
            if contador == 0:
                materia = "Organizacion Empresarial"
                #rendir_materia(jugador, lista_org_emp, mensaje_org_emp, materia)
                contador += 1
            else:
                print("Ya rendiste Organizacion Empresarial, elige otra aula.")
        
        case "4":
            contador = 0
            if contador == 0: 
                materia = "ArSo"
                #rendir_materia(jugador, lista_arso, mensaje_arso, materia)
                contador += 1
            else:
                print("Ya rendiste ArSo, elige otra aula.")
        
        case "5":
            contador = 0
            if contador == 0:
                comprar_buffet(jugador)
            else:
                print("Ya entraste al Buffet, elige otro espacio.")
                
        case "6":
            contador = 0
            if contador == 0:
                buscar_en_biblioteca(jugador)
            else:
                print("Ya entraste a la biblioteca, elige otro espacio.")
        case "7":
            contador = 0
            if contador == 0:
                ingresar_banio(jugador)
        case "8":
            pass
        
        case _:
            print("Opcion invalida, ingrese nuevamente")
            

            