def analizar_texto():
	texto = input("Ingrese texto: ")
	comparar = int(input("Ingrese un valor con el que comparar la longitud de las palabras: "))
	while comparar <= 0:
		print("Error. El valor debe ser mayor a 0")
		comparar = int(input("Ingrese un valor con el que comparar la longitud de las palabras: "))
	vocales = "AaáÁEeéÉIiíÍOoÓóuUúÚ"
	vocal1 = ""; vocales_distintas = False; letras = 0
	cant_vocales_distintas = 0; letras_anterior = None
	palabras_multiplo_anterior = 0; palabras_mayor = 0
	palabras_totales = 0; letras_totales = 0; palabras_mayor_promedio = 0
	numero_vocales = 0
	for caracter in texto:
		if caracter == " " or caracter == ".":
			palabras_totales += 1
			letras_totales += letras
			if vocales_distintas:
				cant_vocales_distintas += 1
			if letras_anterior != None and letras % letras_anterior	== 0:
				palabras_multiplo_anterior += 1
			if letras > comparar:
				palabras_mayor += 1
			letras_anterior = letras; vocales_distintas = False
			letras = 0
			numero_vocales = 0 
		else:
			letras += 1
			if caracter in vocales and numero_vocales == 0:
				vocal1 = caracter
				numero_vocales += 1
			if vocal1 != caracter and caracter in vocales:
				vocales_distintas = True
	prom = letras_totales // palabras_totales
	for caracter in texto:
		if caracter == " " or caracter == ".":
			if letras > prom:
				palabras_mayor_promedio += 1
			letras = 0
		else:
			letras += 1
	print(f"Punto 1: {cant_vocales_distintas}")
	print(f"Punto 2: {palabras_multiplo_anterior}")
	print(f"Punto 3: {palabras_mayor}")
	print(f"Punto 4: {palabras_mayor_promedio}")
