def plantillaCandidato():
	apellido = input("Ingrese apellido del candidato: ")
	nombre = input("Ingrese nombre del candidato: ")
	votos = int(input("Ingrese cantidad de votos: "))
	iniciales = apellido[0] + "." + nombre[0]
	cruces = "x" * votos
	print(iniciales)
	print(f"({votos})")
	print(cruces)
