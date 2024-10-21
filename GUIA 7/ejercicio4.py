import random

def hexanumeros():
	n = int(input("Ingrese cantidad de numeros a generar: "))
	for i in range(n):
		randNum = random.randint(50000, 450000)
		decimal = -1
		hexaNum = ""
		while decimal != 0:
			entero = randNum // 16
			decimal = randNum / 16 - entero
			decimal *= 16
			decimal = int(decimal)
			if decimal != 0:
				if  decimal <= 9:
					hexaNum += str(decimal)
				elif decimal == 10:
					hexaNum += "A"
				elif decimal == 11:
					hexaNum += "B"
				elif decimal == 12:
					hexaNum += "C"
				elif decimal == 13:
					hexaNum += "D"
				elif decimal == 14:
					hexaNum += "E"
				elif decimal == 15:
					hexaNum += "F"
				randNum = entero
		hexaNum = hexaNum[::-1]
		print(f"Numero hexadecimal: {hexaNum}")

hexanumeros()
		
