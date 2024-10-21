
def numEnteros():
	listNums = []
	num = -1
	while num != 0:
		num = int(input("Ingrese numero entero (o presione 0 para terminar): "))
		if num != 0:
			listNums.append(num)
	
	promPos = cantPos = 0
	
	for numero in listNums:
		if numero > 0:
			promPos += numero
			cantPos += 1
	promPos /= cantPos
	
	mayNeg = None
	for numero in listNums:
		if numero < 0:
			if mayNeg == None or numero > mayNeg:
				mayNeg = numero
	
	minNum = min(listNums)
	listNums.remove(minNum)
	segMin = min(listNums)
	
	print(f"El segundo numero mas pequeño es: {segMin}")
	print(f"El promedio de numeros positivos es: {promPos}")
	print(f"El mayor de los numeros negativos es: {mayNeg}")

numEnteros()

