def menu():
	print("*********************MENU DE OPCIONES*********************")
	print("1) Suma de cuadrados")
	print("2) Contar palabras con vocales al final")
	print("3) Determinar si el mayor es par o impar")
	print("0) Salir")
	print("**********************************************************")
	opc = int(input("Ingrese una opcion dentro de los parametros: "))
	while not (3 >= opc >= 0):
		print("Error. Ingrese una opcion valida")
		opc = int(input("Ingrese una opcion dentro de los parametros: "))
	return opc

def principal():
	opc = -1
	while opc != 0:
		opc = menu()
		if opc == 1:
			n = int(input("Ingrese hasta que numero hacer la suma: "))
			while n <= 0:
				print("Error. el numero no puede ser menor o igual a cero")
				n = int(input("Ingrese hasta que numero hacer la suma: "))
			sumCuadrados = 0
			for i in range(n):
				cuadrado = i ** 2
				sumCuadrados += cuadrado
			print(f"El resultado es: {sumCuadrados}")
		elif opc == 2:
			vocales = "AaáÁEeéÉIiíÍOóÓUuúÚ"
			texto = input("Ingrese un texto finalizado con un punto: ")
			cantVocales = 0
			for caracter in texto:
				if caracter == " " or caracter == ".":
					if caracterAnterior in vocales:
						cantVocales += 1
				else:
					caracterAnterior = caracter
			print(f"Cantidad de palabras que terminan en vocal: {cantVocales}")
		elif opc == 3:
			listNums = []
			carga = -1
			pares = impares = 0
			while carga != 0:
				carga = int(input("Ingrese un numero a cargar (con 0 finaliza): "))
				listNums.append(carga)
			for numero in listNums:
				if numero % 2 == 0:
					pares += 1
				else:
					impares += 1
			if pares > impares:
				print("Hay mas numero pares que impares")
			else:
				print("Hay mas numeros impares que pares")
		else:
			print("Gracias por usar el programa!")

principal()
