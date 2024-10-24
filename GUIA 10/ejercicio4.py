
def analizarTexto():
	texto = input("Ingrese un texto finalizado en un punto: ")
	contLetras = contPalabras = 0
	contNa = 0
	pFlag = False
	aFlag = False
	vocales = "AaáÁEeéÉIiíÍOoÓóUuúÚ"
	cantVocales = palabrasVocales = 0
	palabrasCinco = 0
	for caracter in texto:
		if caracter == " " or caracter == ".":
			contPalabras += 1
			if cantVocales > 2:
				palabrasVocales += 1
			if pFlag and aFlag and caracterAnterior == "n":
				contNa += 1
			if contLetras > 5:
				palabrasCinco += 1
			cantVocales = 0
			contLetras = 0
			pFlag = False
			aFlag = False
		else:
			contLetras += 1
			if contLetras == 1 and caracter == "p":
				pFlag = True
			elif contLetras == 2 and caracter == "a":
				aFlag = True
			if contLetras > 3 and caracter in vocales:
				cantVocales += 1
			caracterAnterior = caracter
	porcent = palabrasVocales * 100 // contPalabras
	print(f"Cantidad de palabras que empiezan con pa y terminan en n: {contNa}")
	print(f"Palabras con mas de dos vocales despues de la tercer letra: {palabrasVocales}")
	print(f"Porcentaje punto anterior: {porcent}%")
	print(f"Palabras con mas de 5 letras: {palabrasCinco}")

analizarTexto()
