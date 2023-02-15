import random


class Tablero:
    def __init__(self):
        self.longitud = 5
        self.altura = 4
        self.tablero = [[0 for x in range(self.longitud)] for y in range(self.altura)]

    def imprimir_tablero(self):
        for i in range(self.altura):
            for j in range(self.longitud):
                print(self.tablero[i][j], end="\t")
            print()


import random


class Juego:
    def __init__(self, jugador1, jugador2):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.tablero = Tablero()
        self.dado = random.randint(1, 6)

    def pregunta(self):
        respuestas = {"a": "respuesta a", "b": "respuesta b", "c": "respuesta c"}
        respuesta_correcta = "a"
        # Generar pregunta con tres opciones de respuesta
        print("Pregunta:")
        print("Opción a:", respuestas["a"])
        print("Opción b:", respuestas["b"])
        print("Opción c:", respuestas["c"])
        respuesta = input("Ingrese su respuesta (a, b o c): ")
        if respuesta == respuesta_correcta:
            print("¡Respuesta correcta!")
            return True
        else:
            print("Respuesta incorrecta :(")
            return False

    def manejar_castigo(self, jugador):
        castigos = ["puente", "resbalón", "calavera"]
        castigo = random.choice(castigos)
        print(f"{jugador.nombre} ha caído en una {castigo}.")
        if castigo == "puente":
            jugador.posicion = max(1, jugador.posicion - 3)
        elif castigo == "resbalón":
            jugador.posicion = max(1, jugador.posicion - 2)
        else:
            jugador.posicion = 1
        jugador.castigos += 1

    def jugar(self):
        turno = 1
        ganador = None
        while ganador is None:
            if turno % 2 == 1:
                jugador = self.jugador1
            else:
                jugador = self.jugador2

            print(f"Es el turno de {jugador.nombre}")
            print(f"Está en la casilla {jugador.posicion}")
            # Tirar el dado
            tirada = random.randint(1, 6)
            print(f"Tirada del dado: {tirada}")
            # Mover al jugador a la nueva posición
            jugador.posicion += tirada
            if jugador.posicion > 20:
                jugador.posicion = 20
            print(f"Avanza a la casilla {jugador.posicion}")
            # Hacer una pregunta y manejar el resultado
            resultado_pregunta = self.pregunta()
            if not resultado_pregunta:
                self.manejar_castigo(jugador)
            else:
                jugador.aciertos += 1
            # Verificar si el jugador ha ganado
            if jugador.posicion == 20:
                ganador = jugador
            turno += 1

        # Imprimir el resultado del juego
print(f"¡{ganador.nombre} ha ganado!")
print(f"{Juego.jugador1.nombre} respondió {self.jugador1.aciertos} preguntas correctamente y recibió {self.jugador1.castigos} castigos.")
print(f"{Juego.jugador2.nombre} respondió {self.jugador2.aciertos} preguntas correctamente y recibió {self.jugador2.castigos} castigos.")


tablero=Tablero()
tablero.imprimir_tablero()