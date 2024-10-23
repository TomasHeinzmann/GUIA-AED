import random
def menu():
	print("********************MENU DE OPCIONES********************")
	print("1) Secuencia de numeros")
	print("2) Analizar texto")
	print("3) Analizar notas de alumnos")
	print("0) Salir")
	print("********************************************************")
	opc = int(input("Ingrese una opcion: "))
	while opc > 3 or opc < 0:
		print("Error, el valor ingresado se sale de los parametros")
		opc = int(input("Ingrese una opcion: "))
	return opc

def principal():
	opc = -1
	while opc != 0:
		opc = menu()
		if opc == 1:
			n = int(input("Ingrese cantidad de numeros a generar: "))
			multiTresCinco = 0
			while n <= 0:
				print("Error, el valor ingresado debe ser mayor a cero")
				n = int(input("Ingrese cantidad de numeros a generar: "))
			for i in range(n):
				randNum = random.randint(1, 1000)
				if randNum % 3 == 0 and randNum % 5 == 0:
					multiTresCinco += 1
			porcent = multiTresCinco * 100 // n
			print(f"El porcentaje de los multiplos de 3 y 5 es: {porcent}%")
		elif opc == 2:
			texto = input("Ingrese un texto que finalize con un punto: ")
			cantLetras = cantPalabras = 0
			for caracter in texto:
				if caracter == " " or caracter == ".":
					if cantLetras > 4:
						cantPalabras += 1
					cantLetras = 0
				else:
					cantLetras += 1
			print(f"Palabras con mas de 4 letras: {cantPalabras}")
		elif opc == 3:
			peorNota = 100
			for i in range(3):
				print(f"Alumno {i + 1}")
				nombre = input("Ingrese nombre del alumno: ")
				nota = int(input("Ingrese nota del alumno: "))
				if nota < peorNota:
					peorNota = nota
					peorAlumno = nombre
				else:
					pass
			print(f"El alumno con la peor nota es {peorAlumno}")
		else:
			pass
	print("Gracias por usar el programa!")
