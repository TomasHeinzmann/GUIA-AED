def puntosPlanos():
	n = int(input("Ingrese cantidad de puntos a crear: "))
	puntos = []
	cantprim = cantterc = 0
	for i in range(n):
		print(f"Punto numero {i + 1}")
		x = int(input("Ingrese x: "))
		y = int(input("Ingrese y: "))
		punto = [x, y]
		puntos.append(punto)
	
	mayDistancia = 0
	
	for punto in puntos:
		if punto[0] > 0 and punto[1] > 0:
			print(f"El punto {punto} esta en el primer cuadrante!")
			cantprim += 1
		elif  punto[0] < 0 and punto[1] > 0:
			print(f"El punto {punto} esta en el segundo cuadrante!")
		elif  punto[0] < 0 and punto[1] < 0:
			print(f"El punto {punto} esta en el tercer cuadrante!")
			cantterc += 1
		elif  punto[0] > 0 and punto[1] < 0:
			print(f"El punto {punto} esta en el cuarto cuadrante!")
		elif  punto[0] == 0 and punto[1] != 0:
			print(f"El punto {punto} esta en el eje de ordenadas")
		elif  punto[0] != 0 and punto[1] == 0:
			print(f"El punto {punto} esta en el eje de abscisas")
		else:
			print(f"El punto {punto} esta en el origen")

	for punto in puntos:
		distancia = (punto[0] ** 2 + punto[1] ** 2) ** 0.5
		if distancia > mayDistancia:
			mayDistancia = distancia
			mayPunto = punto
		
	print(f"La cantidad de puntos en el primer cuadrante es: {cantprim}")
	print(f"La cantidad de puntos en el tercer cuadrante es: {cantterc}")
	print(f"El punto mas lejano del origen de coordenadas es: {mayPunto}")
	
puntosPlanos()
		
