def precioArticulo(a):
	conDescuento = a - a * 0.10
	conRecargo = a + a * 0.05
	return f"precio al contado {conDescuento}, precio tarjeta {conRecargo}"

