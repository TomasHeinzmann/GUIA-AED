
def secuenciaNumerica():
	num = -1
	p = int(input("Ingrese valor de p (desde): "))
	q = int(input("Ingrese valor de q (hasta): "))
	cantPQ = 0
	while p == 0 or q == 0:
		print("Error, ninguno puede ser igual a cero, ingrese otro numero")
		p = int(input("Ingrese valor de p (desde): "))
		q = int(input("Ingrese valor de q (hasta): "))
	for num in range(p, q + 1):
		cantPQ += 1
	paresContiguos = 0
	cantNums = 0 ; cantPrimeros = 0
	antNum = None
	while num != 0:
		num = int(input("Ingrese un numero: "))
		if num != 0:
			cantNums += 1
			if antNum != None and antNum % 2 == 0 and num % 2 == 0:
				paresContiguos += 1
			if cantNums == 1:
				primero = num
			elif num % primero == 0:
				cantPrimeros += 1
			antNum = num
	
	porcent = cantPQ * 100 // (cantNums + cantPQ)
	
	print(f"Cantidad de numeros entre p y q: {cantPQ}")
	print(f"Cantidad de numeros contiguos pares: {paresContiguos}")
	print(f"Multiplos del primer numero de la secuencia: {cantPrimeros}")
	print(f"Porcentaje del punto 1: {porcent}%")
	
secuenciaNumerica()
