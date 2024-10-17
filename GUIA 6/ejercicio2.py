def ventasSucursal():
	cantVentas = totalVentas = ventasMen = ventasMay = 0
	ventasMin = False
	ventas = 1
	while ventas > 0:
		ventas = int(input("Ingrese cantidad de ventas realizadas: "))
		cantVentas += 1
		totalVentas += ventas
		if 300 >= ventas >= 100:
			ventasMen += 1
		elif 600 >= ventas >= 400:
			ventasMay += 1
		elif ventas < 50:
			ventasMin = True
	print(f"Cantidad de ventas: {cantVentas}")
	print(f"Cantidad de unidades vendidas: {totalVentas}")
	print(f"Ventas entre 300 y 100 unidades: {ventasMin}")
	print(f"Ventas entre 600 y 400 unidades: {ventasMay}")
	
	if ventasMin:
		print("Hubo al menos una venta de menos de 50 unidades")
