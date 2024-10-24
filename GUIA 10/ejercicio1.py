
def analizarTexto():
	texto = input("Ingrese texto finalzado con un punto: ")
	palabrasCuatro = 0
	cantidadLetras = 0
	flagXoY = False
	contXoY = 0
	promLetras = cantPalabras = 0
	caracterAnterior = ""
	cantidadMo = palabrasMo = 0
	for caracter in texto:
		if caracter == " " or caracter == ".":
			promLetras += cantidadLetras
			cantPalabras += 1
			if cantidadLetras > 4:
				palabrasCuatro += 1
			else:
				pass
			if flagXoY:
				contXoY += 1
			else:
				pass
			if cantidadMo == 1:
				palabrasMo += 1
			else:
				pass
			cantidadLetras = 0
			flagXoY = False
			cantidadMo = 0
		else:
			cantidadLetras += 1
			if caracter in "Xx" or caracter in "Yy":
				flagXoY = True
			else:
				pass
			if caracterAnterior == "m" and caracter == "o":
				cantidadMo += 1
			else:
				pass
			caracterAnterior = caracter
	punto3 = promLetras // cantPalabras
	
	print(f"Palabras con mas de 4 letras: {palabrasCuatro}")
	print(f"Palabras tenian al menos una 'x' o 'y': {contXoY}")
	print(f"Promedio de letras por palabra del texto: {punto3}")
	print(f"Palabras que tuvieron 'mo' solo una vez: {palabrasMo}")
