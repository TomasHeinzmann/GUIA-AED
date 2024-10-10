import random

# 1 - espadas
# 2 - basto
# 3 - copa
# 4 - oro

# 1, 7, 3, 2, 12, 11, 6, 5, 4
# 1, 3, 2, 12, 11, 7, 6, 5, 4
# 3, 2, 1, 12, 11, 7, 6, 5, 4
# 7, 3, 2, 1, 12, 11, 6, 5, 4


def cartasTruco ():
	mano = []
	for _ in range(3):
		numero = random.randint(1, 9)
		palo = random.randint(1, 4)
		carta = [numero, palo]
		mano.append(carta)
	print("Cartas en mano")
	print(mano)
	for carta in mano:
		if carta[0] == 1 and carta[1] == 1:
			print("Tenes el as de espadas! ")
	
	if mano[0][1] == mano[1][1] == mano[2][1]:
		print("Las cartas son del mismo palo! ")
		puntos = [0, 0, 0]
		if mano[0][1] == 1:
			indiceCounter = 0
			for carta in mano:
				punto = 0
				if 4 <= carta[0] <= 6:
					punto = 1
				elif carta[0] == 2 or carta[0] == 12 or carta[0] == 11:
					punto = 2
				elif carta[0] == 1 or carta[0] == 7 or carta[0] == 3:
					punto = 3
				puntos[indiceCounter] += punto
				indiceCounter += 1
				
		elif mano[0][1] == 2:
			indiceCounter = 0
			for carta in mano:
				if 4 <= carta[0] <= 6:
					punto = 1
				elif carta[0] == 12 or carta[0] == 11 or carta[0] == 7:
					punto = 2
				elif carta[0] == 1 or carta[0] == 3 or carta[0] == 2:
					punto = 3
				puntos[indiceCounter] += punto
				indiceCounter += 1
		
		elif mano[0][1] == 3:
			indiceCounter = 0
			for carta in mano:
				if 4 <= carta[0] <= 6:
					punto = 1
				elif carta[0] == 12 or carta[0] == 11 or carta[0] == 7:
					punto = 2
				elif carta[0] == 1 or carta[0] == 3 or carta[0] == 2:
					punto = 3
				puntos[indiceCounter] += punto
				indiceCounter += 1
		
		elif mano[0][1] == 4:
			indiceCounter = 0
			for carta in mano:
				if 4 <= carta[0] <= 6:
					punto = 1
				elif carta[0] == 12 or carta[0] == 11 or carta[0] == 1:
					punto = 2
				elif carta[0] == 7 or carta[0] == 3 or carta[0] == 2:
					punto = 3
				puntos[indiceCounter] += punto
				indiceCounter += 1	
		
		mayor = max(puntos[0], puntos[1], puntos[2])
		cartamayor = puntos.index(mayor)
		
		print(f"La carta con mayor valor de la mano fue: {mano[cartamayor]}")
		
	else:
		print("Las cartas son de distinto palo! ")
	
		
cartasTruco()
