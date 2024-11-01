
def enunciado_tipo_parcial():
	archivo = open("entrada.txt", "r")
	texto = archivo.read()
	# PUNTO 1
	vocales = "AaáÁEeéÉIiíÍOoóÓUuúÚ"; letras = 0
	flag_consonante_3_5 = False; ultimo_caracter = None; punto_1 = 0
	# PUNTO 2
	punto_2 = 0; flag_digitos = False
	# PUNTO 3
	contador_punto_3 = 0; acumulador_punto_3 = 0
	aparicion_t = 0; aparicion_s = 0
	# PUNTO 4
	palabras = 0; flag_ma = False; primer_letra_texto = None
	flag_primer_letra = False; punto_4 = 0
	for caracter in texto:
		if caracter == " " or caracter == ".":
			palabras += 1
			if ultimo_caracter != None and ultimo_caracter in vocales and flag_consonante_3_5:
				punto_1 += 1
			if flag_digitos and letras % 2 != 0:
				punto_2 += 1
			if aparicion_s != 0 and aparicion_t != 0 and aparicion_t < aparicion_s:
				contador_punto_3 += 1
				acumulador_punto_3 += letras
			if flag_ma and flag_primer_letra:
				punto_4 += 1
			flag_consonante_3_5 = False; letras = 0; flag_digitos = False
			aparicion_t = 0; aparicion_s = 0; flag_ma = False; flag_primer_letra = False
		else:
			letras += 1
			if palabras == 0:
				primer_letra_texto = caracter.lower()
			if (letras == 3 or letras == 5) and not(caracter in vocales):
				flag_consonante_3_5 = True
			if caracter.isnumeric():
				flag_digitos = True
			if caracter in "Tt":
				aparicion_t = letras
			if caracter in "Ss":
				aparicion_s = letras
			if ultimo_caracter != None and ultimo_caracter in "Mm" and caracter in "aá" and letras >= 4:
				flag_ma = True
			if caracter == primer_letra_texto:
				flag_primer_letra = True
			ultimo_caracter = caracter
	if contador_punto_3 != 0:
		punto_3 = acumulador_punto_3 / contador_punto_3
	else:
		punto_3 = 0
	print(f"Punto 1: {punto_1}")
	print(f"Punto 2: {punto_2}")
	print(f"Punto 3: {punto_3}")
	print(f"Punto 4: {punto_4}")
	archivo.close()


if __name__ == "__main__":
	enunciado_tipo_parcial()
