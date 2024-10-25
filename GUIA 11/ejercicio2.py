
def analizarTexto():
	texto = input("Ingrese texto a analizar: ")
	vocales = "AaáÁEeéÉIiíÍOoóÓUuÚú"; cantLetras = 0
	consonantesVocales = 0; flagLi = False; cantLi = 0
	palabrasCortas = 0; cantPalabras = 0
	for caracter in texto:
		if caracter == " " or caracter == ".":
			cantPalabras += 1
			if ultimaLetra in vocales and primerConsonante:
				consonantesVocales += 1
			if flagLi:
				cantLi += 1
			if cantLetras < 4:
				palabrasCortas += 1
			cantLetras = 0; flagLi = False
		else:
			cantLetras += 1
			if cantLetras == 1 and caracter not in vocales:
				primerConsonante = caracter
			if cantLetras > 3 and ultimaLetra == "l" and caracter == "i":
				flagLi = True
			ultimaLetra = caracter
	porcent = palabrasCortas * 100 // cantPalabras
	print(f"Palabras que empiezan en consonantes y terminan en vocales: {consonantesVocales}")
	print(f"Palabras con 'li' despues de la tercera letra: {cantLi}")
	print(f"Palabras con menos de 4 letras: {palabrasCortas}")
	print(f"Porcentaje de palabras con menos de 4 letras sobre todo el texto: {porcent}%")

analizarTexto()
