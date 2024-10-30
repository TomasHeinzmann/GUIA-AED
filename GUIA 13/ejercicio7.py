
def parcial_2_1k10():
	texto = input("Ingresa texto: ")
	cant_vocales = 0; letras = 0; punto_1 = 0
	vocales = "AaáÁEeéÉIiíÍOoóÓUuúÚ"; flag_punto_2 = False
	comparador = 10000; punto_2 = 0; ultima_letra = None; punto_3 = 0
	palabras = 0; palabras_ga = 0; flag_punto_3 = False
	flag_punto_4 = False
	for letra in texto:
		if letra == " " or letra == ".":
			palabras += 1
			if cant_vocales >= 3 and letras >= 4:
				punto_1 += 1
			if flag_punto_2 and letras < comparador:
				punto_2 = letras
				comparador = letras
			if flag_punto_3 and (ultima_letra == "n" or ultima_letra == "a"):
				punto_3 += 1
			if flag_punto_4:
				palabras_ga += 1
			letras = 0; cant_vocales = 0; flag_punto_2 = False
			flag_punto_3 = False; flag_punto_4 = False
		else:
			letras += 1
			if letra in vocales:
				cant_vocales += 1
			if letras == 2 and not letra in vocales:
				flag_punto_2 = True
			if letras == 1 and letra in "Vv" or letra in "Pp":
				flag_punto_3 = True
			if ultima_letra != None and ultima_letra in "Gg" and letra == "a":
				flag_punto_4 = True
			ultima_letra = letra
	punto_4 = palabras_ga * 100 / palabras
	print(f"Palabras que tenían por lo menos tres vocales y más de cuatro letras: {punto_1}")
	print(f"Longitud de la palabra más corta de entre las que contenían una consonante en la segunda posición: {punto_2}")
	print(f"Palabras empiezan con 'v' o con 'p' y terminan con 'n' o con 'a': {punto_3}")
	print(f"Porcentaje de palabras que contenían la expresión 'ga' con respecto al total del palabras del texto: {punto_4}%")

parcial_2_1k10()
