def pagoFarmacia (a):
	descuento = 0.35
	pagoDescuento = round(a * descuento, 2)
	return f"Precio actual {a}, descuento del 35%, monto total {pagoDescuento}"

