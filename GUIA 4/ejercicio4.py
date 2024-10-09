def medirTemperaturas():
	temp1 = int(input("Ingrese temperatura 1: "))
	temp2 = int(input("Ingrese temperatura 2: "))
	temp3 = int(input("Ingrese temperatura 3: "))
	
	prom = round((temp1 + temp2 + temp3) / 3, 2)
	
	print(f"El promedio fue de: {prom}")
	
	if temp1 > prom or temp2 > prom or temp3 > prom:
		print("Hay temperaturas mayores que el promedio")

medirTemperaturas()
