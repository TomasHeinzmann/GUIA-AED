import random

random.seed(11)

def divisiblesCuatro():
	cuatroNoOcho = ambos = 0
	cantDosMil = acumDosMil = 0
	menoresPrimero = 0
	flag1 = False
	for i in range(1000):
		randNum = random.randint(1, 2500)
		# PUNTO 1
		if randNum % 4 == 0 and randNum % 8 != 0:
			cuatroNoOcho += 1
		elif randNum % 4 == 0 and randNum % 8 == 0:
			ambos += 1
		else:
			pass
		# PUNTO 2
		if randNum > 2000:
			cantDosMil += 1
			acumDosMil += randNum
		else:
			pass
		# PUNTO 3
		if i == 0:
			primero = randNum
		elif randNum < primero:
			menoresPrimero += 1
		else:
			pass
		# PUNTO 4
		if randNum == 1 or randNum == 2500:
			flag1 = True
		else:
			pass
	
	# CONTINUACION PUNTO 2
	promDosMil = acumDosMil / cantDosMil
	# CONTINUACION PUNTO 3
	porcent = (menoresPrimero * 100) / 1000
	
	print(f"Cantidad de numeros divisibles por 4 pero no por 8: {cuatroNoOcho}")
	print(f"Cantidad de numeros divisibles por 4 y 8: {ambos}")
	print(f"Promedio de los numeros mayores que 2000: {promDosMil}")
	print(f"Cantidad de numeros menores que el primero: {menoresPrimero}")
	print(f"Porcentaje de los numeros menores que el primero sobre el total: {porcent}")
	if flag1:
		print("En la secuencia aparecio uno de los extremos")
	else:
		print("En la secuencia no aparecio ninguno de los extremos")
		
divisiblesCuatro()
