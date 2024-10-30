
def parcial_1_1k06():
	texto = input("Ingrese texto: ")
	digitos = 0; mas_dos_digitos = 0; ultima_letra = None
	flag_la = False; cant_la = 0; letras_la = 0; letras = 0
	flag_ll = False; flag_v = False; cant_ll_v = 0
	for letra in texto:
		if letra == " " or letra == ".":
			if digitos >= 2:
				mas_dos_digitos += 1
			if flag_la:
				cant_la += 1
				letras_la += letras
			if flag_ll and flag_v:
				cant_ll_v += 1
			digitos = 0; flag_la = False; letras = 0; flag_ll = False
			flag_v = False
		else:
			letras += 1
			if letra.isnumeric():
				digitos += 1
			if ultima_letra != None and ultima_letra in "Ll" and letra == "a" and letras == 2:
				flag_la = True
			if ultima_letra != None and ultima_letra in "Ll" and letra == "l" and letras == 2:
				flag_ll = True
			if letra in "Vv":
				flag_v = True
			ultima_letra = letra
	if cant_la != 0:
		prom_la = letras_la / cant_la
	else:
		prom_la = 0
	print(f"Palabras que incluyen dos digitos: {mas_dos_digitos}")
	print(f"Palabras que comienzan con 'la': {cant_la}")
	print(f"Promedio de letras por palabra del punto anterior: {prom_la}")
	print(f"Palabras que empienzan con 'll' y tienen una 'v': {cant_ll_v}")

parcial_1_1k06()
