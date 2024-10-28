def analizar_texto():
	texto = input("Ingrese texto: ")
	cant_letras = 0; cant_letras_anterior = None
	palabras_long_Anterior = 0
	for caracter in texto:
		if caracter == " " or caracter == ".":
			if cant_letras_anterior != None and cant_letras_anterior <= cant_letras:
				palabras_long_Anterior += 1
			cant_letras_anterior = cant_letras
			cant_letras = 0
		else: 
			cant_letras += 1
	print(f"Cantidad de palabras precedidas por una palabra de igual o menor longitud: {palabras_long_Anterior}")
