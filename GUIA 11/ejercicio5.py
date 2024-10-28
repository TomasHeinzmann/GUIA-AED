
def analizar_texto():
	texto = input("Ingrese texto: ")
	cant_letras = 0; palabras_tres_letras = 0; palabras_totales = 0
	palabras_s = 0; ultimo_caracter = None; flag_dr = False
	flag_dre = False; palabras_dre = 0
	for caracter in texto:
		if caracter == " " or caracter == ".":
			palabras_totales += 1
			if cant_letras == 3:
				palabras_tres_letras += 1
			if ultimo_caracter == "s":
				palabras_s += 1
			if flag_dre:
				palabras_dre += 1
			flag_dre = False
			flag_dr = False
			cant_letras = 0
		else:
			cant_letras += 1
			if ultimo_caracter != None and ultimo_caracter == "d" and caracter == "r":
				flag_dr = True
			elif ultimo_caracter != None and ultimo_caracter == "r" and caracter == "e" and flag_dr:
				flag_dr = False
				flag_dre = True
			ultimo_caracter = caracter
	porcent = palabras_tres_letras * 100 // palabras_totales
	print(f"Palabras con 3 letras: {palabras_tres_letras}")
	print(f"Porcentaje de palabras con 3 letras sobre todo el texto: {porcent}%")
	print(f"Palabras que terminan en 's': {palabras_s}")
	print(f"Palabras que tienen 'dre': {palabras_dre}")

analizar_texto()
