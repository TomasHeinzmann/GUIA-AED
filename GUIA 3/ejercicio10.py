def triatlonCalculo(msg):
	minutos = int(input(f"Ingrese cantidad de minutos en {msg}: "))
	segundos = int(input(f"Ingrese cantidad de segundos {msg}: "))
	segundos += minutos * 60
	horastotal = segundos // 60 // 60
	minutostotal = segundos // 60 % 60
	segundostotal = segundos % 60
	print(f"Resultado: {horastotal}:{minutostotal}:{segundostotal}")
	return [horastotal, minutostotal, segundostotal]

pruebanatacion = triatlonCalculo("natacion")
pruebaciclista = triatlonCalculo("ciclismo")
pruebapedestre = triatlonCalculo("pedestre")

def comparacionPruebas(natacion, ciclismo, pedestre):
	totalnatacion = natacion[0] * 3600 + natacion[1] * 60 + natacion[2]
	totalciclismo = ciclismo[0] * 3600 + ciclismo[1] * 60 + ciclismo[2]
	totalpedestre = pedestre[0] * 3600 + pedestre[1] * 60 + pedestre[2]
	tiempoMaximo = max(totalnatacion, totalciclismo, totalpedestre)
	tiempoMinimo = min(totalnatacion, totalciclismo, totalpedestre)
	tiempoPromedio = round((totalnatacion + totalciclismo + totalpedestre) / 3, 2)
	print(f"Tiempo maximo: {tiempoMaximo} segundos")
	print(f"Tiempo minimo: {tiempoMinimo} segundos")
	print(f"Promedio: {tiempoPromedio} segundos")

comparacionPruebas(pruebanatacion, pruebaciclista, pruebapedestre)
