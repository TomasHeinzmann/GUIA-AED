def parcial_1():
	texto = input("Ingrese texto: ")
	vocales = "AaáÁEeéÉIiíÍOoóÓUuúÚ"; ultima_letra = None; letras = 0
	palabras_termina_vocal = 0; cant_consonantes = 0
	cant_vocales = 0; cant_caracteres = 0; mayor_consonantes = 0
	orden_mayor_consonantes = 0; palabras = 0
	acumulador_consonantes = 0; acumulador_vocales = 0
	primer_letra_texto = None; primer_letra_palabra = None
	st_flag = False; cant_st_primer_letra = 0
	consonantes = "QWRTYPSDFGHJKLÑMNBVCXZqwrtypsdfghjklñmnbvcxz"
	for letra in texto: 
		if letra == " " or letra == ".":
			palabras += 1
			acumulador_consonantes += cant_consonantes
			acumulador_vocales += cant_vocales
			if ultima_letra in vocales:
				palabras_termina_vocal += 1
			if cant_consonantes > mayor_consonantes:
				mayor_consonantes = cant_consonantes
				orden_mayor_consonantes = palabras
			if st_flag and primer_letra_palabra == primer_letra_texto:
				cant_st_primer_letra += 1
			cant_vocales = 0; cant_consonantes = 0;letras = 0
			st_flag = False
		else:
			letras += 1
			if palabras == 0 and letras == 1:
				primer_letra_texto = letra.lower()
			if letras == 1:
				primer_letra_palabra = letra.lower()
			if letra in consonantes:
				cant_consonantes += 1
			elif letra in vocales:
				cant_vocales += 1
			cant_caracteres += 1
			if ultima_letra == "s" and letra == "t":
				st_flag = True
			ultima_letra = letra
	porcent_vocales = acumulador_vocales * 100 / cant_caracteres
	porcent_consonantes = acumulador_consonantes * 100 / cant_caracteres
	print(f"Palabras que terminan en vocal: {palabras_termina_vocal}")
	print(f"Porcentaje de consonantes: {porcent_consonantes}%")
	print(f"Porcentaje de vocales: {porcent_vocales}%")
	print(f"Numero de orden de la palabra con mas consonantes: {orden_mayor_consonantes}")
	print(f"Palabras que empiezan con la primer letra del texto y tienen 'st': {cant_st_primer_letra}")

parcial_1()
