def analizar_texto():
	texto = input("Ingrese texto: ")
	mayusculas = "QWERTYUIOPÑLKJHGFDSAMNBVCXZ"; letras = 0
	flag_mayus = False; palabra_mayuscula = 0; cant_numeros = 0
	cant_e = 0; palabras_e = 0; acumulador_impares = 0; cant_impares = 0
	for caracter in texto:
		if caracter == " " or caracter == ".":
			if flag_mayus:
				palabra_mayuscula += 1
			if cant_e > 1:
				palabras_e += 1
			if letras % 2 != 0:
				acumulador_impares += letras
				cant_impares += 1
			letras = 0; flag_mayus = False; cant_e = 0
		else:
			letras += 1
			if letras == 1 and caracter in mayusculas:
				flag_mayus = True
			elif caracter.isnumeric():
				cant_numeros += 1
			if caracter in "Ee":
				cant_e += 1
	promedio_impares = acumulador_impares / cant_impares
	print(f"Palabras que empiezan con mayúscula: {palabra_mayuscula}")
	print(f"Numeros del 0 al 9 en todo el texto: {cant_numeros}")
	print(f"Palabras que tienen más de una e: {palabras_e}")
	print(f"Promedio de letras por palabra, para las palabras de longitud impar: {promedio_impares}")
