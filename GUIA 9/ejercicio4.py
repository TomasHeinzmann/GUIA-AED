def menu():
	print("****************MENU DE OPCIONES****************")
	print("1) Validar CUIT")
	print("2) Validar DNI")
	print("0) Salir")
	print("************************************************")
	opc = int(input("Ingrese una opcion: "))
	while opc > 2 or opc < 0:
		print("Error, el valor se sale de los parametros")
		opc = int(input("Ingrese una opcion: "))
	return opc


def validarDatos():
	opc = -1
	while opc != 0:
		opc = menu()
		if opc == 1:
			primerValidacion = segundaValidacion = False
			cuit = input("Ingrese su cuit: ")
			caracteresCuit = int(len(cuit))
			if caracteresCuit == 13 and cuit[2] == "-" and cuit[11] == "-":
				primerValidacion = True
			else:
				pass
			if primerValidacion:
				sumTotal = 0
				
				for caracter in cuit:
					if caracter != "-" and caracter != cuit[12]:
						num = int(caracter)
						res = num * 5432765432
						sumTotal += res
					else:
						pass
				
				resto11 = sumTotal % 11
				resultado = 11 - resto11
				print(resto11)
				print(resultado)
				
				if resultado == int(cuit[caracteresCuit - 1]):
					segundaValidacion = True
			else:
				pass
			if primerValidacion and segundaValidacion:
				print("El cuit es valido!")
			elif primerValidacion:
				print("El cuit se ingreso correctamente, pero el digito verificador es distinto")
		elif opc == 2:
			dni = input("Ingrese DNI (formto XX.XXX.XXX): ")
			for caracter in dni:
				if caracter == "." and caracter == ".":
					dniValido = True
				elif caracter.isnumeric():
					dniValido = True
				else:
					dniValido = False
					break
			if dniValido:
				print("El DNI es valido")
			else:
				print("El DNI es invalido")
		else:
			pass
	print("Gracias por usar el programa!")

validarDatos()
			
