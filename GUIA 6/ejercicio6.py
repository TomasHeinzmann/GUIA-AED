import random

def menorYpromedio():
	men = None
	prom = cantMen = 0
	for i in range(5000):
		randNum = random.randint(0, 100000)
		if men == None or randNum < men:
			men = randNum
		if randNum < 10000:
			prom += randNum
			cantMen += 1
	res = prom / cantMen
	print(f"El menor de los numeros generados es: {men}")
	print(f"El promedio de los numeros menores que 10000 es: {res}")
