def conversorPies(a):
	yarda = a * 3
	pulgadas = a * 12
	centimetros = pulgadas * 2.54
	metros = centimetros / 100
	return [f"yardas: {yarda}", f"pulgadas: {pulgadas}", f"centimetros: {centimetros}", f"metros: {metros}"]
	
print(conversorPies(5))
