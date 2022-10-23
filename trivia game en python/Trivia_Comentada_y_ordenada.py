# -*- coding: iso-8859-15 -*-
# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


# En python no hay forma de elegir como pasar una variable a una
# funcion (por referencia o por valor). Las variables "inmutables"
# (str, int, float, bool) se pasan siempre por copia mientras que
# las demas (listas, objetos, etc.) se pasan siempre por referencia.
# Esto coincide con el comportamiento por defecto en pseint, pero
# cuando utiliza las palabras clave "Por Referencia" para
# alterarlo la traducci�n no es correcta.

# 1: Guardar los nombres de los jugadores
def nombres_jugadores(jugador_1, jugador_2):
	print "" # no hay forma directa de borrar la pantalla con Python estandar
	print "Indique el nombre del jugador 1:"
	jugador_1 = raw_input()
	print "Indique el nombre del jugador 2:"
	jugador_2 = raw_input()

# 2: Eleccion de difilcultad
def dif(dificultad):
	print "" # no hay forma directa de borrar la pantalla con Python estandar
	opcion = int()
	while True:# no hay 'repetir' en python
		print "Seleccione la difcultad: normal (1) y dificil (2)"
		opcion = int(raw_input())
		if opcion==1:
			dificultad = 1
		else:
			dificultad = 2
		if opcion>0 and opcion<3: break

# 2: Llenado Manual de las preguntas
def importar_preguntas(preguntas):
	# Importar desde el Excel generador de variables
	# https://docs.google.com/spreadsheets/d/1icO6GJE6JdbYCTM0qP9i3GnKGf0uGKFoxwS3ORUP18s
	# OJO! Especificar numero de las respuestas
	# La ultima columna muestra la respuesta correcta
	preguntas[0][0] = "CATEGOR�A: GEOGRAF�A �De qu� pa�s forma parte Hawaii?"
	preguntas[0][1] = "[1] Estados Unidos"
	preguntas[0][2] = "[2] Argentina"
	preguntas[0][3] = "[3] Brasil"
	preguntas[0][4] = "[4] Ecuador"
	preguntas[0][5] = "1"
	preguntas[1][0] = "CATEGOR�A: GEOGRAF�A �Cu�ntos estados tiene integrados Estados Unidos?"
	preguntas[1][1] = "49"
	preguntas[1][2] = "15"
	preguntas[1][3] = "50"
	preguntas[1][4] = "180"
	preguntas[1][5] = "3"
	preguntas[2][0] = "CATEGOR�A: GEOGRAF�A �De qu� a�o es la Constituci�n Espa�ola?"
	preguntas[2][1] = "1999"
	preguntas[2][2] = "1978"
	preguntas[2][3] = "1979"
	preguntas[2][4] = "1845"
	preguntas[2][5] = "2"
	preguntas[3][0] = "CATEGOR�A: GEOGRAF�A �Cu�l es el r�o m�s largo de Espa�a?"
	preguntas[3][1] = "El r�o Elbro"
	preguntas[3][2] = "Opci�n 2"
	preguntas[3][3] = "Opci�n 3"
	preguntas[3][4] = "Opci�n 4"
	preguntas[3][5] = "1"
	preguntas[4][0] = "CATEGOR�A: GEOGRAF�A �Cu�l es el oc�ano m�s grande del mundo?"
	preguntas[4][1] = "El oc�ano Atl�ntico"
	preguntas[4][2] = "El oc�ano Pac�fico"
	preguntas[4][3] = "El oc�ano �ndico"
	preguntas[4][4] = "El oc�ano �rtico"
	preguntas[4][5] = "2"

# 3: Determina la posicion de la matriz (pregunta)
def mostrar_pregunta_individual(preguntas, nro_pregunta):
	j = int()
	for j in range(6-1):
		print preguntas[nro_pregunta][j]

# 4: Sistema de turnos para jugadores y lectura de las respuestas
def preguntar(nro_pregunta, preguntas, jugador_1, jugador_2, puntuacion_jugador_1, puntuacion_jugador_2, dificultad):
	respuesta = int()
	mostrar_pregunta_individual(preguntas,nro_pregunta)
	print "Turno de ",jugador_1," para responder la pregunta"
	respuesta = int(raw_input())
	puntuacion_jugador_1 = puntuacion_jugador_1+comprobar_respuesta(preguntas,nro_pregunta,respuesta,dificultad)
	print "" # no hay forma directa de borrar la pantalla con Python estandar
	mostrar_pregunta_individual(preguntas,nro_pregunta)
	print "Turno de ",jugador_2," para responder la pregunta"
	respuesta = int(raw_input())
	puntuacion_jugador_2 = puntuacion_jugador_2+comprobar_respuesta(preguntas,nro_pregunta,respuesta,dificultad)
	print "Jugador 2 respondi�: ",respuesta

