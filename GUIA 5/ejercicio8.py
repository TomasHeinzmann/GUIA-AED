import random

def juegoDados():
	campPuntaje = int(input("Ingrese record del campeon: "))
	
	print("Empieza la primera ronda!")
	
	dado1 = random.randint(1, 6)
	dado2 = random.randint(1, 6)
	resultado = dado1 + dado2
	
	if resultado % 2 != 0:
		ret1 = resultado
		re2 = 0
		if ret1 > campPuntaje:
			print("El retador 1 supero al campeon!")
	else:
		ret2 = resultado
		ret1 = 0
		if ret2 > campPuntaje:
			print("El retador 2 supero al campeon!")
	
	print("Empieza la segunda ronda! ")
	
	dado1 = random.randint(1, 6)
	dado2 = random.randint(1, 6)
	resultado = dado1 + dado2
	
	dadoMay = max(dado1, dado2)
	dadoMen = min(dado1, dado2)
	
	if resultado % 2 != 0:
		ret1 += dadoMay
		ret2 -= dadoMen
	else:
		ret2 += dadoMay
		ret1 -= dadoMen
		
	if ret1 > campPuntaje:
		print("El retador 1 supero al campeon!")
	elif ret2 > campPuntaje:
		print("El retador 2 supero al campeon!")
		
	if (campPuntaje == ret1 and campPuntaje == ret2) or ret1 == ret2:
		print("Los retadores empataron")
	elif ret1 < campPuntaje > ret2:
		print("El campeon sigue invicto")
	elif ret1 > campPuntaje:
		print("El retador 1 le gano al campeon!")
	elif ret2 > campPuntaje:
		print("El retador 2 le gano al campeon!")
