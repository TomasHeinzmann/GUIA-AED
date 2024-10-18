def mayorParPar():
	num = -1
	listNum = []
	may = None
	while num != 0:
		num = int(input("Ingrese un numero: "))
		if num != 0: 
			listNum.append(num)
			print("Numero guardado!")
	
	for index, num in enumerate(listNum):
		if index % 2 == 0 and num % 2 == 0:
			if may == None or num > may:
				may = num
		
	if may:
		print(f"El mayor numero par, de orden par, ingresado es: {may}")
	else:
		print(f"No se encontro numero que cumpla con la condicion")
