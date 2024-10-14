def elecciones():
	partidos = []
	for vuelta in range(3):
		print(f"Partido numero {vuelta + 1}")
		presi = input("Ingrese nombre del candidato a presidente: ")
		vice = input("Ingrese nombre del candidato a vicepresidente: ")
		cant = int(input("Ingrese cantidad de votos del partido: "))
		partido = [presi, vice, cant]
		partidos.append(partido)
	
	mayor = max(partidos[0][2], partidos[1][2], partidos[2][2])
	menor = min(partidos[0][2], partidos[1][2], partidos[2][2])
	
	if partidos[0][2] != mayor and partidos[0][2] != menor:
		medio = partidos[0][2]
	elif partidos[1][2] != mayor and partidos[1][2] != menor:
		medio = partidos[1][2]
	else:
		medio = partidos[2][2]
		
	totalVotos = mayor + menor + medio
	porcentMayor = (mayor * 100) / totalVotos
	porcentMedio = (medio * 100) / totalVotos
	porcentMenor = (menor * 100) / totalVotos
	diferencia = mayor - medio
	
	contVueltas = 0
	
	for partido in partidos:
		if partido[2] == mayor:
			print(f"La formula de {partido[0]} y {partido[1]} tuvo mayor cantidad de votos, con {round(porcentMayor, 2)}%")
			indexMay = contVueltas
		if partido[2] == medio:
			indexMed = contVueltas
		contVueltas += 1

	if diferencia >= 10 and 45 > mayor >= 40:
		print("El partido con la mayoria de los votos y una diferencia de al menos 10 puntos con el siguiente partido es: ")
		print(f"{partidos[indexMay][0]} y {partidos[indexMay][1]} con {round(porcentMayor, 2)}%")
	elif mayor >= 45:
		print("El partido con mas del 45% es: ")
		print(f"{partidos[indexMay][0]} y {partidos[indexMay][1]} con {round(porcentMayor, 2)}%")
	else:
		print("Se debe hacer una segunda vuelta. Las formulas que participaran son:")
		print(f"El partido mas votado: {partidos[indexMay][0]} con {partidos[indexMay][1]}")
		print(f"El segundo mas votado: {partidos[indexMed][0]} con {partidos[indexMay][1]}")
		

		

elecciones()
