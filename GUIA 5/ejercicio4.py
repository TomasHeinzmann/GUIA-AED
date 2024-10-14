def temperaturas():
	listaTemp = []
	for i in range(4):
		temperatura = int(input(f"Ingrese temperatura {i}: "))
		listaTemp.append(temperatura)
	
	promTemp = (listaTemp[0] + listaTemp[1] + listaTemp[2] + listaTemp[3]) // 4
	maxTemp = max(listaTemp[0], listaTemp[1], listaTemp[2], listaTemp[3])
	minTemp = min(listaTemp[0], listaTemp[1], listaTemp[2], listaTemp[3])
	
	if listaTemp[0] > promTemp or listaTemp[1] > promTemp or listaTemp[2] > promTemp or listaTemp[3] > promTemp:
		print("Alguna de las temperaturas supero el promedio")
	
	print(f"Temperatura maxima: {maxTemp}")
	print(f"Temperatura minima: {minTemp}")
	print(f"Temperatura promedio: {promTemp}")
	
	
temperaturas()
