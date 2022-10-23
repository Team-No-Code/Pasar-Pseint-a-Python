# Pasar-Pseint-a-Python
pasando el juego de trivia, de Pseint a Python .. Contiene algunos errores.. 


#Trivia Game
import db as db # Utilizd db para estandarizar como base de datos


#definimos las variables
class Trivia_Game:
    def __init__(self, jugador1,jugador2, importar_preguntas):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.importar_preguntas = importar_preguntas
    def __abs__(self, puntuacion_jugador1, puntuacion_jugador2 ):
        self.puntuacion_jugador1 = puntuacion_jugador1
        self.puntuacion_jugador2 = puntuacion_jugador2
    def __del__(self, dificultad, ganador, tec, categoria):
        self.dificultad = dificultad
        self.ganador = ganador
        self.tec = tec
        self.categoria = categoria

buffer = open("importar_preguntas", "dificultad")
raw_material = buffer.readlines()

for line in raw_material:
    "categoria; geografia\n"
    continente, pais, capital = line.split(";")
    pais = pais[:-1]
    db[pais] = pais
    print(f"¿ De qué país forma parte Hawaii :")
    print(db)
    {"Estados Unidos", "Brasil", " Alemania"}

num_jugadores_tec = int(input("¿Cuántos jugadores jugaran?: "))
num_dificultad_tec = int(input("¿Qué nivel de dificultad jugaran?: "))

# para construir la logica del juego, se debe repetir tres veces, para eso tengo que
# cargar dos bucles for,  donde jugan dos jugadores, anidados
# primero se construye el bucle que va a controlar los turnos de los ugadores

for i in range(num_cantidad_turnos):
    for j in range(num_jugadores):
        pais_random = random.choice(list(db.keys()))
        print(pais_random)
        respuesta = input(f"De qué pais forma parte Hawaii {pais_random}?")
        if respuesta == db[pais_random]:
            print("Respuesta Correcta")
        else:
            print(f"la respuesta no es correcta, el pais es: {db[pais_random]}")
            









