

def cuantificar_notas():
	archivo = open("datos.txt", "r")
	lineas = archivo.readlines()
	libres = 0; regulares = 0; aprobados = 0
	alumnos_analizados = []
	for linea in lineas:
		notas = [linea[30], linea[33],  linea[36], linea[39]]
		parciales_aprobados = 0; practicos_aprobados = False
		acumulador_notas_parciales = 0; practicos_promocionados = False
		acumulador_notas_totales = 0
		aprobado = False
		for i in range(len(notas)):
			nota = int(notas[i])
			if nota >= 4 and i < 3:
				parciales_aprobados += 1
				if nota >= 7:
					acumulador_notas_parciales += nota
			elif nota >= 4 and i == 3:
				practicos_aprobados = True
				if nota >= 8:
					practicos_promocionados = True
			if aprobado:
				acumulador_notas_totales += nota
		promedio_parciales =  acumulador_notas_parciales / 3
		if promedio_parciales >= 8 and practicos_promocionados:
			aprobados += 1 
		elif parciales_aprobados >= 2 and practicos_aprobados:
			regulares += 1
		else:
			libres += 1
		
		if aprobado and practicos_promocionados and promedio_parciales >= 8:
			alumno = linea[6:29]
			alumno = alumno.rstrip()
			prom = acumulador_notas_totales / 4
			print(f"El alumno {alumno} esta aprobado con un promedio de {round(prom)}")
		
	total = aprobados + regulares + libres
	porcent_aprobados = aprobados * 100 / total
	porcent_regulares = regulares * 100 / total
	porcent_libres = libres * 100 / total		
	print(f"Hay {aprobados} alumnos aprobados, son un {round(porcent_aprobados, 2)}% de los alumnos")
	print(f"Hay {regulares} alumnos regulares, son un {round(porcent_regulares, 2)}% de los alumnos")
	print(f"Hay {libres} alumnos libres, son un {round(porcent_libres, 2)}% de los alumnos")
	archivo.close()

if __name__ == "__main__":
	cuantificar_notas()
