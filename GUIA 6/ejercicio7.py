# ~ Se pide desarrollar un programa que permita leer una serie de números. La finalización de carga de datos se presenta cuando el usuario ingrese un número negativo.
# ~ Los requerimientos funcionales del programa son:
# ~ a) La sumatoria de solo los números que estén comprendidos entre 50 y 100.
# ~ b) Cantidad de valores pares ingresados.
# ~ c) Cantidad de valores impares ingresados.
# ~ d) Informar si en la carga de números se ingreso al menos un número 0.
# ~ e) Informar si la serie contiene solo números pares e impares alternados

def esPar(numero):
	if numero % 2 == 0:
		return True
	else:
		return False

def paresImpares():
	sumNums = parNums = impNums = 0
	num = 0
	numCero = False
	altParImpar = True
	listNums = []
	while num >= 0:
		num = int(input("Ingrese un numero: "))
		if num >= 0:
			if 100 >= num >= 50:
				sumNums += num
			if num % 2 == 0:
				parNums += 1
			else:
				impNums += 1
			if num == 0:
				numCero = True
			listNums.append(num)
	antNum = None
	for numero in listNums:
		print(antNum)
		if antNum != None:
			if (esPar(antNum) and not esPar(numero)) or (not esPar(antNum) and esPar(numero)):
				antNum = numero
				continue
			else:
				altParImpar = False
		antNum = numero
		
			
	print(f"Sumatoria de todos los numeros comprendidos entre 50 y 100: {sumNums}")
	print(f"Cantidad de valores pares ingresados: {parNums}")
	print(f"Cantidad de valores impares ingresados: {impNums}")
	if numCero:
		print("Se ingreso al menos un cero")
	else:
		print("No se ingreso ningun cero")
	if altParImpar:
		print("La serie contiene numeros pares e impares alternados")
	else:
		print("La serie no contiene numeros pares e impares alternados")

paresImpares()
