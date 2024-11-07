from temperaturas import Temperatura

def menu():
	print("*******************MENU DE OPCIONES*******************")
	print("1) Cargar analisis termicos")
	print("2) Informar temperatura maxima promedio en el primer semestre")
	print("3) Region y mes con la menor temperatura del año")
	print("0) ~ Salir ~")
	print("------------------------------------------------------")
	opc = int(input("Ingrese una opcion: "))
	while opc > 3 or opc < 0:
		print("Error. la opcion ingresada no esta entre los parametros")
		opc = int(input("Ingrese una opcion: "))
	return opc

def generar_temperaturas(n):
	temperaturas = [] * n
	for i in range(n):
		temp = Temperatura()
		temperaturas.append(temp)
	return temperaturas

def maxima_promedio_semestre(datos_temperaturas):
	acum, cont = 0, 0
	for temperatura in datos_temperaturas:
		if 1 <= temperatura.mes <= 6:
			acum += temperatura.maxima
			cont += 1
	prom = acum // cont
	return prom
	
def menor_minima_anual(datos_temperaturas):
	menor = None
	mesMenor, regionMenor = None, None
	for temperatura in datos_temperaturas:
		if menor == None or temperatura.minima < menor:
			menor = temperatura.minima
			mesMenor = temperatura.mes
			regionMenor = temperatura.region
	return mesMenor, regionMenor

def principal():
	opc = -1
	flag_primer_punto = False
	while opc != 0:
		opc = menu()
		if opc == 1:
			n = int(input("Ingrese cantidad de analisis a cargar: "))
			while n <= 0:
				print("Error. La cantidad de analisis no puede ser menor o igual a cero")
				n = int(input("Ingrese cantidad de analisis a cargar: "))
			datos_temperaturas = generar_temperaturas(n)
			flag_primer_punto = True
		elif flag_primer_punto:
			if opc == 2:
				prom = maxima_promedio_semestre(datos_temperaturas)
				print(f"La temperatura maxima promedio del primer semestre fue de {prom}")
			elif opc == 3:
				mesMenor, regionMenor = menor_minima_anual(datos_temperaturas)
				print(f"El mes con menor minima del año fue el {mesMenor}")
				print(f"En la region de {regionMenor}")
		elif not flag_primer_punto:
			print("Pase primero por el punto 1 para generar la informacion a analizar")
		
	print("Gracias por usar el programa!")


if __name__ == "__main__":
	principal()
