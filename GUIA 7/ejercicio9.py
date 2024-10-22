def validarCuenta():
	i = -1
	puntosSeguidos = False
	caracterAnterior = None
	while i != 0:
		cuenta = input("Ingrese cuenta (formato: nombre@dominio): ")
		for caracter in cuenta:
			if caracterAnterior != None:
				if caracterAnterior == "." and caracter == ".":
					puntosSeguidos = True 
			caracterAnterior = caracter
		if cuenta.startswith("@") or cuenta.endswith("@") or cuenta.count("@") > 1:
			print("La cuenta no es valida")
		elif puntosSeguidos:
			print("La cuenta no es valida")
		elif cuenta.startswith(".") or cuenta.endswith("."):
			print("La cuenta no es valida")
		else:
			print("La cuenta es valida!")
			i = 0
		puntosSeguidos = False

