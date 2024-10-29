def analizar_texto():
	texto = input("Ingrese un texto: ")
	letras = 0; cant_t = 0; palabras_t = 0; cant_mayor = 0
	cant_c = 0; palabras_totales = 0; flag_c = False
	letras_anterior = None
	for caracter in texto:
		if caracter == " " or caracter == ".":
			palabras_totales += 1
			if cant_t == 1:
				palabras_t += 1
			if letras_anterior != None and letras_anterior < letras:
				cant_mayor += 1
			if flag_c and letras % 2 == 0:
				cant_c += 1
			letras_anterior = letras
			cant_t = 0; letras = 0; flag_c = False
		else:
			letras += 1
			if caracter in "tT":
				cant_t += 1
			if letras == 1 and caracter in "Cc":
				flag_c = True
	
	porcent = palabras_t * 100 // palabras_totales
	print(f"Cantidad de palabras con solo una 't': {palabras_t}")
	print(f"Cantidad de palabras con mas letras que la anterior: {cant_mayor}")
	print(f"Cantidad de palabras pares que empiezan con 'c': {cant_c}")
	print(f"Porcentaje del  punto 1 sobre todo el texto: {porcent}%")

analizar_texto()
