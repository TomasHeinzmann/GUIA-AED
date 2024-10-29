def analizar_texto():
	texto = input("Ingrese texto: ")
	letras = 0; flag_m = False; flag_b = False
	cant_palabras_mb = 0; vocales = "AaáÁEeéÉIiíÍOoóÓUúuÚ"
	cant_palabras_pvocal = 0; cant_palabras_primero_y_ultimo = 0
	p_vocal = False
	for caracter in texto:
		if caracter == " " or caracter == ".":
			if flag_b and flag_m:
				cant_palabras_mb += 1
			if p_vocal:
				cant_palabras_pvocal += 1
			if primer_caracter == caracter_anterior:
				cant_palabras_primero_y_ultimo += 1
			letras = 0; flag_m = False; flag_b = False; p_vocal = False
		else:
			letras += 1
			if letras == 1:
				primer_caracter = caracter
			if letras >= 3 and caracter == "m":
				flag_m = True
			if letras >= 3 and caracter == "b":
				flag_b = True
			if letras == 2 and caracter_anterior in "pP" and caracter in vocales:
				p_vocal = True
			caracter_anterior = caracter
	print(f"Palabras con una m y una b despues de la tercer letra: {cant_palabras_mb}")
	print(f"Palabras que empiezan con 'p' seguida de una vocal: {cant_palabras_pvocal}")
	print(f"Palabras que empiezan y terminan en la misma letra: {cant_palabras_primero_y_ultimo}")
analizar_texto()
