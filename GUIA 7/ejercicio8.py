def guarderiaNautica():
	n = int(input("Ingrese cantidad de barcos a cargar: "))
	listaBarcos = []
	for i in range(n):
		print(f"Barco {i + 1}")
		nombre = input("Ingrese nombre: ")
		tipo = int(input("Ingrese tipo de barco (1-velero, 2-lancha): "))
		monto = int(input("Monto por mes de guarderia: "))
		barco = [nombre, tipo, monto]
		listaBarcos.append(barco)
		print("datos cargados!")
	
	montoVeleroAn = montoLanchaAn = promCuota = 0
	montoVeleroMen = montoLanchaMen = 0
	mayMonto = 0
	
	for barco in listaBarcos:
		if barco[1] == 1:
			montoVeleroAn += barco[2] * 12
			montoVeleroMen += barco[2]
			if barco[2] > mayMonto:
				mayMonto = barco[2]
				mayNombre = barco[0]
		elif barco[1] == 2:
			montoLanchaAn += barco[2] * 12
			montoLanchaMen += barco[2]
		promCuota += barco[2]
	
	promCuota /= n
	
	totalMensual = montoVeleroMen + montoLanchaMen
	
	lanchaPorcent = montoLanchaMen * 100 / totalMensual
	veleroPorcent = montoVeleroMen * 100 / totalMensual
	
	print(f"El total anual pagado por los veleros es ${montoVeleroAn}")
	print(f"El total anual pagado por las lanchas es ${montoLanchaAn}")
	print(f"El velero con mayor cuota mensual es {mayNombre} con una cuota de ${mayMonto}")
	print(f"Valor promedio de cuota contando todos los barcos ${promCuota}")
	print(f"Porcentaje de lo recaudado mensualmente por veleros {round(veleroPorcent, 2)}%")
	print(f"Porcentaje de lo recaudado mensualmente por lanchas {round(lanchaPorcent, 2)}%")
	
guarderiaNautica()
