import random

preguntas = [
    ("¿Cuál es la capital de España?", ["a) Madrid", "b) Barcelona", "c) Valencia"], "a"),
    ("¿Quién escribió el Quijote?", ["a) Miguel de Cervantes", "b) Pablo Neruda", "c) Gabriel García Márquez"], "a"),
    ("¿Cuál es el río más largo del mundo?", ["a) Amazonas", "b) Nilo", "c) Yangtze"], "b"),
    ("¿Cuál es el continente más poblado?", ["a) Asia", "b) Europa", "c) África"], "a"),
    ("¿En qué país se encuentra la Torre Eiffel?", ["a) Francia", "b) Italia", "c) España"], "a"),
    ("¿Qué metal es líquido a temperatura ambiente?", ["a) Oro", "b) Hierro", "c) Mercurio"], "c"),
    ("¿En que año se fundó la ciudad de Medellín", ["a) 7692 a.c", "b) 1650", "c) 1509"], "b"),
    ("¿Cual es el sistema de transporte masivo de Cali?", ["a) TransMilenio", "b) MIO", "c) si"], "b")
     ]


class Tablero:
  def __init__(self):
    self.filas = 4
    self.columnas = 5
    self.jugadores = {}  # Para almacenar las posiciones de cada jugador
    self.meta = (3, 4)  # La casilla de la meta
    self.turno = 1  # Jugador 1 comienza primero

    # Inicializar las posiciones de los jugadores al inicio del juego
    self.jugadores[1] = (0, 0)  # Jugador 1 empieza en la casilla (0, 0)
    self.jugadores[2] = (0, 0)  # Jugador 2 empieza en la casilla (0, 0)

    def mover_jugador(self, jugador, casillas):
        self.jugadores[jugador] += casillas
        if self.jugadores[jugador] > self.meta:
            self.jugadores[jugador] = self.meta - (self.jugadores[jugador] - self.meta)
        elif self.jugadores[jugador] in [5, 9, 14, 18]:
            self.jugadores[jugador] = self.avanzar_por_casilla_especial(self.jugadores[jugador])
        return self.imprimir_tablero()

  def imprimir(self):
    # Mostrar el tablero en la consola
    print("+" + "---+" * self.columnas)
    for fila in range(self.filas):
      print("|", end="")
      for columna in range(self.columnas):
        jugador = None
        for j, pos in self.jugadores.items():
          if pos == (fila, columna):
            jugador = j
            break
        if jugador is not None:
          # Mostrar el número del jugador en la casilla
          print(f" {jugador} |", end="")
        elif (fila, columna) == self.meta:
          # Mostrar la casilla de la meta con una "M"
          print(" M |", end="")
        else:
          # Mostrar una casilla vacía
          print("   |", end="")
      print("\n+" + "---+" * self.columnas)


class Juego:
    def __init__(self):
        self.tablero = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20]
        ]
        self.jugadores = {1: (0, 0), 2: (0, 0)}
        self.meta = (3, 4)
        self.turno = 1
        self.aciertos = {1: 0, 2: 0}

    def mover_jugador(self, jugador, pasos):
        fila, columna = self.jugadores[jugador]
        nuevo_columna = columna + pasos
        if nuevo_columna >= 5:
            fila += nuevo_columna // 5
            columna = nuevo_columna % 5
        else:
            columna = nuevo_columna
        self.jugadores[jugador] = (fila, columna)

    def jugar_turno(self):
        # Seleccionar un jugador aleatorio
        jugador = self.jugadores[self.turno]

        # Tirar el dado y mover al jugador
        dado = random.randint(1, 6)
        print(f"Jugador {self.turno} tiró el dado y obtuvo {dado}")
        self.mover_jugador(self.turno, dado)

        # Seleccionar una pregunta aleatoria
        pregunta, opciones, respuesta = random.choice(preguntas)
        print(pregunta)
        for opcion in opciones:
            print(opcion)

        # Pedir al jugador que ingrese su respuesta
        while True:
            entrada = input("Ingrese su respuesta (a, b o c): ")
            if entrada in ["a", "b", "c"]:
                break

        # Verificar si la respuesta es correcta
        if entrada == respuesta:
            print("Respuesta correcta")
            self.aciertos[self.turno] += 1
        else:
            print("Respuesta incorrecta")
            castigo = random.choice(["puente", "resbalón", "calavera"])
            if castigo == "puente":
                print("¡Ups! Cae en un puente y retrocede 3 casillas")
                self.mover_jugador(self.turno, -3)
            elif castigo == "resbalón":
                print("¡Ups! Resbala y retrocede 2 casillas")
                self.mover_jugador(self.turno, -2)
            elif castigo == "calavera":
                print("¡Ups! Encuentra una calavera y retrocede al inicio")
                self.jugadores[self.turno] = (0, 0)

        # Mostrar el estado actual del tablero

        # Verificar si el jugador ha llegado a la casilla de la meta
        if self.jugadores[self.turno] == self.meta:
            print(f"¡Jugador {self.turno} ha ganado!")
        else:
            # Actualizar el turno al otro jugador
            self.turno = 3 - self.turno




juego = Juego()
while juego.jugadores[1] != juego.meta and juego.jugadores[2] != juego.meta:
    juego.jugar_turno()
    tablero = Tablero()
    tablero.imprimir()
