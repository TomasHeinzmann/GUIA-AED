def censo():
	sexo = "M"
	cant = edad = sexM = sexF = femEscolar = 0
	masViejo = False
	while sexo == "M" or sexo == "F":
		print("------------------ CENSO ------------------")
		sexo = input("Ingrese sexo del habitante (M / F): ")
		if sexo == "M" or sexo == "F":
			edad = int(input("Ingrese edad del habitante: "))
			if sexo == "M":
				sexM += 1
			else:
				sexF += 1
			if sexo == "F" and  18 >= edad >= 4:
				femEscolar += 1
			if sexo == "M" and edad > 80:
				masViejo = True
	
	if sexM > sexF:
		print("Hay mayor cantindad de hombres que mujeres")
	else:
		print("Hay mayor cantindad de mujeres que hombres")

	print(f"Cantidad de mujeres entre 18 y 4 años: {femEscolar}")
	
	if masViejo:
		print("Hay al menos un varon con mas de 80 años!")
	else:
		print("No hay hombres con mas de 80 años")
