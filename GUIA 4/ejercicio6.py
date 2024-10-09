def palabraAnalisis ():
	palabra = input("Ingrese palabra a analizar: ")
	vocales = "aAeEiIoOuU"
	print(f"La palabra tiene {len(palabra)} letras")
	if palabra[len(palabra)-1] in vocales:
		print("La palabra termina en vocal")
	else:
		print("La palabra no termina en vocal")
		
palabraAnalisis()
