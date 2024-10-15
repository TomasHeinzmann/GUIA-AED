def compararPorcentaje(porcentaje):
	if porcentaje >= 90:
		return "Superior"
	elif 75 <= porcentaje < 90:
		return "Medio"
	elif 50 <= porcentaje < 75:
		return "Regular"
	elif porcentaje < 50: 
		return "Fuera de nivel"

def postulantesEmpleo():
	lista = []
	for i in range(3):
		nombre = input("Ingrese nombre del postulante: ")
		cantPreg = int(input("Ingrese cantidad de preguntas realizadas: "))
		cantResp = int(input("Ingrese cantidad de respuestas correctas: "))
		postulante = [nombre, cantPreg, cantResp]
		lista.append(postulante)
	
	porcent1 = lista[0][2] * 100 / lista[0][1]
	porcent2 = lista[1][2] * 100 / lista[1][1]
	porcent3 = lista[2][2] * 100 / lista[2][1]
	
	nivel1 = compararPorcentaje(porcent1)
	nivel2 = compararPorcentaje(porcent2)
	nivel3 = compararPorcentaje(porcent3)
	
	mayorporcent = max(porcent1, porcent2, porcent3)
	
	if mayorporcent == porcent1:
		indexMay = 0
	elif mayorporcent == porcent2:
		indexMay = 1
	elif mayorporcent == porcent3:
		indexMay = 2
	
	print(f"El nivel de {lista[0][0]} es {nivel1}")

	print(f"El nivel de {lista[1][0]} es {nivel2}")
	
	print(f"El nivel de {lista[2][0]} es {nivel3}")
	
	print(f"El postulante con mayor porcentaje es {lista[indexMay][0]}")
	
	print(f"{lista[indexMay][0]} gano el puesto!")

