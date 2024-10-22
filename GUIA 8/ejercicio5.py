import random
def menu():
	print("***************MENU DE OPCIONES***************")
	print("1) Girar al norte y avanzar 10 pasos")
	print("2) Girar al sur y avanzar 10 pasos")
	print("3) Girar al este y avanzar 10 pasos")
	print("4) Girar al oeste y avanzar 10 pasos")
	print("0) Salir")
	opc = int(input("Ingrese una opcion: "))
	while not (4 >= opc >= 0):
		print("Error, la opcion no esta entre los parametros")
		opc = int(input("Ingrese una opcion: "))
	return opc

def titoRobot():
	opc = -1
	inicioX = random.randint(1, 10)
	inicioY = random.randint(1, 10)
	while opc != 0:
		opc = menu()
		if opc == 1:
			print(f"Tito avanza desde el punto ({inicioX}, {inicioY})")
			inicioY += 10
		elif opc == 2:
			print(f"Tito avanza desde el punto ({inicioX}, {inicioY})")
			inicioY -= 10
		elif opc == 3:
			print(f"Tito avanza desde el punto ({inicioX}, {inicioY})")
			inicioX += 10
		elif opc == 4:
			print(f"Tito avanza desde el punto ({inicioX}, {inicioY})")
			inicioX -= 10
		else:
			print(f"Tito se quedo en ({inicioX}, {inicioY})")
			print("Gracias por usar el programa!")

