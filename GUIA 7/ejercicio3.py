def aguinaldo():
	i = 0
	listSueldos = []
	while i < 6:
		print(f"Sueldo del mes {i + 1}")
		sueldo = int(input("Ingrese sueldo: "))
		listSueldos.append(sueldo)
		i += 1
	
	maySueldo = max(listSueldos[0], listSueldos[1], listSueldos[2], listSueldos[3], listSueldos[4], listSueldos[5])
	agu = maySueldo / 2
	
	minSueldo = min(listSueldos[0], listSueldos[1], listSueldos[2], listSueldos[3], listSueldos[4], listSueldos[5])
	indexMin = listSueldos.index(minSueldo)
	
	promSueldo = listSueldos[0] + listSueldos[1] + listSueldos[2] + listSueldos[3] + listSueldos[4] + listSueldos[5]
	promSueldo /= 6
	
	print(f"El aguinaldo es de ${agu}")
	print(f"El mes con menor sueldo fue el mes {indexMin + 1}")
	print(f"El sueldo promedio es de ${round(promSueldo, 2)}")
