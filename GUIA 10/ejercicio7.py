def menu():
	print("*******************MENU DE OPCIONES*******************")
	print("1) Sucesion de numeros enteros positivos")
	print("2) Analisis de intervalo")
	print("3) Numeros contiguos pares de una secuencia")
	print("0) - Salir")
	print("******************************************************")
	opc = int(input("Ingrese una opcion: "))
	while opc > 3 and opc < 0: 
		print("Error, el valor ingresado se sale de los parametros")
		opc = int(input("Ingrese una opcion: "))
	return opc

def principal():
	opc = -1
	while opc != 0:
		opc = menu()
		if opc == 1:
			n = 1
			cantNums = 0 ; cantMulti = 0
			while n != 0:
				n = int(input("Cargue un numero: "))
				while n < 0:
					print("Error, el valor ingresado debe ser mayor que cero")
					n = int(input("Cargue un numero: "))
				if n != 0:
					cantNums += 1
					if cantNums == 1:
						primero = n
					elif n % primero == 0:
						cantMulti += 1
			print(f"Multiplos del primer numero de la secuencia: {cantMulti}")
		elif opc == 2:
			fueraInt = 0; dentroInt = 0; paresDentroInt = 0
			p = int(input("Ingrese valor de 'p': "))
			q = int(input("Ingrese valor de 'q': "))
			while p > q or p < 0:
				print("Error los valores ingresados deben ser '0 < p < q'")
				p = int(input("Ingrese valor de 'p': "))
				q = int(input("Ingrese valor de 'q': "))
			n = -1
			while n != 0:
				n = int(input("Ingrese numeros para comparar con el intervalo: "))
				if n != 0:
					if n < 0:
						print("Error, el valor ingresado debe ser mayor que cero")
						n = int(input("Ingrese numeros para comparar con el intervalo: "))
					elif  n > q or n < p:
						fueraInt += 1
					elif n > p and n < q:
						dentroInt += 1
						if n % 2 == 0:
							paresDentroInt += 1	
			print(f"Numeros dentro del intervalo: {dentroInt}")
			print(f"Numeros pares dentro del intervalo: {paresDentroInt}")
			print(f"Numeros fuera del intervalo: {fueraInt}")
		elif opc == 3:
			n = -1 ; antNum = None ; flagPares = False ; pares = 0 ; cantPares = 0
			while n <= 100:
				n = int(input("Ingrese un valor: "))
				if n <= 100:
					if n < 0:
						print("Error, el valor ingresado debe ser mayor que cero")
						n = int(input("Ingrese un valor: "))
					elif antNum != None and antNum % 2 == 0 and n % 2 == 0:
						flagPares = True
					if n % 2 == 0:
						pares += n
						cantPares += 1
					antNum = n
			if flagPares:
				prom = pares // cantPares
				print("Aparecieron dos numeros pares contiguos!")
				print(f"El promedio de ellos es: {prom}")
			else:
				print("No aparecieron numeros pares contiguos")
	print("Gracias por usar el programa!")

principal()
