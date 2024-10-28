
def analizar_texto():
	texto = input("Ingrese un texto: ")
	flag_numero_encontrado = False; palabras_con_numero = 0
	tres_o_menos = 0; cuatro_a_seis = 0; mas_de_seis = 0
	letras = 0; palabra_larga = 0; palabras_de = 0
	letra_anterior = None; primera_mitad = 0; flag_de = False
	for caracter in texto:
		if caracter == " " or caracter == ".":
			if flag_numero_encontrado:
				palabras_con_numero += 1
			if letras <= 3:
				tres_o_menos += 1
			elif 6 >= letras >= 4:
				cuatro_a_seis += 1
			else:
				mas_de_seis += 1
			if letras > palabra_larga:
				palabra_larga = letras
			if primera_mitad < letras // 2 and flag_de:
				palabras_de += 1
				flag_de = False
			flag_numero_encontrado = False
			letras = 0
		else:
			letras += 1
			if caracter.isnumeric():
				flag_numero_encontrado = True
			if letra_anterior != None and letra_anterior == "d" and caracter == "e":
				flag_de = True
				primera_mitad = letras
			letra_anterior = caracter
	
	print(f"Palabras con un numero en lugar de un caracter: {palabras_con_numero}")
	print(f"Palabras con tres o menos letras: {tres_o_menos}")
	print(f"Palabras con cuatro a seis letras: {cuatro_a_seis}")
	print(f"Palabras con mas de seis letras: {mas_de_seis}")
	print(f"Longitud de la palabra mas larga del texto: {palabra_larga}")
	print(f"Palabras con la expresion 'de' en la primera mitad: {palabras_de}")

analizar_texto()
