def reparacionPc():
	equipos = []
	for i in range(3):
		pcId = input("Ingrese id de la pc: ")
		tiempo = int(input("Ingrese tiempo de reparacion (en minutos): "))
		causa = int(input("Ingrese causa de mantenimiento (1-hardware, 2-software): "))
		equipo = [pcId, tiempo, causa]
		equipos.append(equipo)
	
	tiempoTotal = mayorTiempo = tiempoPromedio = 0
	
	tiempoTotal = equipos[0][1] + equipos[1][1] + equipos[2][1]
	
	print(f"El tiempo total de reparacion de todos los equipos es: {tiempoTotal} minutos")
	
	mayorTiempo = max(equipos[0][1], equipos[1][1], equipos[2][1])
	contIndex = 0
	for pc in equipos:
		if pc[1] == mayorTiempo:
			indexMay = contIndex
		contIndex += 1
	print(f"La pc con mayor tiempo de reparacion es: {equipos[indexMay][0]}")
	
	tiempoPromedio = (equipos[0][1] + equipos[1][1] + equipos[2][1]) / 3
	print(f"El tiempo promedio de reparacion es: {tiempoPromedio} minutos")
	
	if equipos[0][2] == 1 and equipos[1][2] == 1  and equipos[2][2] == 1:
		print("Todas las Pcs tuvieron problemas de hardware") 
		
	
reparacionPc()
