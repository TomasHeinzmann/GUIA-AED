
def secuenciaNumerica():
	num = -1
	n1 = int(input("Ingrese valor de n1: "))
	n2 = int(input("Ingrese valor de n2: "))
	mayoresN1 = menoresN2 = 0
	cantNums = 0
	antNum = None
	flagImparPar = False
	cantCinco = 0
	while num != 0:
		num = int(input("Ingrese un numero de la secuencia: "))
		if num != 0:
			cantNums += 1
			if num > n1:
				mayoresN1 += 1
			if num < n2:
				menoresN2 += 1
			if antNum != None and antNum % 2 != 0 and num % 2 == 0:
				flagImparPar = True
			if antNum == 5 and num == 5:
				cantCinco += 1
			antNum = num
		else:
			pass
	porcentMayores = mayoresN1 * 100 // cantNums 
	porcentMenores = menoresN2 * 100 // cantNums
	
	print(f"Mayores que n1: {mayoresN1}")
	print(f"Menores que n2: {menoresN2}")
	print(f"Porcentaje de mayores que n1: {porcentMayores}%")
	print(f"Porcentaje de menores que n2: {porcentMenores}%")
	print(f"Cantidad de veces que aparecieron dos cincos seguidos: {cantCinco}")
	if flagImparPar:
		print("Aparecio un numero impar seguido de uno par")
	
secuenciaNumerica()
