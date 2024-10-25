def portalTrabajo():
	opc = -1
	while opc != 0:
		opc = int(input("Le gustaria cargar un aviso? (1-si, 0-no): "))
		if opc != 0:
			cuit = input("Ingrese su cuit (con guiones): ")
			cuitValido = True
			for caracter in cuit:
				if caracter == "-" or caracter.isnumeric():
					pass
				else:	
					cuitValido = False
			salarioValido = False
			if cuitValido:
				texto = input("Ingrese descripcion de busqueda: ")
				contPalabras = 0; contCaracteres = 0 ; textoValido = False
				mayusculas = "QWERTYUIOPÑLKJHGFDSAZXCVBNM" ; maySeguidas = False
				caracterAnterior = None
				for caracter in texto:
					contCaracteres += 1
					if caracter == " " or caracter == ".":
						contPalabras += 1
					else:
						if caracterAnterior != None and caracterAnterior in mayusculas and caracter in mayusculas:
							maySeguidas = True
						caracterAnterior = caracter
				if contCaracteres <= 60 and contPalabras >= 3 and not maySeguidas:
					textoValido = True
				else: 
					print("Error. El texto debe tener un maximo de 60 caracteres")
					print("contar con al menos 3 palabras, sin mayusculas seguidas")
			
			else: 
				print("El cuit ingresado es invalido, intente de nuevo")
			if textoValido:
				salario = int(input("Salario ofrecido: "))
				if salario <= 0:
					print("Error. El salario no puede ser negativo ni igual a cero")
				else:
					salarioValido = True
			
			if salarioValido and cuitValido and textoValido:
				print("*******************DATOS ENCONTRADOS*******************")
				print(f"CUIT: {cuit}")
				print(f"Descripcion: {texto}")
				print(f"Salario: {salario}$")
			else:
				print("No se encontraron los datos")
	print("Gracias por usar el pograma!")

portalTrabajo()
