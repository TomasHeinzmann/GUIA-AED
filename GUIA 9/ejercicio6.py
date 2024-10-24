import random
random.seed(20220512)

def ejercicioTipoParcial():
	multiTres = multiCincoNoTres = multiNinguno = 0
	mayUno = 0
	multiOncePar = cantOncePar = 0
	for i in range(25000):
		randNum = random.randint(1, 45000)
		# PUNTO 1
		if randNum % 3 == 0:
			multiTres += 1
		elif randNum % 5 == 0 and randNum % 3 != 0:
			multiCincoNoTres += 1
		else:
			multiNinguno += 1
		# PUNTO 2
		stringRandNum = str(randNum)
		if stringRandNum[0] == "1" and randNum > mayUno:
			mayUno = randNum
		else:
			pass
		# PUNTO 3
		if randNum % 2 == 0 and randNum % 11 == 0:
			multiOncePar += randNum
			cantOncePar += 1
		else:
			pass
	# CONTINUACION PUNTO 3
	prom = multiOncePar // cantOncePar
	# PUNTO 4
	porcentTres = (multiTres * 100) // 25000
	porcentCinco = (multiCincoNoTres * 100) // 25000
	porcentNinguno = (multiNinguno * 100) // 25000
	
	print(f"Punto 1 (multiplos de 3): {multiTres}")
	print(f"Punto 1 (multiplos de 5 pero no de 3): {multiCincoNoTres}")
	print(f"Punto 1 (ni multiplos de 5 ni de 3): {multiNinguno}")
	print(f"Punto 2: {mayUno}")
	print(f"Punto 3: {prom}")
	print(f"Punto 4 (multiplos de 3): {porcentTres}%")
	print(f"Punto 4 (multiplos de 5 pero no de 3): {porcentCinco}%")
	print(f"Punto 4 (ni multiplos de 5 ni de 3): {porcentNinguno}%")
ejercicioTipoParcial()
