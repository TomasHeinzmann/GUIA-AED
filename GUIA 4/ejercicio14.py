import random

def pasoPeaje():
	patente = input("Ingrese patente del vehiculo: ")
	randnum = random.randint(0, 9)
	if int(patente[len(patente)-1]) == randnum:
		monto = 50
	else:
		monto = 90
	if int(patente[len(patente)-1]) == 7:
		monto -= monto * 0.50
	else:
		monto -= monto * 0.10
	
	print(f"El monto a pagar es {monto}")

pasoPeaje()
