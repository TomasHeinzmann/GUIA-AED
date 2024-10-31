
def simulacro_parcial_2():
	texto = open("entrada.txt", "r")
	leer = texto.read()
	# PUNTO 1
	mayusculas = "QWERTYUIOPASDFGHJKLÑZXCVBNM"
	letras = 0; flag_impares = False; flag_minusculas = True
	punto_1 = 0
	# PUNTO 2
	vocales = "AaáÁEeéÉIiíÍOoóÓUuúÚ"; punto_2 = None; flag_b = False
	flag_empieza_vocal = False
	# PUNTO 3
	flag_a_m = False; cantidad_vocales = 0; cantidad_consonantes = 0
	acumulador_punto_3 = 0; contador_punto_3 = 0; punto_3 = 0
	# PUNTO 4
	caracter_anterior = None; cantidad_dvocal = 0; punto_4 = 0
	for caracter in leer:
		if caracter == " " or caracter == ".":
			if flag_impares and not(flag_minusculas):
				punto_1 += 1
			if punto_2 == None and flag_b and flag_empieza_vocal:
				punto_2 = letras
			elif flag_b and flag_empieza_vocal and letras > punto_2:
				punto_2 = letras
			if cantidad_consonantes > cantidad_vocales and not(flag_a_m):
				acumulador_punto_3 += letras
				contador_punto_3 += 1
			if cantidad_dvocal >= 2 and caracter_anterior in vocales:
				punto_4 += 1
			flag_impares = False; letras = 0; flag_minusculas = True
			flag_b = False; flag_empieza_vocal = False
			flag_a_m = False; cantidad_vocales = 0; cantidad_consonantes = 0
			cantidad_dvocal = 0
		else:
			letras += 1
			if caracter in vocales:
				cantidad_vocales += 1
			else:
				cantidad_consonantes += 1
			if letras == 1 and caracter.isnumeric():
				digito = int(caracter)
				if digito % 2 != 0:
					flag_impares = True
			elif letras == 1 and caracter in vocales:
				flag_empieza_vocal = True 
			if caracter in mayusculas:
				flag_minusculas = False
			if caracter in "Bb":
				flag_b = True
			if caracter in "AaáÁMm":
				flag_a_m = True
			if caracter_anterior != None and caracter_anterior in "Dd" and caracter in vocales:
				cantidad_dvocal += 1
			caracter_anterior = caracter
	if contador_punto_3 != 0:
		punto_3 = acumulador_punto_3 // contador_punto_3
	else:
		punto_3 = 0
	texto.close()
	print(f"Punto 1: {punto_1}")
	print(f"Punto 2: {punto_2}")
	print(f"Punto 3: {punto_3}")
	print(f"Punto 4: {punto_4}")
	

if __name__ == "__main__":
	simulacro_parcial_2()
