def palabraEnmascarada(palabra):
	nuevaPalabra = ""
	for letra in range(len(palabra)):
		if 0 < letra < (len(palabra) - 1):
			nuevaPalabra += "*"
		else:
			nuevaPalabra += palabra[letra]
	return nuevaPalabra		
	
