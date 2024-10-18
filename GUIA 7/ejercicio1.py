def ciclistas():
	n = int(input("Ingrese cantidad de ciclistas: "))
	rec = int(input("Ingrese tiempo record: "))
	competidores = []
	for i in range(n):
		nombre = input("Ingrese nombre del ciclista: ")
		tiempo = int(input("Ingrese tiempo de carrera: "))
		competidor = [nombre, tiempo]
		competidores.append(competidor)
	
	menTime = None
	promTime = 0
	for competidor in competidores:
		promTime += competidor[1]
		if menTime == None or competidor[1] < menTime:
			menTime = competidor[1]
			nomGanador = competidor[0]
	if menTime < rec:
		print("El ganador supero el record anterior!!")
	promTime /= n
	
	print(f"El ganador de la carrera es {nomGanador}")
	print(f"El promedio de tiempo por ciclista es {promTime} segundos")

ciclistas()
