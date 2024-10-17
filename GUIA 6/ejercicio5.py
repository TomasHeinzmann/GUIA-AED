import random

def mayorRandom():
	may = None
	cantPos = 0
	for i in range(10000):
		randnum = random.randint(-100000, 100000)
		if may == None or may < randnum:
			may = randnum
		if randnum > 0:
			cantPos += 1
	cantPos *= 100 / 10000
	print(f"Porcentaje de numeros positivos: {cantPos}%")
	print(f"Mayor numero aleatorio: {may}")
		
	
mayorRandom()
