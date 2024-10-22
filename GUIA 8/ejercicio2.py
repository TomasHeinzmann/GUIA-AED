# ~ Ingresar una secuencia de números, de a uno por vez, la carga finaliza cuando el usuario ingresa el cero. Determinar
# ~ a) Porcentaje que representan los números divisibles por 3 sobre el total de números ingresados en la secuencia
# ~ b) Determinar la cantidad de números que son el cuadrado del número anterior
# ~ c) Determinar la posición del mayor elemento impar de la secuencia

def secuenciaNumerica():
	num = -1
	listNum = []
	numTres = antNum = 0
	numCuad = mayImp = 0
	while num != 0:
		num = int(input("Ingrese numero a cargar (0 finaliza): "))
		if num != 0: 
			listNum.append(num)
	
	for numero in listNum:
		if numero % 3 == 0:
			numTres += 1
		if num == antNum:
			print(num == antNum)
			numCuad += 1
		if num % 2 != 0 and num > mayImp:
			mayImp = num
		antNum = num ** 2
	totalNums = len(listNum)
	porcentTres = numTres * 100 / totalNums
	mayIndex = listNum.index(mayImp)
	
	print(f"Porcentaje de numeros divisibles por 3: {round(porcentTres, 2)}")
	print(f"Cantidad de numeros que son el cuadrado del anterior: {numCuad}")
	print(f"Posicion del mayor elemento impar de la secuencia: {mayIndex}")
