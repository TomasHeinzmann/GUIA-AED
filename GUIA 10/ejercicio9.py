import random

def contadorPuntos(carta):
	if carta[0] == 1 or carta[0] == 2:
		if carta[1] >= 1 and carta[1] <= 3:
			return 1
		elif carta[1] >= 4 and carta[1] <= 6:
			return 2
		elif carta[1] >= 7 and carta[1] <= 9:
			return 3
		elif carta[1] >= 10 and carta[1] <= 12:
			return 4
	elif carta[0] == 3 or carta[0] == 4:
		if carta[1] >= 1 and carta[1] <= 3:
			return 4
		elif carta[1] >= 4 and carta[1] <= 6:
			return 3
		elif carta[1] >= 7 and carta[1] <= 9:
			return 2
		elif carta[1] >= 10 and carta[1] <= 12:
			return 1
def juegoDeCartas():
	n = int(input("Ingrese numero de rondas: "))
	jugador1 = []; jugador2 = []
	puntosJugador1 = 0; puntosJugador2 = 0
	for i in range(n):
		palo1 = random.randint(1, 4)
		palo2 = random.randint(1, 4)
		num1 = random.randint(1, 12)
		num2 = random.randint(1, 12)
		carta1 = [palo1, num1]
		carta2 = [palo2, num2]
		puntos1 = contadorPuntos(carta1)
		puntos2 = contadorPuntos(carta2)
		if puntos1 > puntos2:
			jugador1.append(carta1)
			jugador1.append(carta2)
		elif puntos2 > puntos1:
			jugador2.append(carta1)
			jugador2.append(carta2)
		elif (palo1 == 3 and palo2 == 3) or (palo1 != 3 and palo2 != 3):
			jugador1.append(carta1)
			jugador2.append(carta2)
	for carta in jugador1:
		puntos = contadorPuntos(carta)
		puntosJugador1 += puntos
	for carta in jugador2:
		puntos = contadorPuntos(carta)
		puntosJugador2 += puntos
	if puntosJugador1 > puntosJugador2:
		print("El jugador 1 es el triunfador!")
		print(f"Puntos jugador 1: {puntosJugador1}")
		print(f"Puntos jugador 2: {puntosJugador2}")
	else:
		print("El jugador 2 es el triunfador!")
		print(f"Puntos jugador 1: {puntosJugador1}")
		print(f"Puntos jugador 2: {puntosJugador2}")

juegoDeCartas()
	
