def impuestoVehiculo():
	modelo = int(input("Ingrese modelo del vehiculo (año de fabricacion): "))
	tipo = input("Ingrese tipo de vehiculo (P: Particular/T: Taxi/R: Remis): ")
	diferencia = 2024 - modelo
	
	if tipo == "P" and diferencia < 10:
		print("Por vehiculo particular")
		print("Impuesto a pagar: $200")
	elif tipo == "P" and 20 >= diferencia >= 10:
		print("Por vehiculo particular")
		print("Impuesto a pagar: $150")
	elif tipo == "P" and diferencia > 20:
		print("Por la antiguedad del vehiculo, no paga impuestos")
		
	if tipo == "T" and diferencia < 10:
		print("Por vehiculo particular y licencia de Taxi")
		print("Impuesto a pagar: $200")
		print("Mas licencia de Taxi ($150): $350")
	elif tipo == "T" and 20 >= diferencia >= 10:
		print("Por vehiculo particular y licencia de Taxi")
		print("Impuesto a pagar: $150")
		print("Mas licencia de Taxi ($150): $300")
	elif tipo == "T" and diferencia > 20:
		print("Por vehiculo particular y licencia de Taxi")
		print("Por la antiguedad del vehiculo, no paga impuestos")
		print("Mas licencia de Taxi ($150): $150")
		
	if tipo == "R":
		monto = diferencia * 100
		print("Por remis:")
		print(f"Impuesto a pagar: {monto}")

impuestoVehiculo()
