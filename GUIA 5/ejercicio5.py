def opciones():
	print("----------- MENU DE TRIGONOMETRIA -----------")
	print("1) Calcular superficie de un triangulo")
	print("2) Calcular perimetro de un triangulo")
	print("3) Informar la longitud de el lado menor")
	print("0) Salir")
	print("---------------------------------------------")
	opc = int(input("Ingrese una opcion: "))
	return opc

def ingresarLados ():
	triangulo = []
	for i in range(3):
		lado = int(input(f"Ingresar lado {i + 1} : "))
		triangulo.append(lado)
	return triangulo

def menuBasico():
	opc = -1 
	while opc != 0:
		if opc == 1:
			triangulo = ingresarLados()
			s = (triangulo[0] + triangulo[1] + triangulo[2]) / 2
			superficie = (s*(s - triangulo[0])*(s - triangulo[1])*(s - triangulo[2])) * 0.5
			print(f"La superficie del triangulo es: {superficie}")
		elif opc == 2:
			triangulo = ingresarLados()
			perimetro = triangulo[0] + triangulo[1] + triangulo[2]
			print(f"El perimetro del triangulo ingresado es: {perimetro}")
		elif opc == 3:
			triangulo = ingresarLados()
			ladoMen = min(triangulo[0], triangulo[1], triangulo[2])
			print(f"El lado menor es: {ladoMen}")
		else:
			print("Error, la opcion ingresada no esta entre las opciones disponibles")
		opc = opciones()
	print("Gracias por usar el programa! ")


			
			
		
