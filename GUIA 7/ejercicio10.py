def direccionTransito():
	patente = input("Ingrese patente: ")
	longPantente = len(patente)
	validaAntigua = False
	validaNueva = False
	if longPantente == 6:
		contIndex = 0
		for caracter in patente:
			if caracter.isalpha() and 2 >= contIndex >= 0:
				validaAntigua = True
				contIndex += 1
			elif caracter.isnumeric() and 5 >= contIndex >= 3:
				validaAntigua = True
				contIndex += 1
			else:
				validaAntigua = False
				break 
	elif longPantente == 7:
		contIndex = 0
		for caracter in patente:
			if caracter.isalpha() and 1 >= contIndex >= 0:
				validaNueva = True
				contIndex += 1
			elif caracter.isnumeric() and 4 >= contIndex >= 2:
				validaNueva = True
				contIndex += 1
			elif caracter.isalpha() and 6 >= contIndex >= 5:
				validaNueva = True
				contIndex += 1
			else:
				validaNueva = False
	if validaNueva:
		print("La patente esta en formato nuevo")
		print("La patente es valida. Contiene letras y numeros de acuerdo a lo esperado")
	elif validaAntigua:
		print("La patente esta en formato antiguo")
		print("La patente es valida. Contiene letras y numeros de acuerdo a lo esperado")
	else:
		print("La pantente no es valida. No contiene letras y numeros de acuerdo a lo esperado")
