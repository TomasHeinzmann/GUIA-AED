def comercioArticulos():
	articulos = []
	for i in range(3):
		nombre = input("Ingrese el nombre del articulo: ")
		precio = int(input("Ingrese precio del articulo: "))
		cantidad = int(input("Ingrese cantidad vendida: "))
		monto = precio * cantidad
		articulo = [nombre, monto]
		articulos.append(articulo)
	
	mayAporte = max(articulos[0][1], articulos[1][1], articulos[2][1])
	
	if mayAporte == articulos[0][1]:
		mayIndex = 0
	elif mayAporte == articulos[1][1]:
		mayIndex = 1
	elif mayAporte == articulos[2][1]:
		mayIndex = 2
	
	totalAporte = articulos[0][1] + articulos[1][1] + articulos[2][1]
	
	porcentMay = mayAporte * 100 / totalAporte
	
	print(f"El articulo con mayor porcentaje de aporte es: {articulos[mayIndex][0]}")
	print(f"Con un porcentaje del {round(porcentMay, 2)}% del aporte total")

