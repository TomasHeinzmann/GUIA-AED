def analizarTexto():
	texto = input("Ingrese texto: ")
	contLetras = 0; contPalabras = 0; palabrasVocal = 0
	vocales = "AaáÁEeéÉIiíÍOoóÓUuÚú"; flagAnterior = False
	palabrasAnterior = 0 ; palabrasTotal = 0; letraAnterior = None
	letraTermina = None
	for caracter in texto:
		if caracter == " " or caracter == ".":
			palabrasTotal += 1
			if primerLetra in vocales and letraAnterior in vocales:
				palabrasVocal += 1
			if flagAnterior:
				palabrasAnterior += 1
			contLetras = 0 ; letraTermina = letraAnterior
			flagAnterior = False
		else:
			contLetras += 1
			if contLetras == 1:
				primerLetra = caracter
			if letraTermina == primerLetra:
				flagAnterior = True
			letraAnterior = caracter
	porcent = palabrasVocal * 100 // palabrasTotal
	
	print(f"Palabras que empiezan y terminan en vocal: {palabrasVocal}")
	print(f"Palabras que comienzan con la misma letra que termina la anterior: {palabrasAnterior}")
	print(f"Porcentaje del punto 1 sobre todas las palabras: {porcent}%")
