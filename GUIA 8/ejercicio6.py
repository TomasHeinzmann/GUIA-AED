import random
def menu():
	print("*********************MENU DE OPCIONES*********************")
	print("1) Calcular promedio de numeros cargados")
	print("2) Determinar valores positivos y negativos")
	print("3) Nota de un alumno")
	print("0) Salir")
	print("**********************************************************")
	opc = int(input("Ingrese una opcion: "))
	while not (3 >= opc >= 0):
		print("Error, el valor ingresado se sale de los parametros")
		opc = int(input("Ingrese una opcion: "))
	return opc

def principal():
	opc = -1
	while opc != 0:
		opc = menu()
		if opc == 1:
			n = 0
			prom = cantCarg = 0
			while n != -1:
				n = int(input("Ingrese numero a cargar (-1 termina): "))
				prom += n
				cantCarg += 1
			prom = prom / cantCarg
			print(f"El promedio de los numeros cargados es: {round(prom, 2)}")
		elif opc == 2:
			n = int(input("Ingrese cantidad de numeros a generar: "))
			cantPos = cantNeg = 0
			for i in range(n):
				randNum = random.randint(-100, 100)
				if randNum > 0:
					cantPos += 1
				else: 
					cantNeg += 1
			print(f"Numeros positivos: {cantPos}")
			print(f"Numeros negativos: {cantNeg}")
		elif opc == 3:
			nota = int(input("Ingrese nota del alumno: "))
			while not (10 >= nota >= 1):
				print("Error, la nota se sale de los parametros")
				nota = int(input("Ingrese nota del alumno: "))
			if nota >= 4:
				print("El alumno esta aprobado")
			else:
				print("El alumno esta desaprobado")
		else:
			print("Gracias por usar el programa!")
