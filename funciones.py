jugador = {
    "nombre": "pepe",
    "porcentaje_somvick": 0,
    "vidas" : 3
}

def mostrar_menu_inicial():
    print('''
    [¡Bienvenidos a Somvicks!]
    
    Para ser programador necesitás estudiar hasta convertirte en un Somvicks primero.
    Y para ello, deberás contestar las preguntas de menera correcta. Si las contestás bien, sumás puntos; 
    pero cuidado porque si las contestás mal perdés 1 (una) vida. 
    
    1 - Iniciar
    2 - Salir
    ''')

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

