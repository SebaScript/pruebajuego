import random

tablero = []

for i in range(1, 21, 5):
    fila = list(range(i, i + 5))
    tablero.append(fila)

def dibujar_tablero(tablero, jugador1, jugador2):
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if jugador1 == (i, j):
                print('X', end='\t')
            elif jugador2 == (i, j):
                print('O', end='\t')
            else:
                print(tablero[i][j], end='\t')
        print()
print(tablero)

preguntas = [
    {
        'pregunta': '¿Cuál es la capital de España?',
        'respuestas': ['a) Madrid', 'b) Barcelona', 'c) Valencia'],
        'respuesta_correcta': 'a'
    },

    {
        'pregunta': '¿Cuál es el lugar más frío de la Tierra??',
        'respuestas': ['a) Antártida', 'b) Finlandia.', 'c) Alaska'],
        'respuesta_correcta': 'a'
    },


    {
        'pregunta': '¿Cuál es el lugar organo que consume más energía en el cuerpo humano??',
        'respuestas': ['a) Corazón', 'b) Cerebro.', 'c) Pancreas'],
        'respuesta_correcta': 'b'
    },


    {
        'pregunta': '¿Cuál es el país más pequeño del mundo??',
        'respuestas': ['a) Nauru', 'b) Mónaco.', 'c) Vaticano'],
        'respuesta_correcta': 'c'
    },



    {
        'pregunta': '¿Cuál es la formula del hierro??',
        'respuestas': ['a) Fe2O3', 'b) Fe4O5.', 'c) H2O'],
        'respuesta_correcta': 'a'
    },



    {
        'pregunta': '¿Quién pinto la monaliza??',
        'respuestas': ['a) Pablo picasso', 'b) Van Gogh.', 'c) Leonardo Da Vinci'],
        'respuesta_correcta': 'c'
    },



    {
        'pregunta': '¿Qué planeta del sistema solar tiene más lunas??',
        'respuestas': ['a) Júpiter', 'b) Marte.', 'c) Saturno'],
        'respuesta_correcta': 'a'
    },


    {
        'pregunta': '¿Quién fue el auténtico padre de la electricidad??',
        'respuestas': ['a) Thomas Edison', 'b) Nikola Tezla.', 'c) Albert Einstein'],
        'respuesta_correcta': 'b'
    },

    {
        'pregunta': '¿Qué colores tiene la bandera de Paraguay, en orden de arriba hacía abajo??',
        'respuestas': ['a)Rojo,azúl y blanco ', 'b) blanco, rojo y azúl.', 'c)Rojo,blanco y azúl'],
        'respuesta_correcta': 'c'
    },


    {
        'pregunta': '¿En qué año fue la Revolución Francesa?',
        'respuestas': ['a) 1789', 'b) 1815', 'c) 1848'],
        'respuesta_correcta': 'a'
    },
    {
        'pregunta': '¿Cuál es el metal más pesado?',
        'respuestas': ['a) Hierro', 'b) Plomo', 'c) Oro'],
        'respuesta_correcta': 'b'
    },
    {
        'pregunta': 'En que año se fundo la ciudad de Medellin?',
        'respuestas': ['a) 7809 a.c', 'b) 1508', 'c) 1650'],
        'respuesta_correcta' : 'c'
    },
    {
        'pregunta': '¿Cuál es el continente más poblado?',
        'respuestas': ['a) asia', 'b) europa', 'c) america'],
        'respuesta_correcta': 'a'
    }
]

def lanzar_dado():
    return random.randint(1, 6)

def hacer_pregunta():
    pregunta = random.choice(preguntas)
    print(pregunta['pregunta'])
    for respuesta in pregunta['respuestas']:
        print(respuesta)
    respuesta_jugador = input('Elige una respuesta (a, b o c): ')
    if respuesta_jugador == pregunta['respuesta_correcta']:
        print('¡Correcto!')
        return True
    elif respuesta_jugador != "a" or "b" or "c":
        print("Respuesta invalida")
    else:
        print('¡Incorrecto!')
        return False


#Si el resultado es 1, el castigo es puente, 2 es resbalon y 3 es calavera

def aplicar_castigo(posicion_jugador, tipo_castigo):

    castigos = ['puente', 'resbalon', 'calavera']
    tipo_castigo = random.choice(castigos)

    if tipo_castigo == 'puente':
        nueva_posicion = posicion_jugador - 3
    elif tipo_castigo == 'resbalon':
        nueva_posicion = posicion_jugador - 2
    elif tipo_castigo == 'calavera':
        nueva_posicion = 1
    else:
        # En caso de que se proporcione un tipo de castigo inválido
        nueva_posicion = posicion_jugador

    # Si la nueva posición es menor que 1, el jugador se devuelve a la casilla 1
    if nueva_posicion < 1:
        nueva_posicion = 1

    print(f'{tipo_castigo}! pasas de la posicion {posicion_jugador} a la posicion {nueva_posicion}')
    return nueva_posicion

jugador1 = {'nombre': 'Jugador 1', 'posicion': 0, 'aciertos': 0}
jugador2 = {'nombre': 'Jugador 2', 'posicion': 0, 'aciertos': 0}

while True:
    # Turno del jugador 1
    print(f'Turno de {jugador1["nombre"]}')
    lanzamiento = lanzar_dado()
    print(f'Lanzamiento: {lanzamiento}')
    jugador1['posicion'] += lanzamiento
    if jugador1['posicion'] >= 20:
        print(f'{jugador1["nombre"]} ha ganado!')
        break
    if hacer_pregunta():
        jugador1['aciertos'] += 1
    else:
        jugador1['posicion'] = aplicar_castigo(jugador1['posicion'], 2)
    print(f'Posición actual: {jugador1["posicion"]}, Aciertos: {jugador1["aciertos"]}')

    # Turno del jugador 2
    print(f'Turno de {jugador2["nombre"]}')
    lanzamiento = lanzar_dado()
    print(f'Lanzamiento: {lanzamiento}')
    jugador2['posicion'] += lanzamiento
    if jugador2['posicion'] >= 20:
        print(f'{jugador2["nombre"]} ha ganado!')
        break
    if hacer_pregunta():
        jugador2['aciertos'] += 1
    else:
        jugador2['posicion'] = aplicar_castigo(jugador2['posicion'], 2)
    print(f'Posición actual: {jugador2["posicion"]}, Aciertos: {jugador2["aciertos"]}')
