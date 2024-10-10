def precioProducto():
	precio = int(input("Ingrese el precio unitario: "))
	cantidad = int(input("Ingrese cantidad: "))
	efectivo = int(input("El pago es en efectivo (1-Si, 2-No): "))
	monto = precio * cantidad
	if efectivo == 2:
		print(f"El precio total seria: {monto}")
	else:
		if cantidad > 10:
			monto -= monto * 0.15
			print(f"El precio total seria: {monto}")
		else: 
			monto -= monto * 0.05
			print(f"El precio total seria: {monto}")
