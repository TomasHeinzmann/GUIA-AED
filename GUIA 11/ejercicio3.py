
def analizar_texto():
	texto = input("Ingrese texto: ")
	cont_vocales = 0; cont_letras_totales = 0; cont_letras = 0
	prom_letras = 0; cant_palabras = 0; may_long = 0
	caracter_Anterior = None ; cant_Ta = 0
	vocales = "AaáÁEeéÉIiíÍOoóÓUuúÚ"
	for caracter in texto:
		if caracter == " " or caracter == ".":
			prom_letras += cont_letras
			if cont_letras > may_long:
				may_long = cont_letras 
			cant_palabras += 1
			cont_letras = 0
		else:
			if caracter in vocales:
				cont_vocales += 1
			cont_letras += 1
			cont_letras_totales += 1
			if caracter_Anterior != None and caracter_Anterior in "Tt" and caracter == "a" and cont_letras == 2:
				cant_Ta += 1
			caracter_Anterior = caracter
	
	porcent = cont_vocales * 100 // cont_letras_totales
	prom_long = prom_letras // cant_palabras
	print(f"Porcentaje de vocales respecto al total de letras del texto: {porcent}%")
	print(f"Longitud promedio de las palabras: {prom_long}")
	print(f"Longitud de la palabra mas larga del texto: {may_long} letras")
	print(f"Cantidad de palabras que empiezan con 'ta': {cant_Ta} palabras")
