def contadorVotos(a, b):
	total = a + b
	porcentajeA = round(a * 100 / total)
	porcentajeB = round(b * 100 / total)
	return f"Total votos {total}, a favor {porcentajeA}% en contra {porcentajeB}%"

