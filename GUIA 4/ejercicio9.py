def edadConcurso ():
	edad1 = int(input("Ingrese edad del participante 1: "))
	edad2 = int(input("Ingrese edad del participante 2: "))
	edad3 = int(input("Ingrese edad del participante 3: "))
	minEdad = int(input("Ingrese edad minima para participar: "))
	
	if edad1 >= minEdad and edad2 >= minEdad and edad3>= minEdad:
		print("Todos los participantes cumplen con el minimo de edad")
	else:
		print("Alguno de los participantes no cumple el minimo de edad")
