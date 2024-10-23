import random

random.seed(76)

def problemaParcial():
	cantPares = mayoresPrimero = dosMil = porcent = 0
	for i in range(5000):
		randNum = random.randint(1, 65000)
		# Punto 1
		if randNum % 2 == 0 and randNum % 6 == 0:
			cantPares += 1
		else:
			pass
		# Punto 2
		if i == 0:
			primerNumero = randNum
		elif randNum > primerNumero:
			mayoresPrimero += 1
		else:
			pass
		# Punto 3
		if 2000 <= randNum <= 2999:
			dosMil += 1
		else:
			pass
	# Punto 4
	porcent = mayoresPrimero * 100 / 5000
	
	print(f"Cantidad de numeros pares multiplos de 6: {cantPares}")
	print(f"Cantidad de numeros mayores al primero: {mayoresPrimero}")
	print(f"Cantidad de numeros en el seguindo millar: {dosMil}")
	print(f"Porcentaje del punto 2 sobre el total de numeros: {round(porcent)}%")
