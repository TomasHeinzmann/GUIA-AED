import random

def secuenciaAleatoria():
	n = int(input("Ingrese cantidad de numeros a generar: "))
	while n == 0:
		print("Error, el valor ingresado debe ser mayor a cero")
		n = int(input("Ingrese cantidad de numeros a generar: "))
	
	terminaCinco = pares = menorTres = primerCantidad = 0
	
	for i in range(n):
		randNum = random.randint(1, 1000)
		if randNum % 10 == 5:
			terminaCinco += 1
		else:
			pass
		if randNum % 2 == 0:
			pares += 1
		else:
			pass
		if randNum % 3 == 0 and randNum < menorTres:
			menorTres = randNum
		else:
			pass
		if i == 0:
			primero = randNum
		elif randNum == primero:
			primerCantidad += 1
		else:
			pass
	
	porcent = pares * 100 // n
	
	print(f"Cantidad de numeros que terminan en 5: {terminaCinco}")
	print(f"Porcentaje de numeros pares de la secuencia: {porcent}%")
	print(f"Menor numero multiplo de 3 de la secuencia: {menorTres}")
	print(f"Cantidad de veces que aparece el primer numero en la secuencia: {primerCantidad}")

secuenciaAleatoria()
