/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package trivia_game;

import java.io.IOException;


public class Trivia_Game {

  public static void main(String args[]) throws IOException {
		int dificultad;
		boolean finalizado;
		String ganador;
		int i;
		String jugador_1;
		String jugador_2;
		String preguntas[][];
		int puntuacion_jugador_1;
		int puntuacion_jugador_2;
		String tec;
		puntuacion_jugador_1 = 0;
		puntuacion_jugador_2 = 0;
		// Reemplazar 5 por la cantidad de preguntas en preguntas
		preguntas = new String[5][6];
		finalizado = false;
		dificultad = 0;
		System.out.println(" ______   ______     __     __   __   __     ______     ");
		System.out.println("/\\__  _\\ /\\  == \\   /\\ \\   /\\ \\ / /  /\\ \\   /\\  __ \\    ");
		System.out.println("\\/_/\\ \\/ \\ \\  __<   \\ \\ \\  \\ \\ \\ /   \\ \\ \\  \\ \\  __ \\   ");
		System.out.println("   \\ \\_\\  \\ \\_\\ \\_\\  \\ \\_\\  \\ \\__|    \\ \\_\\  \\ \\_\\ \\_\\  ");
		System.out.println("    \\/_/   \\/_/ /_/   \\/_/   \\/_/      \\/_/   \\/_/\\/_/  ");
		System.out.println("                                                        ");
		System.out.println("       ______     ______     __    __     ______        ");
		System.out.println("      /\\  ___\\   /\\  __ \\   /\\  -./  \\   /\\  ___\\       ");
		System.out.println("      \\ \\ \\__ \\  \\ \\  __ \\  \\ \\ \\-./\\ \\  \\ \\  __\\       ");
		System.out.println("       \\ \\_____\\  \\ \\_\\ \\_\\  \\ \\_\\ \\ \\_\\  \\ \\_____\\     ");
		System.out.println("        \\/_____/   \\/_/\\/_/   \\/_/  \\/_/   \\/_____/     ");
		System.out.println("");
		System.out.println("               Presione enter para continuar            ");
		tec = bufEntrada.readLine();
		nombres_jugadores(jugador_1,jugador_2);
		dif(dificultad);
		System.out.println(""); // no hay forma directa de borrar la consola en Java
		importar_preguntas(preguntas);
		while (finalizado!=true) {
			// Reemplazar 5 por la cantidad de preguntas en preguntas
			for (i=0;i<=5-1;i++) {
				preguntar(i,preguntas,jugador_1,jugador_2,puntuacion_jugador_1,puntuacion_jugador_2,dificultad);
				System.out.println(""); // no hay forma directa de borrar la consola en Java
			}
			finalizado = true;
		}
		ganador = determinar_ganador(jugador_1,puntuacion_jugador_1,jugador_2,puntuacion_jugador_2,ganador);
		System.out.println(ganador);
	}

	// 1: Guardar los nombres de los jugadores
	public static void nombres_jugadores(String jugador_1, String jugador_2) throws IOException {
		System.out.println(""); // no hay forma directa de borrar la consola en Java
		System.out.println("Indique el nombre del jugador 1:");
		jugador_1 = bufEntrada.readLine();
		System.out.println("Indique el nombre del jugador 2:");
		jugador_2 = bufEntrada.readLine();
	}

	// 2: Eleccion de difilcultad
	public static void dif(double dificultad) throws IOException {
		int opcion;
		System.out.println(""); // no hay forma directa de borrar la consola en Java
		do {
			System.out.println("Seleccione la difcultad: normal (1) y dificil (2)");
			opcion = Integer.parseInt(bufEntrada.readLine());
			if (opcion==1) {
				dificultad = 1;
			} else {
				dificultad = 2;
			}
		} while (!(opcion>0 && opcion<3));
	}

	// 2: Llenado Manual de las preguntas
	public static void importar_preguntas(String preguntas[][]) {
		// Importar desde el Excel generador de variables
		// https://docs.google.com/spreadsheets/d/1icO6GJE6JdbYCTM0qP9i3GnKGf0uGKFoxwS3ORUP18s
		// OJO! Especificar numero de las respuestas
		// La ultima columna muestra la respuesta correcta
		preguntas[0][0] = "CATEGORÍA: GEOGRAFÍA ¿De qué país forma parte Hawaii?";
		preguntas[0][1] = "[1] Estados Unidos";
		preguntas[0][2] = "[2] Argentina";
		preguntas[0][3] = "[3] Brasil";
		preguntas[0][4] = "[4] Ecuador";
		preguntas[0][5] = "1";
		preguntas[1][0] = "CATEGORÍA: GEOGRAFÍA ¿Cuántos estados tiene integrados Estados Unidos?";
		preguntas[1][1] = "49";
		preguntas[1][2] = "15";
		preguntas[1][3] = "50";
		preguntas[1][4] = "180";
		preguntas[1][5] = "3";
		preguntas[2][0] = "CATEGORÍA: GEOGRAFÍA ¿De qué año es la Constitución Española?";
		preguntas[2][1] = "1999";
		preguntas[2][2] = "1978";
		preguntas[2][3] = "1979";
		preguntas[2][4] = "1845";
		preguntas[2][5] = "2";
		preguntas[3][0] = "CATEGORÍA: GEOGRAFÍA ¿Cuál es el río más largo de España?";
		preguntas[3][1] = "El río Elbro";
		preguntas[3][2] = "Opción 2";
		preguntas[3][3] = "Opción 3";
		preguntas[3][4] = "Opción 4";
		preguntas[3][5] = "1";
		preguntas[4][0] = "CATEGORÍA: GEOGRAFÍA ¿Cuál es el océano más grande del mundo?";
		preguntas[4][1] = "El océano Atlántico";
		preguntas[4][2] = "El océano Pacífico";
		preguntas[4][3] = "El océano Índico";
		preguntas[4][4] = "El océano Ártico";
		preguntas[4][5] = "2";
	}

