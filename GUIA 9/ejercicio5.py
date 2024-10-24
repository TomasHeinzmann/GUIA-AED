import random

random.seed(49)

def simulacroParcial():
	multiCinco = multiSiete = multiNueve = 0
	mayUltimoDigito = 0
	paresMenores = 0
	for i in range(20000):
		randNum = random.randint(1, 45000)
		# PUNTO 1
		if randNum % 5 == 0:
			multiCinco += 1
		else:
			pass
		if randNum % 7 == 0:
			multiSiete += 1
		else:
			pass
		if randNum % 9 == 0:
			multiNueve += 1
		else:
			pass
		# PUNTO 2
		if randNum % 10 >= 5 and randNum % 10 <= 8 and randNum > mayUltimoDigito:
			mayUltimoDigito = randNum
		else:
			pass
		# PUNTO 3
		if randNum % 2 == 0 and randNum < 15000:
			paresMenores += 1
		else:
			pass
	# PUNTO 4
	porcent = (paresMenores * 100) // 20000
	
	print(f"Punto 1 (multiplos de 5): {multiCinco}")
	print(f"Punto 1 (multiplos de 7): {multiSiete}")	
	print(f"Punto 1 (multiplos de 9): {multiNueve}")	
	print(f"Punto 2: {mayUltimoDigito}")
	print(f"Punto 3: {paresMenores}")	
	print(f"Punto 4: {porcent}%")		

simulacroParcial() 
