def infoCursos():
	grados = []
	for i in range(3):
		print(f"Curso {i + 1}")
		gradoId = input("Ingrese id del curso: ")
		niños = int(input("Ingrese cantidad de niños: "))
		niñas = int(input("Ingrese cantidad de niñas: "))
		maximo = int(input("Ingrese cupo maximo: "))
		grado = [gradoId, niños, niñas, maximo]
		grados.append(grado)
	
	alumnosGrado1 = grados[0][1] + grados[0][2]
	alumnosGrado2 = grados[1][1] + grados[1][2]
	alumnosGrado3 = grados[2][1] + grados[2][2]
	
	menosAlumnos = min(alumnosGrado1, alumnosGrado2, alumnosGrado3)
	contIndex = 0
	for grado in grados:
		gradoAlumnos = grado[1] + grado[2]
		if gradoAlumnos == menosAlumnos:
			minIndex = contIndex
		contIndex += 1
	print(f"El grado con menos alumnos es: {grados[minIndex][0]}")

	porcentNiñas1 = grados[0][2] * 100 / alumnosGrado1
	porcentNiñas2 = grados[1][2] * 100 / alumnosGrado2
	porcentNiñas3 = grados[2][2] * 100 / alumnosGrado3
	
	print(f"Porcentaje de niñas en {grados[0][0]} es de {round(porcentNiñas1, 2)}%")
	print(f"Porcentaje de niñas en {grados[1][0]} es de {round(porcentNiñas2, 2)}%")
	print(f"Porcentaje de niñas en {grados[2][0]} es de {round(porcentNiñas3, 2)}%")
	
	porcentNiños1 = grados[0][1] * 100 / alumnosGrado1
	porcentNiños2 = grados[1][1] * 100 / alumnosGrado2
	porcentNiños3 = grados[2][1] * 100 / alumnosGrado3
	
	print(f"Porcentaje de niños en {grados[0][0]} es de {round(porcentNiños1, 2)}%")
	print(f"Porcentaje de niños en {grados[1][0]} es de {round(porcentNiños2, 2)}%")
	print(f"Porcentaje de niños en {grados[2][0]} es de {round(porcentNiños3, 2)}%")
	
	promAlumnos = (alumnosGrado1 + alumnosGrado2 + alumnosGrado3) / 3
	print(f"Promedio de alumnos: {round(promAlumnos)}")
	
	if alumnosGrado1 > grados[0][3] or alumnosGrado2 > grados[0][3] or alumnosGrado3 > grados[0][3]:
		print("Se necesita la apertura de una nueva division! ")

infoCursos()
