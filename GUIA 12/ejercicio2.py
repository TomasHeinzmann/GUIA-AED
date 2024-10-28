def secuencia_numerica():
	num = -1
	num_list = []
	while num != 0:
		num = float(input("Ingrese numero de la secuencia: "))
		if num != 0:
			num_list.append(num)
	total = len(num_list)
	pares = 0; num_cuatro_cinco = 0; menor = None; mayores_siete = False
	for numero in num_list:
		if numero % 2:
			pares += 1
		if numero % 10 == 4 or numero % 10 == 5:
			num_cuatro_cinco += 1
		if menor == None:
			menor = numero
		elif numero < menor and numero % 3 == 0:
			menor = numero
		if numero > 7:
			mayores_siete = True
	porcent = pares * 100 // total
	
	print(f"Porcentaje de numeros pares: {porcent}%")
	print(f"Numeros con un 4 o 5 en su ultimo digito: {num_cuatro_cinco}")
	print(f"Menor numero multiplo de 3: {menor}")
	if mayores_siete:
		print("Hay numeros mayores a 7")
	else:
		print("Solo hay numeros menores o iguales a 7")