# 5: Determina si la respuesta correcta
def comprobar_respuesta(preguntas, nro_pregunta, respuesta, dificultad):
	premio = int()
	if respuesta==float(preguntas[nro_pregunta][5]):
		premio = 20
	else:
		if dificultad==2:
			premio = -10
		else:
			premio = 0
	# Escribir "Contest�", respuesta;
	# Escribir "Respuesta correcta", preguntas[nro_pregunta, 5];
	return premio

# 6: Determina el ganador de la partida
def determinar_ganador(jugador_1, puntuacion_jugador_1, jugador_2, puntuacion_jugador_2, ganador):
	resultado = str()
	ganador_final = str()
	resultado = ""
	ganador_final = ""
	if puntuacion_jugador_1>puntuacion_jugador_2:
		resultado = "G A N A   J U G A D O R 1"
		ganador_final = jugador_1
	else:
		if puntuacion_jugador_2>puntuacion_jugador_1:
			resultado = "G A N A   J U G A D O R 2"
			ganador_final = jugador_2
		else:
			resultado = "E M P A T E"
	# BUG: Cuando hay empate, da ganador al jugador_1
	print " ______     ______     __    __     ______    ",
	print "/\\  ___\\   /\\  __ \\   /\\  -./  \\   /\\  ___\\   ",
	print "\\ \\ \\__ \\  \\ \\  __ \\  \\ \\ \\-./\\ \\  \\ \\  __\\   ",
	print " \\ \\_____\\  \\ \\_\\ \\_\\  \\ \\_\\ \\ \\_\\  \\ \\_____\\ ",
	print "  \\/_____/   \\/_/\\/_/   \\/_/  \\/_/   \\/_____/ ",
	print "                                              ",
	print " ______     __   __   ______     ______       ","RESULTADOS"
	print "/\\  __ \\   /\\ \\ / /  /\\  ___\\   /\\  == \\      ","    ",puntuacion_jugador_1
	print "\\ \\ \\/\\ \\  \\ \\ \\ /   \\ \\  __\\   \\ \\  __<      ","    ",puntuacion_jugador_2
	print " \\ \\_____\\  \\ \\__|    \\ \\_____\\  \\ \\_\\ \\_\\    ",resultado
	print "  \\/_____/   \\/_/      \\/_____/   \\/_/ /_/    ","Gana jugador ",ganador_final
	print ""
	return ganador

if __name__ == '__main__':
	jugador_1 = str()
	jugador_2 = str()
	puntuacion_jugador_1 = int()
	puntuacion_jugador_2 = int()
	ganador = str()
	dificultad = int()
	tec = str()
	puntuacion_jugador_1 = 0
	puntuacion_jugador_2 = 0
	preguntas = str()
	# Reemplazar 5 por la cantidad de preguntas en preguntas
	preguntas = [[str() for ind0 in range(6)] for ind1 in range(5)]
	finalizado = bool()
	finalizado = False
	dificultad = 0
	print " ______   ______     __     __   __   __     ______     "
	print "/\\__  _\\ /\\  == \\   /\\ \\   /\\ \\ / /  /\\ \\   /\\  __ \\    "
	print "\\/_/\\ \\/ \\ \\  __<   \\ \\ \\  \\ \\ \\ /   \\ \\ \\  \\ \\  __ \\   "
	print "   \\ \\_\\  \\ \\_\\ \\_\\  \\ \\_\\  \\ \\__|    \\ \\_\\  \\ \\_\\ \\_\\  "
	print "    \\/_/   \\/_/ /_/   \\/_/   \\/_/      \\/_/   \\/_/\\/_/  "
	print "                                                        "
	print "       ______     ______     __    __     ______        "
	print "      /\\  ___\\   /\\  __ \\   /\\  -./  \\   /\\  ___\\       "
	print "      \\ \\ \\__ \\  \\ \\  __ \\  \\ \\ \\-./\\ \\  \\ \\  __\\       "
	print "       \\ \\_____\\  \\ \\_\\ \\_\\  \\ \\_\\ \\ \\_\\  \\ \\_____\\     "
	print "        \\/_____/   \\/_/\\/_/   \\/_/  \\/_/   \\/_____/     "
	print ""
	print "               Presione enter para continuar            "
	tec = raw_input()
	nombres_jugadores(jugador_1,jugador_2)
	dif(dificultad)
	print "" # no hay forma directa de borrar la pantalla con Python estandar
	importar_preguntas(preguntas)
	i = int()
	while finalizado!=True:
		# Reemplazar 5 por la cantidad de preguntas en preguntas
		for i in range(5):
			preguntar(i,preguntas,jugador_1,jugador_2,puntuacion_jugador_1,puntuacion_jugador_2,dificultad)
			print "" # no hay forma directa de borrar la pantalla con Python estandar
		finalizado = True
	ganador = determinar_ganador(jugador_1,puntuacion_jugador_1,jugador_2,puntuacion_jugador_2,ganador)
	print ganador

