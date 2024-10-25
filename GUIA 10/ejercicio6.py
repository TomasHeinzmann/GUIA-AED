
def analizarTexto():
	texto = input("Ingrese texto finalizado con un punto: ")
	tresCincoSiete = 0 ; cantLetras = 0; cantPalabras = 0
	vocales = "AaáÁEeéÉIiíÍOoóÓUuúÚ" ; flagVocales = False ; vocalPalabras = 0
	cantVocales = 0 ; unaDosVocales = 0
	carAnterior = None ; peVeces = 0 ; pePalabras = 0
	for caracter in texto:
		if caracter == " " or caracter == ".":
			cantPalabras += 1
			if cantLetras == 3 or cantLetras == 5 or cantLetras == 7:
				tresCincoSiete += 1
			if flagVocales and cantLetras > 3:
				vocalPalabras += 1
			if cantVocales == 1 or cantVocales == 2:
				unaDosVocales += 1
			if peVeces > 1:
				pePalabras += 1
			cantLetras = 0 ; flagVocales = False ; cantVocales = 0
			peVeces = 0
		else:
			cantLetras += 1
			if cantLetras == 3 and caracter in vocales:
				flagVocales = True
			if caracter in vocales:
				cantVocales += 1
			if carAnterior != None and carAnterior in "Pp" and caracter in "Ee":
				peVeces += 1
			carAnterior = caracter
	porcent = unaDosVocales * 100 // cantPalabras
	
	print(f"Palabras con 3, 5 o 7 letras: {tresCincoSiete}") 
	print(f"Palabras de mas de 3 letras con una vocal en la tercer letra: {vocalPalabras}") 
	print(f"Porcentaje de las palabras con una o dos vocales: {porcent}%") 
	print(f"Palabras con mas de un 'pe': {pePalabras}")

analizarTexto() 
