import random

def laberinto_del_raton():
	camino_raton = random.randint(1, 3)
	minutos = 0
	while camino_raton != 3:
		if camino_raton == 1:
			print("El raton sigue en la jaula, luego de 3 minutos")
			minutos += 3
		elif camino_raton == 2:
			print("El raton sigue en la jaula, luego de 5 minutos")
			minutos += 5
		camino_raton = random.randint(1, 3)
	print("El raton sale de la jaula, luego de 7 minutos")
	minutos += 7
	print(f"El raton se libero! Tardo {minutos} minutos en salir!")

laberinto_del_raton()
