def analizar_texto():
	texto = input("Ingrese un texto: ")
	palabras = 0; letras = 0; acum_letras = 0; ultimo_caracter = None
	termina_vocal = 0; palabra_larga = 0; flag_lvocal = False
	flag_num = False
	lvocal_palabras = 0; numeros_primer_mitad = 0
	vocales = "AaáÁEeéÉIiíÍOoóÓUuúÚ"
	for caracter in texto:
		if caracter == " " or caracter == ".":
			palabras += 1
			acum_letras += letras
			if ultimo_caracter in vocales:
				termina_vocal += 1
			if letras > palabra_larga:
				palabra_larga = palabras
			if flag_lvocal:
				lvocal_palabras += 1
			if flag_num and (letras // 2) > posicion:
				numeros_primer_mitad += 1
			letras = 0; flag_lvocal = False; flag_num = False
		else:
			letras += 1
			if ultimo_caracter != None and ultimo_caracter in "lL" and caracter in vocales:
				flag_lvocal = True
			if caracter.isnumeric():
				flag_num = True
				posicion = letras
			ultimo_caracter = caracter
	prom_letras_palabra = acum_letras // palabras
	print(f"Promedio de letras por palabra del texto: {prom_letras_palabra}")
	print(f"Cantidad de palabras terminadas en vocal: {termina_vocal}")
	print(f"Orden de la palabra mas larga del texto: {palabra_larga}")
	print(f"Cantidad de pelabras con 'l + vocal': {lvocal_palabras}")
	print(f"Cantidad de palabras con un digito en la primer mitad: {numeros_primer_mitad}")