	// 3: Determina la posicion de la matriz (pregunta)
	public static void mostrar_pregunta_individual(String preguntas[][], SIN_TIPO nro_pregunta) {
		int j;
		for (j=0;j<=6-2;j++) {
			System.out.println(preguntas[nro_pregunta][j]);
		}
	}

	// 4: Sistema de turnos para jugadores y lectura de las respuestas
	public static void preguntar(String nro_pregunta, String preguntas, String jugador_1, String jugador_2, double puntuacion_jugador_1, double puntuacion_jugador_2, String dificultad) throws IOException {
		int respuesta;
		mostrar_pregunta_individual(preguntas,nro_pregunta);
		System.out.println("Turno de "+jugador_1+" para responder la pregunta");
		respuesta = Integer.parseInt(bufEntrada.readLine());
		puntuacion_jugador_1 = puntuacion_jugador_1+comprobar_respuesta(preguntas,nro_pregunta,respuesta,dificultad);
		System.out.println(""); // no hay forma directa de borrar la consola en Java
		mostrar_pregunta_individual(preguntas,nro_pregunta);
		System.out.println("Turno de "+jugador_2+" para responder la pregunta");
		respuesta = Integer.parseInt(bufEntrada.readLine());
		puntuacion_jugador_2 = puntuacion_jugador_2+comprobar_respuesta(preguntas,nro_pregunta,respuesta,dificultad);
		System.out.println("Jugador 2 respondió: "+respuesta);
	}

	// 5: Determina si la respuesta correcta
	public static int comprobar_respuesta(String preguntas[][], int nro_pregunta, double respuesta, double dificultad) {
		int premio;
		if (respuesta==String.valueOf(preguntas[nro_pregunta][5])) {
			premio = 20;
		} else {
			if (dificultad==2) {
				premio = -10;
			} else {
				premio = 0;
			}
		}
		// Escribir "Contestó", respuesta;
		// Escribir "Respuesta correcta", preguntas[nro_pregunta, 5];
		return premio;
	}

	// 6: Determina el ganador de la partida
	public static SIN_TIPO determinar_ganador(String jugador_1, String puntuacion_jugador_1, String jugador_2, String puntuacion_jugador_2, SIN_TIPO ganador) {
		String ganador_final;
		String resultado;
		resultado = "";
		ganador_final = "";
		if (puntuacion_jugador_1>puntuacion_jugador_2) {
			resultado = "G A N A   J U G A D O R 1";
			ganador_final = jugador_1;
		} else {
			if (puntuacion_jugador_2>puntuacion_jugador_1) {
				resultado = "G A N A   J U G A D O R 2";
				ganador_final = jugador_2;
			} else {
				resultado = "E M P A T E";
			}
		}
		// BUG: Cuando hay empate, da ganador al jugador_1
		System.out.println(" ______     ______     __    __     ______    "+);
		System.out.println("/\\  ___\\   /\\  __ \\   /\\  -./  \\   /\\  ___\\   "+);
		System.out.println("\\ \\ \\__ \\  \\ \\  __ \\  \\ \\ \\-./\\ \\  \\ \\  __\\   "+);
		System.out.println(" \\ \\_____\\  \\ \\_\\ \\_\\  \\ \\_\\ \\ \\_\\  \\ \\_____\\ "+);
		System.out.println("  \\/_____/   \\/_/\\/_/   \\/_/  \\/_/   \\/_____/ "+);
		System.out.println("                                              "+);
		System.out.println(" ______     __   __   ______     ______       "+"RESULTADOS");
		System.out.println("/\\  __ \\   /\\ \\ / /  /\\  ___\\   /\\  == \\      "+"    "+puntuacion_jugador_1);
		System.out.println("\\ \\ \\/\\ \\  \\ \\ \\ /   \\ \\  __\\   \\ \\  __<      "+"    "+puntuacion_jugador_2);
		System.out.println(" \\ \\_____\\  \\ \\__|    \\ \\_____\\  \\ \\_\\ \\_\\    "+resultado);
		System.out.println("  \\/_____/   \\/_/      \\/_____/   \\/_/ /_/    "+"Gana jugador "+ganador_final);
		System.out.println("");
		return ganador;
	}


}
