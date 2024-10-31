

def simulacro_2_parcial_2():
	archivo = open("entrada.txt", "r")
	texto = archivo.read()
	# PUNTO 1
	letras = 0; vocales = "AaáÁEeéÉIiíÍOoóOUuúÚ"; cantidad_vocales = 0
	cantidad_consonantes = 0; punto_1 = 0
	# PUNTO 2
	flag_digito = False; flag_no_p = True; punto_2 = None
	# PUNTO 3
	acumulador_punto3 = 0; contador_punto3 = 0
	contador_s = 0; punto_3 = 0
	# PUNTO 4
	flag_vocal_primero = False; punto_4 = 0; ultimo_caracter = None
	flag_ra = False
	for caracter in texto:
		if caracter == " " or caracter == ".":
			if letras % 2 == 0 and letras // 2 == cantidad_vocales:
				punto_1 += 1
			if flag_digito and flag_no_p and punto_2 == None:
				punto_2 = letras
			elif flag_digito and flag_no_p and punto_2 < letras:
				punto_2 = letras
			if letras > 2 and contador_s:
				acumulador_punto3 += letras
				contador_punto3 += 1
			if flag_vocal_primero and flag_ra:
				punto_4 += 1
			letras = 0; cantidad_consonantes = 0; cantidad_vocales = 0
			flag_digito = False; flag_no_p = True
			flag_vocal_primero = False; flag_ra = False
		else:
			letras += 1
			if caracter in vocales:
				cantidad_vocales += 1
			else:
				cantidad_consonantes += 1
			if caracter.isnumeric():
				flag_digito = True
			elif caracter in "pP":
				flag_no_p = False
			if caracter in "Ss":
				contador_s += 1
			if ultimo_caracter != None and ultimo_caracter in "Rr" and caracter in "AaáÁ":
				flag_ra = True
			if letras <= 2 and caracter in vocales:
				flag_vocal_primero = True
			ultimo_caracter = caracter
	if contador_punto3 != 0:
		punto_3 = acumulador_punto3 // contador_punto3
	else:
		punto_3 = 0
	archivo.close()
	print(f"Punto 1: {punto_1}")
	print(f"Punto 2: {punto_2}")
	print(f"Punto 3: {punto_3}")
	print(f"Punto 4: {punto_4}")
if __name__ == "__main__":
	simulacro_2_parcial_2()
