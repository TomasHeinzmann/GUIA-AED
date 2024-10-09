import random

def tarjetaBingo ():
	tarjeta = []
	for _ in range(15):
		randnum = random.randint(1, 100)
		tarjeta.append(randnum)
	num1 = int(input("Ingrese primer numero: "))
	num2 = int(input("Ingrese segundo numero: "))
	num3 = int(input("Ingrese ultimo numero: "))
	
	if num1 in tarjeta or num2 in tarjeta or num3 in tarjeta:
		print("El jugador marco algun numero de la tarjeta")
	else:
		print("El jugador tiene mala suerte, no marco ninguna casilla")
	

