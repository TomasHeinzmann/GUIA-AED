def tresCalculoVariante():
	listVal = []
	for i in range(3):
		print(f" Valor {i+1}")
		val = float(input("Ingrese valor: "))
		listVal.append(val)
	
	mayVal = max(listVal[0], listVal[1], listVal[2])
	minVal = min(listVal[0], listVal[1], listVal[2])
	
	if listVal[0] != mayVal and listVal[0] != minVal:
		midVal = listVal[0]
	elif listVal[1] != mayVal and listVal[1] != minVal:
		midVal = listVal[1]
	else:
		midVal = listVal[2]
		
	sumVal = midVal + minVal
	
	contImp = 0
	
	for val in listVal:
		if val % 2 != 0:
			contImp += 1
	
	if listVal[0] % 5 == 0 or listVal[1] % 5 == 0 or listVal[2] % 5 == 0:
		print("Alguno de los valores es multiplo de 5")
	if mayVal > sumVal:
		print("El mayor de ellos supera la suma de los demas")
	
	print(f"Hay {contImp} numeros impares")
