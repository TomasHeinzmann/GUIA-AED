import random

def caraCruz ():
	opcion = int(input("Ingrese opcion (1-cara, 2-cruz): "))
	moneda = random.randint(1, 2)
	if opcion == moneda:
		print("El jugador acerto")
	else:
		print("El jugador no acerto")
		
