def menu():
	print("********************MENU DE OPCIONES********************")
	print("1) Tabla de multiplicar")
	print("2) Mayor y menor ")
	print("3) Multiplos")
	print("4) Texto")
	print("0) - Salir")
	opc = int(input("Ingrese una opcion: "))
	while opc < 0 or opc > 4:
		print("Error. El valor ingresado se sale de los parametros")
		opc = int(input("Ingrese una opcion: "))
	return opc 

def principal():
	opc = -1
	while opc != 0:
		opc = menu()
		if opc == 1:
			n = int(input("Ingrese un numero entre 0 y 10: "))
			while n > 10 or n < 0:
				print("Error. El valor ingresado debe estar entre 0 y 10")
				n = int(input("Ingrese un numero entre 0 y 10: "))
			for i in range(10):
				res = n * (i + 1)
				print(f"n por {i + 1}: {res}")
		elif opc == 2:
			mayor = None ; menor = None
			n = -1
			while n != 0:
				n = int(input("Ingrese numero de la sucesion: "))
				if n < 0:
					print("Error. Los numeros deben ser positivos")
					n = int(input("Ingrese numero de la sucesion: "))
				if mayor == None:
					mayor = n
				elif n > mayor:
					mayor = n
				if menor == None:
					menor = n
				elif n < menor and n != 0:
					menor = n
			print(f"El mayor numero de la secuencia es: {mayor}")
			print(f"El menor numero de la secuencia es: {menor}")
		elif opc == 3:
			a = int(input("Ingrese el valor de 'a': "))
			b = int(input("Ingrese el valor de 'b': "))
			multiA = 0
			while a < 0 or b < a:
				print("Error. A no puede ser menor que 0 y B no puede ser menor que A")
				a = int(input("Ingrese el valor de 'a': "))
				b = int(input("Ingrese el valor de 'b': "))
			for num in range(a, b + 1):
				if num % a == 0 and num != a:
					multiA += num
			print(f"La suma de los multiplos de 'a' es: {multiA}")
		elif opc == 4:
			texto = input("Ingrese texto a analizar: ")
			cantPalabras = 0; ultLetra = None; cantVocales = 0
			vocales = "AaáÁEeéÉIiíÍOoóÓUuúÚ"
			for caracter in texto:
				if caracter == " " or caracter == ".":
					cantPalabras += 1
					if ultLetra in vocales:
						cantVocales += 1
				else:
					ultLetra = caracter
			porcent = cantVocales * 100 // cantPalabras
			print(f"Porcentaje de palabras que terminan en vocal: {porcent}%")
	print("Gracias por usar el programa!")
