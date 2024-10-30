
def promedio(acumulador, total):
	if total != 0:
		return acumulador / total
	else:
		return 0

def parcial_1k15_T2():
	texto = input("Ingrese texto: ")
	digitos = 0; letras = 0; solo_digitos = 0
	ultima_letra = None; termina_digito_con_letra = 0
	longitud_corta = 1000; orden_corta = 0; palabras = 0
	acum_digitos = 0; 
	flag_ch = False; cant_ch = 0
	for letra in texto:
		if letra == " " or letra == ".":
			palabras += 1
			if letras == digitos:
				solo_digitos += 1
				acum_digitos += digitos
			if ultima_letra != None and ultima_letra.isnumeric() and digitos != letras:
				termina_digito_con_letra += 1
			if letras < longitud_corta:
				longitud_corta = letras
				orden_corta = palabras
			if flag_ch:
				cant_ch += 1
			digitos = 0; letras = 0; flag_ch = False
		else:
			letras += 1
			if letra.isnumeric():
				digitos += 1
			if letras > 4 and ultima_letra == "c" and letra == "h":
				flag_ch = True
			ultima_letra = letra
	prom_digitos = promedio(acum_digitos, solo_digitos)
	print(f"Promedio de dígitos por palabra de las palabras formadas solo por dígitos que posee el texto: {prom_digitos}")
	print(f"Cantidad de palabras que finalizan con un dígito y tienen al menos una letra: {termina_digito_con_letra}")
	print(f"Longitud de la palabra más corta del texto: {longitud_corta}")
	print(f"Posición de la palabra más corta del texto: {orden_corta}")
	print(f"Cantidad de palabras que tienen las letras “ch” continuas pero comenzando esa secuencia a partir de la cuarta letra en adelante: {cant_ch}")
