import random
def mayMen():
	may = men = None
	for i in range(8):
		randNum = random.randint(1, 100)
		print(randNum)
		if randNum % 2 == 0:
			if may == None or randNum > may:
				may = randNum
		elif randNum % 2 != 0:
			if men == None or randNum < men:
				men = randNum
	print(f"El mayor par es: {may}")
	print(f"El menor impar es: {men}")
mayMen()
