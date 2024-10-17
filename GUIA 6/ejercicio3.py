import random

def opciones():
	print("************************MENU DE OPCIONES************************")
	print("1) Promedio de 1000 numeros aleatorios entre 1 y 100000")
	print("2) Buscar el mayor de 10000 numeros aleatorios entre 1 y 100000")
	print("3) Buscar el menor de 5000 numeros aleatorios entre 1 y 100000, y promedio de los menores que 10000")
	print("Presione otro numero para salir del programa")
	print("****************************************************************")
	opc = int(input("Ingrese una opcion: "))
	return opc

def menuOpciones():
	opc = -1
	while opc == -1 or 1 <= opc <= 3:
		opc = opciones()
		if opc == 1:
			prom = 0
			for i in range(1000):
				randnum = random.randint(1, 100000)
				prom += randnum
			prom /= 1000
			print(f"El promedio en esta instancia es de: {prom}")
		elif opc == 2:
			may = 0
			for i in range(1, 100000):
				randnum = random.randint(1, 100000)
				if randnum > may:
					may = randnum
			print(f"El mayor de entre todos los numeros es {may}")
		elif opc == 3:
			men = 100000
			prom = cantMen = 0
			for i in range(5000):
				randnum = random.randint(1, 100000)
				if randnum < men:
					men = randnum
				if randnum < 10000:
					prom += randnum
					cantMen += 1
			print(f"El menor de entre todos los numeros es {men}")
			print(f"El promedio de todos los numeros menores que 10000 es {men}")
		else:
			print("Gracias por usar el programa!")

menuOpciones()
			
