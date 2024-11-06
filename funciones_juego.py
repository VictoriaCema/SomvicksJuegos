import random

def mostrar_menu_inicial():
    print("""Ingrese el numero del espacio al que quiere acceder. 
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

def agregar_puntos(jugador: dict, puntaje: int):
    jugador["porcentaje_somvicks"] += puntaje

def quitar_vida(jugador:dict):
    jugador["vidas"] -= 1

def terminar_juego():
    print("Saliste del juego")

def chequear_vida(jugador:dict) -> bool:
    if jugador["vidas"] > 0:
        vida = True
    else:
        vida = False
    return vida

def evaluar_respuesta(lista, pregunta):
        for i in lista:
            pregunta1 = i[0]
            if pregunta1 == pregunta:
                respuesta = i[1]
                return respuesta

def elegir_destino():
    print("Elige tu destino, puedes tomar el camino del bien y contestar las preguntas o echar tu suerte y aceptar las consecuencias...")
    destino = input("1 - Camino del bien 😇\n 2- Camino del mal 😈: ")
    return destino

def rendir_materia(jugador, lista, mensaje, materia):
    destino = elegir_destino() #Esta funcion devuelve un bool
    if destino == "1": 
        for i in lista:
            pregunta = [lista][i]
            print(pregunta)
            respuesta_usuario = input("Su respuesta: ")
            respuesta_correcta = evaluar_respuesta(lista, pregunta)
            if respuesta_usuario == respuesta_correcta:
                jugador[materia] += 25
                mensaje = mensaje[0]
            elif respuesta_usuario != respuesta_correcta:
                jugador["vidas"] -= 1          
                mensaje = mensaje[1]
    elif destino == "2":
        moneda = random.randint(0,100) + jugador["suerte"] 
        if moneda < 50:
            jugador["vidas"] -= round(jugador["vidas"]/2)
            mensaje = mensaje[2]
        elif moneda > 49:
            mensaje = mensaje[3]
            jugador[materia] += 100
    return mensaje

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
        print("Bien! te alcanza para un cafe y ganas una vida!")
        jugador["vidas"] += 1
        #pudiste comprar el cafe y sumaste vida
    else:
        print("Se te debito Netflix y no te alcanza para un cafe. Tu suerte desciende 20 puntos.")
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

def mostrar_atributos(jugador):
    print(f'''Estas son tus estadisticas: 
        {jugador}''')

def evento_random(): #terminar
    pass
    
def rendir_final(jugador):
    suma_materias = jugador["programacion"] + jugador["matemtica"] + jugador["org_emp"] + jugador["arso"]
    porcentaje = (suma_materias * 100) / 400
    if porcentaje > 69:
        if jugador["suerte"]>30:
            #print(pregunta_final_facil)
            respuesta_usuario = input("Respuesta: ")
            #evaluar_final(pregunta_final_facil, respuesta_usuario)
            pass
        else:
            #print(pregunta_final_dificil)
            respuesta_usuario = input("Respuesta: ")
            #evaluar_final(pregunta_final_dificil, respuesta_usuario)
            pass

def evaluar_final(): #terminar
    pass
    return #respuesta_correcta
    pass