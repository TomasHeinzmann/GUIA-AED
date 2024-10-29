def analizar_texto():
	texto = input("Ingrese un texto: ")
	vocales = "AaáÁEeéÉIiíÍOoóÓUuúÚ"; cant_vocales = 0
	palabras_vocales = 0; numero_encontrado = False
	letras = 0; palabras_digitos_cuatro = 0; flag_primer_letra = True
	primer_letra = ""; ultima_letra = None; menor = 10000
	cant_palabras_men = 0; flag_me = False; flag_men = False
	palabras_totales = 0; letras_men = 0
	for caracter in texto:
		if caracter == " " or caracter == ".":
			palabras_totales += 1
			if cant_vocales == 3:
				palabras_vocales += 1
			if numero_encontrado and letras > 4:
				palabras_digitos_cuatro += 1
			if primer_letra == ultima_letra and letras < menor:
				menor_orden = palabras_totales
			if flag_men and letras // 2 == letras_men:
				cant_palabras_men += 1
			cant_vocales = 0; numero_encontrado = False; letras	= 0
			flag_me = False; flag_men = False
		else:
			if flag_primer_letra:
				primer_letra = caracter
				flag_primer_letra = False
			letras += 1
			if caracter in vocales:
				cant_vocales += 1
			if caracter.isnumeric():
				numero_encontrado = True
				letras -= 1
			if ultima_letra == "m" and caracter == "e":
				flag_me = True
			if flag_me and caracter == "n":
				flag_me = False
				flag_men = True
				letras_men = letras
			ultima_letra = caracter
	porcent = palabras_digitos_cuatro * 100 // palabras_totales
	print(f"Palabras con 3 vocales: {palabras_vocales}")
	print(f"Porcentaje de palabras con mas de 4 letras y un digito: {porcent}%")
	if menor_orden:
		print(f"Orden de la palabra mas corta del texto que termina con la misma letra que empieza el texto: {menor_orden}")
	print(f"Palabras con 'men' en la primera mitad del la palabra: {cant_palabras_men}")
