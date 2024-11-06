import random

def validar(msg):
	n = int(input(msg))
	while n <= 0:
		print("Error. El valor ingresado debe ser mayor a cero")
		n = int(input(msg))
	return n

def generar_viajes(n):
	estaciones = []
	idas = []
	vueltas = []
	opciones = ["Maipú", "Borges", "Libertador", "Anchorena", "Barrancas", "San Isidro R", "Punta Chica", "Marina Nueva", "San Fernando R", "Canal", "Delta"]
	for _ in range(n):
		estacion = random.choice(opciones)
		ida = random.randint(0, 250)
		vuelta = random.randint(0, 250)
		estaciones.append(estacion)
		idas.append(ida)
		vueltas.append(vuelta)
	return estaciones, idas, vueltas

def menu():
	print("------------------------------------------MENU DE OPCIONES------------------------------------------")
	print("1) Mostrar datos cargados")
	print("2) Total de pasajeros de los viajes de ida y vuelta")
	print("3) Estacion en la que se subieron mas pasajeros en la ida")
	print("4) Estaciones en las que no se subieron pasajeros en la vuelta")
	print("5) Mostrar cantidad de estaciones en las que los pasajeros de ida son mayores que los de vuelta")
	print("0) ~ Salir ~")
	print("----------------------------------------------------------------------------------------------------")
	opc = int(input("Ingrese una opcion: "))
	while opc > 5 or opc < 0:
		print("Error. La opcion ingresada no corresponde las opciones disponibles")
		opc = int(input("Ingrese una opcion: "))
	return opc

def mostrar_datos(estaciones, idas, vueltas):
	for i in range(len(estaciones)):
		print(f"En la estacion {estaciones[i]}")
		print(f"En la ida se subieron {idas[i]} pasajeros")
		print(f"En la vuelta se subieron {vueltas[i]} pasajeros")
		print("-------------------------------------------------")

def total_ida_vuelta(idas, vueltas):
	total_idas = 0
	total_vueltas = 0
	for i in range(len(idas)):
		total_idas += idas[i]
		total_vueltas += vueltas[i]
	print(f"El total de pasajeros en la ida es de {total_idas}")
	print(f"El total de pasajeros en la vuelta es de {total_vueltas}")

def mayor_pasajeros_ida(estaciones, idas):
	estacion_mas_pasajeros = [0, 0]
	for i in range(len(idas)):
		if idas[i] > estacion_mas_pasajeros[0]:
			estacion_mas_pasajeros[0] = idas[i]
			estacion_mas_pasajeros[1] = estaciones[i]
	print(f"Estacion con mas pasajeros en al ida {estacion_mas_pasajeros[1]}")
	print(f"Cantidad de pasajeros en la ida {estacion_mas_pasajeros[0]}")

def estaciones_vuelta_sin_pasajeros(vueltas):
	vagon_vacio = 0
	for i in range(len(vueltas)):
		if vueltas[i] == 0:
			vagon_vacio += 1
	if vagon_vacio > 0:
		porcent = vagon_vacio * 100 // len(vueltas)
		print(f"El porcentaje de viajes de vuelta sin pasajeros es de {porcent}%")
	else:
		print("Todos los viajes de vuelta tuvieron al menos 1 pasajero")

def estaciones_con_mas_idas_que_vueltas(estaciones, idas, vueltas):
	encontrado = False
	for i in range(len(estaciones)):
		if idas[i] > vueltas[i]:
			print(f"En la estacion {estaciones[i]} hubo mas idas que vueltas")
			encontrado = True
	if not encontrado:
		print("No hubo estaciones con mas idas que vueltas")
	else:
		pass
			

def principal():
	n = validar("Ingrese cantidad de viajes: ")
	estaciones, idas, vueltas = generar_viajes(n)
	opc = -1
	while opc != 0:
		opc = menu()
		if opc == 1:
			mostrar_datos(estaciones, idas, vueltas)
		elif opc == 2:
			total_ida_vuelta(idas, vueltas)
		elif opc == 3:
			mayor_pasajeros_ida(estaciones, idas)
		elif opc == 4:
			estaciones_vuelta_sin_pasajeros(vueltas)
		elif opc == 5:
			estaciones_con_mas_idas_que_vueltas(estaciones, idas, vueltas)
	print("Gracias por usar el programa!")
		

if __name__ == "__main__":
	principal()
