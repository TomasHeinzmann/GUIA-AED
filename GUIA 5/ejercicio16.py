def pagoProveedor ():
	cat = input("Ingrese categoria: ")
	imp = int(input("Ingrese importe a pagar: "))
	
	if cat == "A" and imp > 1000:
		print("Descuento del 5%")
		imp -= imp * 0.05
		print(f"El monto a pagar es: ${imp}")
	elif cat == "B" and 2500 >= imp >= 1500:
		print("Descuento del 2%")
		imp -= imp * 0.02
		print(f"El monto a pagar es: ${imp}")
	else:
		print("No se aplican descuentos")
		print(f"El monto a pagar es: ${imp}")
		
