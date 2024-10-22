def secuenciaNumerica():
	n = -1
	listNums = []
	cantCinco = cantPrimero = cantMayores = 0
	antNum = None
	while n != 0:
		n = int(input("Ingrese numero a cargar (0 finaliza): "))
		if n != 0:
			listNums.append(n)
	
	for numero in listNums:
		if numero % 5 == 0:
			cantCinco += 1
		if numero == listNums[0]:
			cantPrimero += 1
		if antNum != None and numero > antNum:
			cantMayores += 1
		antNum = numero

	print(f"Cantidad de numeros que terminan en 5: {cantCinco}")
	print(f"Cantidad de veces que aparece el primer numero: {cantPrimero}")
	print(f"Cantidad de numeros mayores al numero anterior: {cantMayores}")
