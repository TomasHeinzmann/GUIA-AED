
def parcial_2_1k03():
	texto = input("Ingrese texto: ")
	letras = 0; flag_n = False; cant_n = 0; palabras_t = 0
	letras_t = 0; flag_t = False; flag_s = False; flag_e = False
	flag_a = False; cant_a_s_noe = 0; ultima_letra = None
	flag_re = False; cant_reo = 0
	for letra in texto:
		if letra == " " or letra == ".":
			if letras > 4 and flag_n:
				cant_n += 1
			if flag_t:
				palabras_t += 1
				letras_t += letras
			if flag_a and flag_s and not flag_e:
				cant_a_s_noe += 1
			if flag_re and ultima_letra in "oó":
				cant_reo += 1
			flag_n = False; flag_t = False; flag_a = False
			flag_s = False; flag_e = False; flag_re = False
			letras = 0
		else:
			letras += 1
			if letra in "Nn":
				flag_n = True
			elif letra in "Tt" and letras == 1:
				flag_t = True
			elif letra in "AaáA":
				flag_a = True
			elif letra in "Ss":
				flag_s = True
			elif letra in "EeéÉ":
				flag_e = True
			if ultima_letra != None and ultima_letra in "Rr" and letra == "e":
				flag_re = True
			ultima_letra = letra
	if palabras_t != 0:
		prom_t = letras_t / palabras_t
	else:
		prom_t = 0
	print(f"Palabras con mas de cuatro letras con una 'n': {cant_n}")
	print(f"Promedio de letras que empiezan por 't': {prom_t}")
	print(f"Palabras con 'a' y 's' pero sin 'e': {cant_a_s_noe}")
	print(f"Palabras que contienen la expresion 're' y su ultima letra es 'o': {cant_reo}")
