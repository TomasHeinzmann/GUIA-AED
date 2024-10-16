def lluvias():
	listLluvias = []
	for i in range(3):
		print(f"Lluvia mes {i + 1}")
		lluvia = float(input("Ingrese milimetros: "))
		listLluvias.append(lluvia)
	
	prom = (listLluvias[0] + listLluvias[1] + listLluvias[2]) / 3
	
	print(f"Promedio de milimetros: {prom}")
	
	cantMes = 0
	mesMen = min(listLluvias[0], listLluvias[1], listLluvias[2])
	contIndex = 0
	for lluvia in listLluvias:
		if lluvia >= prom:
			cantMes += 1
		if lluvia == mesMen:
			contIndex = listLluvias.index(lluvia)
			
	print(f"Cantidad de meses con mas o igual lluvia que el promedio: {cantMes}")
	
	print(f"Mes con menos lluvia en el cuatrimestre: {contIndex + 1}")
		
	if listLluvias[contIndex] == 0:
		print(f"En el mes {contIndex + 1} llovio ni un milimetro!")
