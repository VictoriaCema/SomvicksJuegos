import random


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

def mostrar_menu_inicial():
    print("""
    Ingrese el numero del espacio al que quiere acceder. 
        1. Programación
        2. Matematica
        3. Organización Empresarial
        4. ArSo
        5. Buffet
        6. Biblioteca
        7. Baño
        8. Pregunta Final! 
        9. Mostrar atributos
        10. Salir                """)

def explicar_juego():
    print('''
        [Bienvenido a Somvicks]
    El objetivo del juego es que te conviertas en un Somvicks después de haber estudiado mucho y aprobado todas las materias! 
    Podés ingresar una sola vez a cada espacio. Las aulas contienen 4 preguntas que deberás contestar. Pero antes puedes elegir el camino del bien, y contestar las preguntas, o echar suerte en el camino del mal, donde puede irte muy bien o muy mal. Es importante que cuides tus vidas y tu puntaje de suerte porque te servirán para rendir el final. Hay otros espacios que pueden o no traerte suerte.
    A la pregunta final solo tendras acceso si el promedio de la suma de los puntos de todas las materias es mayor a 60. Y dependiendo de los puntos de suerte que tengas tendrás mas o menos chance de contestar una pregunta muy difícil o muy fácil.''')


def quitar_vida(jugador:dict):
    jugador["vidas"] -= 1

def terminar_juego():
    print("Saliste del juego")

def chequear_vida(jugador:dict) -> bool:
    if jugador["vidas"] > 0:
        vida = True
    else:
        vida = False
        jugador["vidas"] = 0
    return vida

def evaluar_respuesta(lista, pregunta):
        for i in lista:
            pregunta1 = i[0]
            if pregunta1 == pregunta:
                respuesta = i[1]
                return respuesta

def mostrar_atributos(jugador):
    jugador_items = list(jugador.items()) 
    print("\nEstas son tus estadisticas: \n")
    for clave, valor in jugador_items:
        print(f"{clave} = {valor}")

def elegir_destino()-> str:
    print("Elige tu destino, puedes tomar el camino del bien y contestar las preguntas o echar tu suerte y aceptar las consecuencias...")
    destino = input("1 - Camino del bien 😇\n2 - Camino del mal 😈: ")
    return destino

def rendir_materia(jugador, lista, mensaje, materia):
    destino_elegido = elegir_destino() 
    if destino_elegido == "1": 
        for i in lista:
            elemento = i
            pregunta = elemento[0]
            print(pregunta)
            respuesta_usuario = input("Su respuesta: ")
            respuesta_correcta = evaluar_respuesta(lista, pregunta)
            if respuesta_usuario == respuesta_correcta:
                jugador[materia] += 25
                mensaje1 = mensaje[0]
                print(mensaje1)
            elif respuesta_usuario != respuesta_correcta:
                quitar_vida(jugador)          
                mensaje1 = mensaje[1]
                print(mensaje1)
    elif destino_elegido == "2":
        moneda = random.randint(0,100) + jugador["suerte"] 
        if moneda < 50:
            jugador["vidas"] -= round(jugador["vidas"]/2)
            mensaje1 = mensaje[2]
            print(mensaje1)
        elif moneda > 49:
            mensaje1 = mensaje[3]
            print(mensaje1)
            jugador[materia] += 100
    return

def buscar_en_biblioteca(jugador):
    print('''Entraste a la Biblioteca!
        Puedes:
        1 -  Dormir: Recuperas entre '1-3 vidas' y Pierdes entre'10-30 puntos de suerte'
        2 -  Estudiar: Recuperas enre'10-30 puntos de suerte' y pierdes entre '1-3 vidas' ''')
    accion = input("¿Qué deseas hacer?: ")
    if accion == "1":
        vidas = random.randint(1,3)
        suerte = random.randint(10,30)
        jugador["vidas"] += vidas
        jugador["suerte"] -= suerte
        mensaje = f"Has ganado {vidas} vidas y perdido {suerte} puntos de suerte"
    elif accion == "2":
        vidas = random.randint(1,3)
        suerte = random.randint(10,30)
        jugador["vidas"] -= vidas
        jugador["suerte"] += suerte
        mensaje = f"Has ganado {vidas} vidas y perdido {suerte} puntos de suerte"
    return mensaje

def comprar_buffet(jugador):
    dinero = random.randint(10,5000)
    print(f'''Entraste al Buffet
        abriste tu mercado pago y tienes ${dinero}
        ''')
    if dinero >2999:
        print("Bien! te alcanza para un café y ganas una vida!")
        jugador["vidas"] += 1
        #pudiste comprar el cafe y sumaste vida
    else:
        print("Se te debitó Netflix y no te alcanza para un café. Tu suerte desciende 20 puntos.")
        jugador["suerte"] -= 20
        #NO pudiste comprar el cafe perdiste suerte

def ingresar_banio(jugador):
    banio = random.randint(1,2)
    print(""" Entraste desesperade al baño""")
    if banio == 1:
        print("Encontraste las respuestas en la puerta, ganaste 20 puntos de suerte")
        jugador["suerte"] +=20
    else:
        print("Estaba mojado el piso, te resbalaste y perdiste una vida")
        jugador["vidas"] -=1

def evento_random(suerte): #terminar
    if suerte == "1":
        print("Te encontraste con tu grupo de amigos y te pasan las respuestas. Tu suerte aumenta 20 puntos")
        jugador["suerte"] += 20
    if suerte == "2":
        lista_aleatoria = []
        if jugador["programacion"] != 0:
            lista_aleatoria.append("programacion")
        if jugador["matematica"] != 0:
            lista_aleatoria.append("matematica")
        if jugador["arso"] != 0:
            lista_aleatoria.append("arso")
        if jugador["org_emp"] != 0:
            lista_aleatoria.append("org_emp")
        random.shuffle(lista_aleatoria)
        materia_perdida = random.randint(lista_aleatoria)
        jugador[materia_perdida] = 0
        print(f"En secretaria de alumnos borraron accidentalmente tus regristros, pierdes las notas de {materia_perdida}.")

def tirar_suerte():
    return random.randint(1, 6)

def rendir_final(jugador, lista):
    suma_materias = jugador["programacion"] + jugador["matematica"] + jugador["org_emp"] + jugador["arso"]
    porcentaje = (suma_materias * 100) / 400
    if porcentaje > 59:
        if jugador["suerte"]>30:
            pregunta_final = lista[1][0]
            print(pregunta_final)
            respuesta_usuario = input("Respuesta: ")
            respuesta_correcta = evaluar_respuesta(lista, pregunta_final)
            if respuesta_usuario == respuesta_correcta:
                print("Felicidades! Ganaste el juego!")
                mostrar_atributos(jugador)
            else:
                print("Respuesta Incorrecta. Perdiste el juego")
                jugador["vidas"] = 0
        else:
            pregunta_final = lista[0][0]
            print(lista[0][0])
            respuesta_usuario = input("Respuesta: ")
            respuesta_correcta = evaluar_respuesta(lista, pregunta_final)
            if respuesta_usuario == respuesta_correcta:
                print("Felicidades! Ganaste el juego!")
                mostrar_atributos(jugador)
            else:
                print("Respuesta Incorrecta. Perdiste el juego")
                jugador["vidas"] = 0
    else:
        print("El promedio de las notas fue menor a 60, no puedes rendir el final. Perdiste el juego.")
        jugador["vidas"] = 0


def terminar_juego():
    print("Saliste del juego.")