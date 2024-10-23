import random

random.seed(37)

def parcialComplicado():
	numsNegNeg = numsNegPos = numsPosNueve = 0
	cantPunto2 = promPunto2 = 0
	mayorPunto3 = -30000
	divisiblesSiete = 0
	for i in range(27000):
		randNum = random.randint(-20000, 30000)
		# Punto 1
		if -20000 <= randNum < -5000:
			numsNegNeg += 1
		elif -5000 <= randNum < 15000:
			numsNegPos += 1
		elif randNum >= 15000 and randNum % 9 == 0:
			numsPosNueve += 1
		else:
			pass
		# Punto 2
		if randNum >= 1000 and (randNum % 10 == 4 or randNum % 10 == 6):
			cantPunto2 += 1
			promPunto2 += randNum
		else:
			pass
		# Punto 3
		if randNum > 0 and randNum % 2 != 0 and randNum % 10 != 1 and mayorPunto3:
			mayorPunto3 = randNum
		else:
			pass
		# Punto 4
		if randNum % 7 == 0:
			divisiblesSiete += 1
		else:
			pass
	
	# Continuacion del punto 2
	promedio = promPunto2 // cantPunto2
	# Continuacion del punto 4
	porcent = (divisiblesSiete * 100) // 27000
	
	print(f"Numeros mayores o iguales a -20000 pero menores que -5000: {numsNegNeg}")
	print(f"Numeros mayores o iguales a -5000 pero menores que 15000: {numsNegPos}")
	print(f"Numeros mayores o iguales a 15000 y multiplos de 9: {numsPosNueve}")
	print(f"Promedio de numeros mayores o iguales a 1000 que terminan en 4 o 6: {promedio}")
	print(f"Porcentaje de numeros divisibles por 7 sobre el total de numeros: {porcent}%")	
