def terreno ():
	frente = int(input("Ingrese tamaño del frente: "))
	fondo = int(input("Ingrese tamaño del fondo: "))
	superficie = frente * fondo
	
	if frente == fondo:
		print("El terreno es cuadrado")
		print(f"Su superficie es de: {superficie}")
	else:
		print("El terreno es rectangular")
		print(f"Su superficie es de: {superficie}")
