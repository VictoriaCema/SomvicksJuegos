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
    
def evaluar_pregunta(pregunta):
    if pregunta == "Siempre que una relación es 'asimétrica' también es 'no simétrica'.":
        respuesta = "si"
    elif pregunta == "Super().__init__ no son los atributos heredados de la clase padre.":
        respuesta = "no"
    elif pregunta == "¿Las listas son mutables?":
        respuesta = "si"
    elif pregunta == "¿Para aprobar Programación I es requisito conocer StarWars?":
        respuesta = "si"
    elif pregunta == "Para crear una carpeta desde la terminal se usa el siguiente comando: mkdir <nombreCapeta>":
        respuesta = "si"
    elif pregunta ==  "Los elementos de un set tienen un orden determinado":
        respuesta = "no"
    elif pregunta == "La amortización SOLO va en el presupuesto financiero: ":
        respuesta = "no"
    return respuesta
