def secuenciaNumerica():
	n = -1
	listNums = []
	multiSeis = divisorAnt = secuenImp = imparesSeguidos = 0
	numAnt = None
	while n != 0:
		n = int(input("Ingrese un numero (0 termina): "))
		if n != 0:
			listNums.append(n)
	
	for numero in listNums:
		if numero % 6 == 0:
			multiSeis += 1
		if numAnt != None:
			if numero % numAnt == 0:
				divisorAnt += 1
		if numero % 2 != 0:
			imparesSeguidos += 1
			if imparesSeguidos >= 3:
				secuenImp += 1
		if numero % 2 == 0:
			imparesSeguidos = 0
		
		numAnt = numero
	
	print(f"Cantidad de numeros multiplos de 6: {multiSeis}")
	print(f"Cantidad de numeros divisibles por el anterior: {divisorAnt}")
	print(f"Cantidad de veces que aparecen 3 o mas veces seguidas numeros impares: {secuenImp}")
