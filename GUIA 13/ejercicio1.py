
def analizar_texto():
	texto = input("Ingrese texto: ")
	letras = 0; flag_si = False; palabras_si = 0
	vocales = "AaáÁEeéÉIiíÍOoóÓUuúÚ"; palabras_impares_vocales = 0
	cant_vocales = 0; palabras_una_vocal = 0; caracter_anterior = ""
	primer_letra = ""; flag_cc = False; palabras_cc = 0
	total_palabras = 0 ; palabra_mas_corta = 10000
	palabras_misma_letra = 0; acumular_letras = 0
	for caracter in texto:
		if caracter == " " or caracter == ".":
			total_palabras += 1
			acumular_letras += letras
			if flag_si:
				palabras_si += 1
			if caracter_anterior in vocales and letras % 2 != 0:
				palabras_impares_vocales += 1
			if cant_vocales == 1:
				palabras_una_vocal += 1
			if primer_letra == caracter_anterior:
				palabras_misma_letra += 1
			if flag_cc:
				palabras_cc += 1
			if letras < palabra_mas_corta:
				palabra_mas_corta = letras
			flag_si = False; letras = 0; cant_vocales = 0;  flag_cc = False
		else:
			letras += 1
			if letras == 1:
				primer_letra = caracter
			if caracter_anterior in "sS" and caracter == "i" and letras == 2:
				flag_si = True
			if caracter in vocales:
				cant_vocales += 1
			if caracter_anterior == "C" and caracter == "C":
				flag_cc = True
			caracter_anterior = caracter
	promedio = acumular_letras // total_palabras
	porcent = palabras_impares_vocales * 100 // total_palabras
	print(f"Punto 1: {palabras_si}")
	print(f"Punto 2: {palabras_impares_vocales}")
	print(f"Punto 3: {palabras_una_vocal}")
	print(f"Punto 4: {palabras_misma_letra}")
	print(f"Punto 5: {palabras_cc}")
	print(f"Punto 6: {porcent}%")
	print(f"Punto 7: {palabra_mas_corta}")
	print(f"Punto 8: {promedio}")
analizar_texto()
