
def analizar_texto():
	texto = input("Ingrese texto: ")
	palabra_larga = 0; letras = 0
	otras_vocales = "EeéÉIiíÍOoóÓUuúÚ"; flag_otras_vocales = False
	cant_solo_a = 0; palabras = 0
	for caracter in texto:
		if caracter == " " or caracter == ".":
			palabras += 1
			if palabra_larga == None:
				palabra_larga = letras
			elif palabra_larga < letras:
				palabra_larga = letras
			if not flag_otras_vocales:
				cant_solo_a += 1
			flag_otras_vocales = False
			letras = 0
		else:
			letras += 1
			if caracter in otras_vocales:
				flag_otras_vocales = True
	
	porcent = cant_solo_a * 100 / palabras
	print(f"Longitud de la palabra mas larga: {palabra_larga}")
	print(f"Palabras que tienen como unica vocal la letra 'a': {cant_solo_a}")
	print(f"Porcentaje del punto anterior sobre todas las palabras: {round(porcent)}%")

analizar_texto()
