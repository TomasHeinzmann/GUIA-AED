import random

random.seed(95)

def problemaParcialNoTanBasico():
	numsMenorSegundo = numsMayorCuatro = porcent = 0
	numsSeis = numsNueve = numsAmbos = 0
	segundoNumero = None
	for i in range(45000):
		randNum = random.randint(1, 95000)
		# Punto 1
		if i == 1:
			segundoNumero = randNum
		elif segundoNumero != None and randNum < segundoNumero:
			numsMenorSegundo += 1
		else:
			pass
		# Punto 2
		if randNum % 6 == 0 and randNum % 9 == 0:
			numsAmbos += 1
		elif randNum % 6 == 0:
			numsSeis += 1
		elif randNum % 9 == 0:
			numsNueve += 1
		else:
			pass
		# Punto 3
		if randNum > numsMayorCuatro and randNum % 4 == 0:
			numsMayorCuatro = randNum
		else:
			pass
	# Punto 4
	porcent = numsMenorSegundo * 100 / 45000
	
	print(f"Cantidad de numeros menores al segundo numero: {numsMenorSegundo}")
	print(f"Cantidad de numeros multiplos de 6: {numsSeis}")
	print(f"Cantidad de numeros multiplos de 9: {numsNueve}")
	print(f"Cantidad de numeros multiplos de 6 y 9: {numsAmbos}")
	print(f"Mayor numero multiplo de 4 encontrado: {numsMayorCuatro}")
	print(f"Porcentaje de numeros del punto 1 sobre el total de numeros: {round(porcent)}%")
