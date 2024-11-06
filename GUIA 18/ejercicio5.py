import random

def validar(msg):
	n = int(input(msg))
	while n <= 0:
		print("Error. El valor debe ser mayor a cero")
		n = int(input(msg))
	return n

def generar_resultados(n):
	calzados = []
	colores = []
	edades = []
	materiales = []
	opciones = ["blanco", "negro", "azul"]
	preferencia = ["cuero", "tela"]
	for _ in range(n):
		randNum = random.randint(25, 45)
		calzados.append(randNum)
		color = random.choice(opciones)
		colores.append(color)
		edad = random.randint(10, 25)
		edades.append(edad)
		material = random.choice(preferencia)
		materiales.append(material)
	return calzados, colores, edades, materiales
		
def calzado_promedio(calzados):
	total = 0
	for calzado in calzados:
		total += calzado
	prom = total // len(calzados)
	print(f"El calzado promedio es de {prom}")

def color_entre_10_18(colores, edades):
	contador = [0] * 3
	for i in range(len(colores)):
		if 10 <= edades[i] <= 18 and colores[i] == "blanco":
			contador[0] += 1
		elif 10 <= edades[i] <= 18 and colores[i] == "negro":
			contador[1] += 1
		elif 10 <= edades[i] <= 18 and colores[i] == "azul":
			contador[2] += 1
	if contador[1] < contador[0] > contador[2]:
		print("El color blanco es el color que mas les gusta a los jovenes entre los 10 y 18 años")
	elif contador[0] < contador[1] > contador[2]:
		print("El color negro es el color que mas les gusta a los jovenes entre los 10 y 18 años")
	else:
		print("El color azul es el color que mas les gusta a los jovenes entre los 10 y 18 años")
		
def material_entre_19_25(materiales, edades):
	contador = [0] * 2
	for i in range(len(edades)):
		if 19 <= edades[i] <= 25 and materiales == "cuero":
			contador[0] += 1
		elif 19 <= edades[i] <= 25 and materiales == "tela":
			contador[1] += 1
	if contador[0] > contador[1]:
		print("Los jovenes de entre 19 y 25 años, prefieren cuero")
	else:
		print("Los jovenes de entre 19 y 25 años, prefieren tela")
		
def demanda_calzados_grandes(calzados):
	contador = [0] * 6
	for calzado in calzados:
		if calzado >= 35 and calzado <= 40:
			index = calzado - 35
			contador[index] += 1
	mayor = [0, 0]
	menor = [None, 0]
	for i in range(len(contador)):
		if contador[i] > mayor[0]:
			mayor[0] = contador[i]
			mayor[1] = i + 35
		if menor[0] == None or contador[i] < menor[0]:
			menor[0] = contador[i]
			menor[1] = i + 35
	print(f"El numero con mayor demanda es {mayor[1]}")
	print(f"El numero con menor demanda es {menor[1]}")
			
			
		
def principal():
	n = validar("Ingrese cantida de encuestas realizadas: ")
	calzados, colores, edades, materiales = generar_resultados(n)
	calzado_promedio(calzados)
	color_entre_10_18(colores, edades)
	material_entre_19_25(materiales, edades)
	demanda_calzados_grandes(calzados)

if __name__ == "__main__":
	principal()
