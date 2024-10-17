import random 

def promedioAleatorios():
	prom = 0
	for i in range(1000):
		randnum = random.randint(1, 100000)
		prom += randnum
	prom /= 1000
	print(f"El promedio de 1000 numero aleatorios (entre 1 y 100000) es {prom}")

promedioAleatorios()
